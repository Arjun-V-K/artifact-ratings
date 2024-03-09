from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Artifact, db

import json

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def welcome():
    return render_template('welcome.html')

@main_bp.route('/view_artifacts_page')
def view_artifacts_page():
    artifacts = Artifact.query.all()
    return render_template('view_artifacts.html', artifacts=artifacts)

@main_bp.route('/add_artifacts_page')
def add_artifacts_page():
    return render_template('add_artifacts.html')

@main_bp.route('/add_artifact', methods=['POST'])
def add_artifact():
    set_key = request.form.get('set_key')
    slot_key = request.form.get('slot_key')
    rarity = request.form.get('rarity')
    main_stat_key = request.form.get('main_stat_key')
    level = request.form.get('level')

    new_artifact = Artifact(
        setKey=set_key, 
        slotKey=slot_key,
        rarity=rarity,
        mainStatKey=main_stat_key,
        level=level
    )
    db.session.add(new_artifact)
    db.session.commit()
    return redirect(url_for('main.view_artifacts_page'))

@main_bp.route('/add_artifact_json', methods=['POST'])
def add_artifact_json():
    if 'json_file' in request.files and request.files['json_file'].filename:
        json_file = request.files['json_file']
        data = json.load(json_file)
    else:
        data = json.loads(request.form['json_data'])
    
    # print(f"Received Data: {data} : {type(data)}")
    for artifact in data.get('artifacts'):
        # print(f"\n{artifact} : {type(artifact)}")
        setKey = artifact.get('setKey')
        slotKey = artifact.get('slotKey')
        rarity = artifact.get('rarity')
        mainStatKey = artifact.get('mainStatKey')
        level = artifact.get('level')

        substats = artifact.get('substats', [])
        subStatKeys = []
        subStatValues = []
        for i in range(4):
            substat = substats[i] if i < len(substats) else None 
            subStatKeys.append(substat.get('key') if substat else None)
            subStatValues.append(substat.get('value') if substat else None)
        
        new_artifact = Artifact(
            setKey=setKey, 
            slotKey=slotKey,
            rarity=rarity,
            mainStatKey=mainStatKey,
            level=level,
            subStatKey1 = subStatKeys[0],
            subStatKey2 = subStatKeys[1],
            subStatKey3 = subStatKeys[2],
            subStatKey4 = subStatKeys[3],
            subStatValue1 = subStatValues[0],
            subStatValue2 = subStatValues[1],
            subStatValue3 = subStatValues[2],
            subStatValue4 = subStatValues[3]
        )
        db.session.add(new_artifact)
    db.session.commit()
    return redirect(url_for('main.view_artifacts_page'))

@main_bp.route('/delete_artifact/<int:artifact_id>', methods=['POST'])
def delete_artifact(artifact_id):
    artifact_to_delete = Artifact.query.get(artifact_id)
    db.session.delete(artifact_to_delete)
    db.session.commit()
    return redirect(url_for('main.view_artifacts_page'))
