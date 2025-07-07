from flask import Flask
from app.routes import main, upload, download, list_files, delete

def create_app():
    app = Flask(__name__)
    app.secret_key = 'h7g@8h!12fa6$G#9Zx!@94KDg'  

    app.register_blueprint(main.bp)
    app.register_blueprint(upload.bp)
    app.register_blueprint(download.bp)
    app.register_blueprint(list_files.bp)
    app.register_blueprint(delete.bp)

    return app
