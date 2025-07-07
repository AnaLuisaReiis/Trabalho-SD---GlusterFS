
from flask import Blueprint, send_file, request, jsonify
# from app.utils.jwt_utils import token_required
import os

bp = Blueprint('download', __name__)

@bp.route('/download/<filename>', methods=['GET'])
# @token_required
def download(filename):
    path = os.path.join('/mnt/glusterfs', filename)
    if os.path.exists(path):
        return send_file(path)
    return jsonify({'error': 'Arquivo não encontrado'}), 404
