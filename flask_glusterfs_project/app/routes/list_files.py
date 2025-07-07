
from flask import Blueprint, jsonify,render_template
import os

bp = Blueprint('list_files', __name__)
@bp.route('/list_files', methods=['GET'])
def upload_form():
    return render_template('list_files.html')

@bp.route('/files', methods=['GET'])
def listar_arquivos():
    files = os.listdir('/mnt/glusterfs')
    return render_template('list_files.html', arquivos=files)


