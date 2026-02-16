from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h2>Welcome!</h2>
    <p>Send a POST request to /sentiment with JSON: {"text": "your text here"}</p>
    """

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Please provide 'text' in JSON body"}), 400
    
    text = data['text']
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # ranges from -1 (negative) to 1 (positive)

    return jsonify({
        "text": text,
        "sentiment_score": sentiment_score,
        "sentiment": "positive" if sentiment_score > 0 else "negative" if sentiment_score < 0 else "neutral"
    })

if __name__ == "__main__":

    app.run(debug=True)  # Runs on http://127.0.0.1:5001





