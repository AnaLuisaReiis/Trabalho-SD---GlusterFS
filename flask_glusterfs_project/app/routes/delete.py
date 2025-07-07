
from flask import Blueprint, jsonify
import os

bp = Blueprint('delete', __name__)

@bp.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    path = os.path.join('/mnt/glusterfs', filename)
    if os.path.exists(path):
        os.remove(path)
        return jsonify({'message': 'Arquivo deletado'})
    return jsonify({'error': 'Arquivo não encontrado'}), 404
