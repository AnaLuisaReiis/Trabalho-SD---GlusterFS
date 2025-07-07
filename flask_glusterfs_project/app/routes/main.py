from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.file_service import save_file, list_files, delete_file
# from app.utils.jwt_utils import token_required

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    files = list_files()
    return render_template('index.html', files=files)

@bp.route('/upload', methods=['POST'])
# @token_required
def upload():
    file = request.files.get('file')
    if file:
        save_file(file)
        flash('Arquivo enviado com sucesso!')
    else:
        flash('Nenhum arquivo selecionado.')
    return redirect(url_for('main.index'))

@bp.route('/delete/<filename>', methods=['POST'])
# @token_required
def delete(filename):
    delete_file(filename)
    flash('Arquivo deletado.')
    return redirect(url_for('main.index'))
