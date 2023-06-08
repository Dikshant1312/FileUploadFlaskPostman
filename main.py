from flask import Flask, request

app = Flask(__name__)
@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file is present in the request
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    # Check if the file is of PDF type
    if file.filename.endswith('.pdf'):
        # Save the file to a desired location
        file.save('uploads/' + file.filename)
        return 'File uploaded successfully', 200
    else:
        return 'Invalid file type. Only PDF files are allowed', 400
if __name__ == '__main__':
    app.run(debug=True)
