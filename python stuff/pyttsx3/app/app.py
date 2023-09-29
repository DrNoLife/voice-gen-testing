from flask import Flask, request, send_file, jsonify
import pyttsx3
import os
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
   
app = Flask(__name__)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    try:
        text = request.form.get('text', '')
        if not text:
            return {'error': 'No text provided'}, 400
        #text = request.json.get('text', '')
        filename = '/output.mp3'
        engine = pyttsx3.init()
        engine.save_to_file(text, filename)
        engine.runAndWait()
        
        return send_file(filename, as_attachment=True)
    except:
        error_msg = "Completely failed.\nReceived following payload:\n\n"
        if request.json:
            error_msg += request.json.get('text', '')
        else:
            error_msg += "No JSON data or 'text' key found in the payload."

        app.logger.critical(error_msg)

@app.route('/text-to-speech-get', methods=['GET'])
def text_to_speech_get():
    try:
        text = request.args.get('text', '')  # Access 'text' from query parameters
        if not text:
            return {'error': 'No text provided'}, 400
        filename = '/output.mp3'
        engine = pyttsx3.init()
        engine.save_to_file(text, filename)
        engine.runAndWait()
        
        return send_file(filename, as_attachment=True)
    except Exception as e:  # Catch and log exceptions
        error_msg = f"Completely failed.\nReceived following payload:\n\n{request.args.get('text', '')}"
        app.logger.critical(error_msg)
        
        # Include error details in the response
        error_details = {
            'error': 'An error occurred',
            'error_message': str(e)  # Convert the exception to a string
        }
        return jsonify(error_details), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
