from flask import Flask, render_template, request, jsonify, send_file
import qrcode
import os

app = Flask(__name__)

# path for saving QR codes
QR_CODE_PATH = os.path.join('static', 'qr_codes')
if not os.path.exists(QR_CODE_PATH):
    os.makedirs(QR_CODE_PATH)

def generate_qr(data, size, fg_color, bg_color, file_format):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill=fg_color, back_color=bg_color)

    file_name = f"qr_code.{file_format}"
    file_path = os.path.join(QR_CODE_PATH, file_name)
    
    if file_format == "png":
        img.save(file_path)
    elif file_format == "svg":
        qr.make_image(fill=fg_color, back_color=bg_color).convert("RGB").save(file_path, format="SVG")

    return file_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json.get('data', '')
    size = int(request.json.get('size', 10))
    fg_color = request.json.get('fg_color', 'black')
    bg_color = request.json.get('bg_color', 'white')
    file_format = request.json.get('format', 'png')

    if not data:
        return jsonify({"error": "No data provided"}), 400

    file_name = generate_qr(data, size, fg_color, bg_color, file_format)
    return jsonify({"qr_code_url": f"/static/qr_codes/{file_name}"})

@app.route('/download')
def download():
    file_format = request.args.get('format', 'png')
    file_path = os.path.join(QR_CODE_PATH, f"qr_code.{file_format}")
    
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
