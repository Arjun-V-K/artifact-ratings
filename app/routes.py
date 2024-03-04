from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Artifact, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    artifacts = Artifact.query.all()
    return render_template('index.html', artifacts=artifacts)

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
    return redirect(url_for('main.index'))

@main_bp.route('/delete_artifact/<int:artifact_id>', methods=['POST'])
def delete_artifact(artifact_id):
    artifact_to_delete = Artifact.query.get(artifact_id)
    db.session.delete(artifact_to_delete)
    db.session.commit()
    return redirect(url_for('main.index'))
