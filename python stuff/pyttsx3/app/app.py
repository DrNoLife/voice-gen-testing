from flask import Flask, request, send_file, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Define paths
    output_file = '/app/audio_files/output.wav'
    
    # Voice and its settings
    voice = data.get('voice', None)  # Default is None, meaning let Festival decide
    pitch = data.get('pitch', "100")
    rate = data.get('rate', "1.0")

    # Convert text to speech
    try:
        if voice:
            subprocess.call(f'echo "{text}" | text2wave -eval "(voice_{voice})" -o {output_file}', shell=True)
        else:
            subprocess.call(f'echo "{text}" | text2wave -o {output_file}', shell=True)

        # TODO: Apply pitch and rate adjustments using another tool like `sox` if required.

        # Read WAV bytes and return as response
        with open(output_file, 'rb') as f:
            audio_data = f.read()
        return send_file(output_file, as_attachment=True)
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
