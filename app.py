import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Securely use API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content": question}]
        )
        answer = response.choices[0].message["content"]
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
