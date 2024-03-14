from app import create_app, db
from socket import gethostname
app = create_app()

if __name__ == '__main__':
    # Create the tables
    with app.app_context():
        db.create_all()
    if 'liveconsole' not in gethostname():
        app.run(debug=True)
