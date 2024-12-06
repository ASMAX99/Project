from flask import Flask, render_template, request, jsonify
from model import analyze_code

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        code = request.json.get("code", "")
        if not code:
            return jsonify({"error": "No code provided"}), 400
        
        feedback = analyze_code(code)
        return jsonify(feedback)

if __name__ == "__main__":
    app.run(debug=True)
