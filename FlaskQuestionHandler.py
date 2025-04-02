from flask import Flask, request, jsonify
from flask_cors import CORS
from OpenAIJsonQueryHandler import ask_txt
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    answer = ask_txt(question)

    return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
