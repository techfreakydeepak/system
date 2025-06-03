import json
import os
import datetime
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models.user import users, get_user_by_username
from chat.ai_assistant import AIAssistant

employee_chat = Blueprint('employee_chat', __name__)

CHAT_DIR = "chat_histories"
os.makedirs(CHAT_DIR, exist_ok=True)

def get_chat_file(employee_id):
    return os.path.join(CHAT_DIR, f"employee_{employee_id}.json")

def load_chat_history(employee_id):
    chat_file = get_chat_file(employee_id)
    if os.path.exists(chat_file):
        with open(chat_file, "r") as f:
            return json.load(f)
    return []

def save_chat_history(employee_id, history):
    chat_file = get_chat_file(employee_id)
    with open(chat_file, "w") as f:
        json.dump(history, f)

@employee_chat.route('/chat/employee/send_to_manager', methods=['POST'])
def send_to_manager():
    employee_id = request.form.get('employee_id')
    message = request.form.get('message')
    history = load_chat_history(employee_id)
    history.append({
        "from": "employee",
        "message": message,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_chat_history(employee_id, history)
    return redirect(url_for('employee_chat.employee_home', employee_id=employee_id))

@employee_chat.route('/chat/employee/ai_assistant', methods=['POST'])
def ai_assistant():
    employee_id = request.form.get('employee_id')
    employee_query = request.form.get('query')

    ai_assistant = AIAssistant()
    ai_response = ai_assistant.get_response(employee_query)

    history = load_chat_history(employee_id)
    history.append({
        "from": "employee",
        "message": employee_query,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    history.append({
        "from": "ai_assistant",
        "message": ai_response,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_chat_history(employee_id, history)

    return redirect(url_for('employee_chat.employee_home', employee_id=employee_id))

@employee_chat.route('/employee/<int:employee_id>/home')
def employee_home(employee_id):
    history = load_chat_history(employee_id)
    return render_template('employee_home.html', employee_id=employee_id, chat_history=history)