from flask import Flask, request, Response
import subprocess
import os

app = Flask(__name__)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.json.get('text', '')
    voice = request.json.get('voice', 'en-us')
    speed = request.json.get('speed', 150)
    pitch = request.json.get('pitch', 50)

    if not text:
        return {'error': 'No text provided'}, 400

    # Ensure the directory exists
    if not os.path.exists("/app/audio_files"):
        os.makedirs("/app/audio_files")

    # Generate WAV file using espeak with MBROLA voice
    wav_file = "/app/audio_files/output.wav"
    subprocess.call(["espeak", "-w", wav_file, "-v", voice, "-s", str(speed), "-p", str(pitch), text])

    if not os.path.exists(wav_file):
        return {"error": "WAV file was not generated. Check espeak logs for more details."}, 500

    # Convert WAV to MP3 using ffmpeg
    mp3_file = "/app/audio_files/output.mp3"
    process = subprocess.Popen(["ffmpeg", "-i", wav_file, mp3_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Log ffmpeg output for debugging
    print("FFMPEG STDOUT:", stdout.decode())
    print("FFMPEG STDERR:", stderr.decode())

    # Check if the MP3 file exists before attempting to open it
    if os.path.exists(mp3_file):
        with open(mp3_file, 'rb') as f:
            mp3_data = f.read()

        # Optionally, remove temporary files
        os.remove(wav_file)
        os.remove(mp3_file)

        return Response(mp3_data, content_type='audio/mpeg')

    else:
        return {"error": "MP3 file was not generated. Check ffmpeg logs for more details."}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
