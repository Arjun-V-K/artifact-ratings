from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Artifact, Substat, db

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

        new_artifact = Artifact(
            set_key = artifact.get('setKey'),
            slot_key = artifact.get('slotKey'),
            level = artifact.get('level'),
            rarity = artifact.get('rarity'),
            main_stat_key = artifact.get('mainStatKey'),
            location = artifact.get('location'),
            lock = artifact.get('lock')
        )

        substats_data = artifact.get('substats', [])
        substats_list = []
        for substat in substats_data:
            new_substat = Substat(
                key = substat.get('key'),
                value = substat.get('value')
            )
            substats_list.append(new_substat)
        
        new_artifact.substats = substats_list
        db.session.add(new_artifact)
        
    db.session.commit()
    return redirect(url_for('main.view_artifacts_page'))

@main_bp.route('/delete_artifact/<int:artifact_id>', methods=['POST'])
def delete_artifact(artifact_id):
    artifact_to_delete = Artifact.query.get(artifact_id)
    db.session.delete(artifact_to_delete)
    db.session.commit()
    return redirect(url_for('main.view_artifacts_page'))
