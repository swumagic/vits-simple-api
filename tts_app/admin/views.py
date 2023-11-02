from flask import Blueprint, request, render_template
from flask_login import login_required

from tts_app.model_manager import model_manager

admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
def home():
    return render_template('pages/home.html')


@admin.route('/get_models_info', methods=["GET", "POST"])
@login_required
def get_models_info():
    return model_manager.get_models_info()


@admin.route('/load_model', methods=["GET", "POST"])
@login_required
def load_model():
    if request.method == "GET":
        request_data = request.args
    elif request.method == "POST":
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            request_data = request.get_json()
        else:
            request_data = request.form
        print(content_type)
    print(request_data)
    model_path = request_data.get("model_path")
    config_path = request_data.get("config_path")

    return model_manager.load_model(model_path, config_path)


@admin.route('/unload_model', methods=["GET", "POST"])
@login_required
def unload_model():
    if request.method == "GET":
        request_data = request.args
    elif request.method == "POST":
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            request_data = request.get_json()
        else:
            request_data = request.form
    model_type = request_data.get("model_type")
    model_id = request_data.get("model_id")

    return model_manager.unload_model(model_type, model_id)


@admin.route('/get_path', methods=["GET", "POST"])
@login_required
def get_path():
    return model_manager.scan_path()
