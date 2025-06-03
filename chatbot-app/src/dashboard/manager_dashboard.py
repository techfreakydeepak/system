from flask import Blueprint, render_template, request, redirect, url_for
from models.user import users
import os, json, datetime

manager_dashboard = Blueprint('manager_dashboard', __name__)

def get_all_employees():
    return [u for u in users if u["role"] == "employee"]

def get_chat_history(employee_id):
    chat_file = os.path.join("chat_histories", f"employee_{employee_id}.json")
    if os.path.exists(chat_file):
        with open(chat_file, "r") as f:
            return json.load(f)
    return []

def get_manager_ai_chat_file(manager_id):
    return os.path.join("chat_histories", f"manager_ai_{manager_id}.json")

def load_manager_ai_history(manager_id):
    chat_file = get_manager_ai_chat_file(manager_id)
    if os.path.exists(chat_file):
        with open(chat_file, "r") as f:
            return json.load(f)
    return []

def save_manager_ai_history(manager_id, history):
    chat_file = get_manager_ai_chat_file(manager_id)
    with open(chat_file, "w") as f:
        json.dump(history, f)

@manager_dashboard.route('/dashboard')
def dashboard():
    employees = get_all_employees()
    employee_status = []
    recent_chats = []
    for emp in employees:
        history = get_chat_history(emp["id"])
        filtered = [msg for msg in history if msg["from"] in ("manager", "employee")]
        last_message = filtered[-1]["message"] if filtered else "No messages yet"
        last_time = filtered[-1].get("timestamp", "") if filtered and "timestamp" in filtered[-1] else ""
        employee_status.append({
            "id": emp["id"],
            "name": emp["username"],
            "status": "Active",
            "last_activity": last_time or last_message
        })
        recent_chats.append({
            "employee_id": emp["id"],
            "employee_name": emp["username"],
            "message": last_message,
            "timestamp": last_time
        })
    return render_template(
        'dashboard.html',
        employees=employee_status,
        recent_chats=recent_chats
    )

@manager_dashboard.route('/employee/<int:employee_id>/chat', methods=['GET', 'POST'])
def employee_chat(employee_id):
    chat_file = os.path.join("chat_histories", f"employee_{employee_id}.json")
    employee = next((u for u in users if u["id"] == employee_id), None)
    employee_name = employee["username"] if employee else f"Employee {employee_id}"
    ai_response = None

    # For demo, assume manager_id is always 1
    manager_id = 1

    if request.method == 'POST':
        if 'message' in request.form:
            message = request.form.get('message')
            history = get_chat_history(employee_id)
            history.append({
                "from": "manager",
                "message": message,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            with open(chat_file, "w") as f:
                json.dump(history, f)
            return redirect(url_for('manager_dashboard.employee_chat', employee_id=employee_id))
        elif 'ai_query' in request.form:
            ai_query = request.form.get('ai_query')
            from chat.ai_assistant import AIAssistant
            ai_assistant = AIAssistant()
            # Load full manager-AI history and build OpenAI messages
            ai_history = load_manager_ai_history(manager_id)
            messages = []
            if not ai_history:
                messages.append({"role": "system", "content": "You are a helpful assistant for managers."})
            for msg in ai_history:
                if msg["from"] == "manager":
                    messages.append({"role": "user", "content": msg["message"]})
                elif msg["from"] == "ai_assistant":
                    messages.append({"role": "assistant", "content": msg["message"]})
            # Add the new manager question
            messages.append({"role": "user", "content": ai_query})
            ai_response = ai_assistant.get_response(messages, is_chat=True)
            # Save both question and answer to history
            ai_history.append({
                "from": "manager",
                "message": ai_query,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            ai_history.append({
                "from": "ai_assistant",
                "message": ai_response,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            save_manager_ai_history(manager_id, ai_history)

    # Only show manager/employee messages
    full_history = get_chat_history(employee_id)
    filtered_history = [msg for msg in full_history if msg["from"] in ("manager", "employee")]
    # Load manager-AI chat history
    manager_ai_history = load_manager_ai_history(manager_id)
    return render_template(
        'chat.html',
        chat_history=filtered_history,
        employee_id=employee_id,
        employee_name=employee_name,
        ai_response=ai_response,
        manager_ai_history=manager_ai_history
    )