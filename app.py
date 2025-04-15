from flask import Flask, request, jsonify, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a new chatbot
chatbot = ChatBot('My Chatbot')

# Create a new trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot
trainer.train('chatterbot.corpus.english')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = chatbot.get_response(user_input)
    return jsonify({'response': str(response)})

if __name__ == '__main__':
    app.run(debug=True)
