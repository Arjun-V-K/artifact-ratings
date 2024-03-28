from app import create_app, db
from socket import gethostname

app = create_app()

if __name__ == '__main__':
    # Run this from terminal to initialize the database
    with app.app_context():
        db.create_all()
    # Run the app in debug mode, when not hosted in pythonanywhere
    if 'liveconsole' not in gethostname():
        app.run(debug=True)
