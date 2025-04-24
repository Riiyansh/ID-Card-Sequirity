
from flask import Flask, render_template, request
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    if 'image1' not in request.files or 'image2' not in request.files:
        return render_template('index.html', result="Please upload both images.")

    img1 = request.files['image1']
    img2 = request.files['image2']

    if img1.filename == '' or img2.filename == '':
        return render_template('index.html', result="One or both files are empty.")

    image1_data = img1.read()
    image2_data = img2.read()

    # Convert to base64 for preview
    image1_base64 = base64.b64encode(image1_data).decode('utf-8')
    image2_base64 = base64.b64encode(image2_data).decode('utf-8')

    # Decode for OpenCV processing
    image1 = cv2.imdecode(np.frombuffer(image1_data, np.uint8), cv2.IMREAD_COLOR)
    image2 = cv2.imdecode(np.frombuffer(image2_data, np.uint8), cv2.IMREAD_COLOR)

    if image1.shape != image2.shape:
        return render_template('index.html', result="Tampering Detected: Images have different dimensions.",
                               img1=image1_base64, img2=image2_base64)

    # Image difference logic
    difference = cv2.absdiff(image1, image2)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    non_zero_count = cv2.countNonZero(thresh)
    total_pixels = gray.size
    similarity_percent = 100 - ((non_zero_count / total_pixels) * 100)

    if non_zero_count > 1000:
        result = "Tampering Detected"
    else:
        result = "No Tampering Detected"

    return render_template('index.html',
                           result=result,
                           similarity=f"{similarity_percent:.2f}%", 
                           img1=image1_base64,
                           img2=image2_base64)

if __name__ == '__main__':
    app.run(debug=True)
