import json
import os
from flask import Blueprint, request, jsonify
from models.user import users, get_user_by_username
from chat.ai_assistant import AIAssistant
manager_chat_bp = Blueprint('manager_chat', __name__)  
class EmployeeChat:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def get_chat_history(self):
        return load_chat_history(self.employee_id)

    def send_message(self, message):
        history = load_chat_history(self.employee_id)
        history.append({"from": "employee", "message": message})
        save_chat_history(self.employee_id, history)
        return True

employee_chat = Blueprint('employee_chat', __name__)

@manager_chat_bp.route('/manager/chat/<employee_id>', methods=['GET', 'POST'])
def chat_with_employee(employee_id):
    if request.method == 'GET':
        employee_chat = EmployeeChat(employee_id)
        messages = employee_chat.get_chat_history()
        return jsonify(messages)

    if request.method == 'POST':
        data = request.json
        message = data.get('message')
        employee_chat = EmployeeChat(employee_id)
        employee_chat.send_message(message)
        return jsonify({"status": "Message sent"})

@manager_chat_bp.route('/manager/chat/ai_assistant', methods=['POST'])
def chat_with_ai_assistant():
    data = request.json
    query = data.get('query')
    ai_assistant = AIAssistant()
    response = ai_assistant.get_response(query)
    return jsonify({"response": response})