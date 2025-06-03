# Chatbot Application

This project is a chatbot application designed for managing employee and manager interactions. It allows managers to inquire about employee work statuses, while employees can communicate with their managers and an AI assistant for support.

## Features

- **User Authentication**: Users can sign up and log in using their mobile numbers, with OTP verification for security.
- **Chat Functionality**: 
  - Managers can view all employee chats and send messages.
  - Employees can respond to manager queries and interact with an AI assistant for help.
- **Dashboard**: Managers have access to a dashboard that displays the status of their employees and chat summaries.
- **AI Assistant**: Provides automated responses to common employee queries.

## Project Structure

```
chatbot-app
├── src
│   ├── app.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── otp.py
│   │   └── users.py
│   ├── chat
│   │   ├── __init__.py
│   │   ├── manager.py
│   │   ├── employee.py
│   │   └── ai_assistant.py
│   ├── dashboard
│   │   ├── __init__.py
│   │   └── manager_dashboard.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── sms.py
│   └── templates
│       ├── base.html
│       ├── login.html
│       ├── signup.html
│       ├── chat.html
│       └── dashboard.html
├── requirements.txt
├── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

## Usage

- Navigate to `http://localhost:5000` in your web browser.
- Sign up using your mobile number and verify with the OTP sent to your phone.
- Managers can log in to view their dashboard and employee chats.
- Employees can log in to respond to manager queries and access the AI assistant.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.