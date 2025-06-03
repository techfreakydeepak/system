from flask import Flask, render_template, request, redirect, url_for, jsonify
from auth.users import login_user, register_user
from chat.manager import manager_chat_bp
from chat.employee import employee_chat
from dashboard.manager_dashboard import manager_dashboard
from chat.ai_assistant import ai_assistant_response

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(manager_chat_bp)
app.register_blueprint(employee_chat)
app.register_blueprint(manager_dashboard)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login_user(username, password)
        if user:
            if user["role"] == "manager":
                return redirect(url_for('manager_dashboard.dashboard'))
            elif user["role"] == "employee":
                return redirect(url_for('employee_chat.employee_home', employee_id=user["id"]))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        mobile_number = request.form['mobile_number']
        if register_user(mobile_number):
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    # Add session clearing logic here if you use sessions
    return redirect(url_for('login'))

@app.route('/ai-assistant', methods=['POST'])
def ai_assistant():
    data = request.json
    query = data.get('query', '')
    return ai_assistant_response(query)

if __name__ == '__main__':
    app.run(debug=True)