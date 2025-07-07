
from flask import Blueprint, request, jsonify,render_template
from app.services.file_service import save_file
# from app.utils.jwt_utils import token_required

bp = Blueprint('upload', __name__)
@bp.route('/upload', methods=['GET'])
def upload_form():
    return render_template('upload.html')

@bp.route('/upload', methods=['POST'])
# @token_required
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'Arquivo não enviado'}), 400
    result = save_file(file)
    return jsonify(result)


