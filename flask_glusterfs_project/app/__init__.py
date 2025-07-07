
from flask import Flask
from app.routes import upload, download, list_files, delete

def create_app():
    app = Flask(__name__)
    app.register_blueprint(upload.bp)
    app.register_blueprint(download.bp)
    app.register_blueprint(list_files.bp)
    app.register_blueprint(delete.bp)
    return app
