import openai
import os
from flask import jsonify

class AIAssistant:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_response(self, messages, is_chat=False):
        try:
            if is_chat:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    max_tokens=150,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()
            else:
                # For single-turn queries
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant for employees and managers."},
                        {"role": "user", "content": messages}
                    ],
                    max_tokens=150,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Sorry, I couldn't get a response from the AI. ({str(e)})"

def ai_assistant_response(query):
    assistant = AIAssistant()
    response = assistant.get_response(query)
    return jsonify({"response": response})