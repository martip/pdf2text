from flask import Flask, request, jsonify
from pypdf import PdfReader
import os

app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Extract optional parameters from the request body
    extraction_mode = request.form.get("mode", "layout")  # Default to "layout"
    layout_mode_space_vertically = request.form.get("space_vertically", "false").lower() == "true"  # Default to false
    layout_mode_scale_weight = float(request.form.get("scale_weight", 1.25))  # Default to 1.25

    try:
        # Save the uploaded file temporarily
        temp_path = os.path.join("/tmp", file.filename)
        file.save(temp_path)

        # Use PyPDF to extract text with the specified options
        reader = PdfReader(temp_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text(
                extraction_mode=extraction_mode,
                layout_mode_space_vertically=layout_mode_space_vertically,
                layout_mode_scale_weight=layout_mode_scale_weight
            )

        # Remove the temporary file
        os.remove(temp_path)

        return jsonify({"extracted_text": text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7357)
