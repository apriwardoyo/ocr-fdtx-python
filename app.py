from flask import Flask, request, jsonify, send_from_directory
import pytesseract
from PIL import Image

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")


@app.route("/ocr", methods=["POST"])
def ocr():
    if "file" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    img_file = request.files["file"]

    try:
        img = Image.open(img_file.stream)
        text = pytesseract.image_to_string(img, lang="eng+ind")
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
