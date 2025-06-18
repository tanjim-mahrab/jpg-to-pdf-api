from flask import Flask, request, send_file
from PIL import Image
import os
import uuid

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_jpg_to_pdf():
    if 'image' not in request.files:
        return {"error": "No image file found"}, 400

    image_file = request.files['image']
    if image_file.filename == '':
        return {"error": "Empty file"}, 400

    filename = f"{uuid.uuid4()}.pdf"
    image = Image.open(image_file.stream).convert("RGB")
    output_path = os.path.join("output", filename)
    os.makedirs("output", exist_ok=True)
    image.save(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

