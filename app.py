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
    # Check both files present
    if 'image1' not in request.files or 'image2' not in request.files:
        return render_template('index.html', error="Please upload both images.")

    img1 = request.files['image1']
    img2 = request.files['image2']

    if img1.filename == '' or img2.filename == '':
        return render_template('index.html', error="Both files must be selected.")

    # Read raw bytes
    data1 = img1.read()
    data2 = img2.read()

    # Base64 for display
    original_b64 = base64.b64encode(data1).decode('utf-8')
    suspected_b64 = base64.b64encode(data2).decode('utf-8')

    # Decode for OpenCV comparison
    im1 = cv2.imdecode(np.frombuffer(data1, np.uint8), cv2.IMREAD_COLOR)
    im2 = cv2.imdecode(np.frombuffer(data2, np.uint8), cv2.IMREAD_COLOR)

    # Dimension mismatch?
    if im1.shape != im2.shape:
        return render_template('index.html',
                               original=original_b64,
                               suspected=suspected_b64,
                               result="Tampering Detected: Image dimensions do not match.")

    # Compute difference
    diff = cv2.absdiff(im1, im2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on suspect
    marked = im2.copy()
    cv2.drawContours(marked, contours, -1, (0, 0, 255), 2)
    _, buf = cv2.imencode('.png', marked)
    marked_b64 = base64.b64encode(buf).decode('utf-8')

    # Similarity metric
    non_zero = cv2.countNonZero(thresh)
    similarity = 100 - ((non_zero / gray.size) * 100)
    result = "Tampering Detected ❌" if non_zero > 1000 else "No Tampering Detected ✅"

    return render_template('index.html',
                           original=original_b64,
                           suspected=suspected_b64,
                           marked=marked_b64,
                           result=result,
                           similarity=f"{similarity:.2f}%")

if __name__ == '__main__':
    app.run(debug=True)
