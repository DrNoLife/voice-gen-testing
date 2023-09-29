from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # for example, 16 MB

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.form.get('text', '')
    if not text:
        return {'error': 'No text provided'}, 400

    tts = gTTS(text, lang='en')
    mp3_filename = 'speech.mp3'
    tts.save(mp3_filename)

    return send_file(mp3_filename, mimetype='audio/mp3')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

