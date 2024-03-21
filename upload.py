## upload.py
from flask import jsonify, request
from flask_restful import Resource
from flask_login import login_required
from textanalyzer import analyze_document

class FileUpload(Resource):
    @login_required
    def post(self):
        if 'document' not in request.files:
            return jsonify({"error": "No file part"})
        file = request.files['document']
        if file.filename == '':
            return jsonify({"error": "No selected file"})
        if file:
            text = file.read().decode("utf-8")
            analysis_result = analyze_document(text)
            return jsonify(analysis_result)
