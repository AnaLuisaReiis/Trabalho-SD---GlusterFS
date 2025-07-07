import os
from app.config import UPLOAD_PATH

def save_file(file):
    path = os.path.join(UPLOAD_PATH, file.filename)
    file.save(path)
    return {'message': 'Arquivo salvo com sucesso'}

def list_files():
    try:
        return os.listdir(UPLOAD_PATH)
    except FileNotFoundError:
        return []

def delete_file(filename):
    path = os.path.join(UPLOAD_PATH, filename)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
