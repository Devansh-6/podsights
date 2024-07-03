from flask import Flask, jsonify, send_from_directory
import librosa
import numpy as np
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

# Path to your hardcoded audio file
AUDIO_FILE_PATH = os.path.join(os.path.dirname(__file__), 'stiff-socks-284.mp3')

def process_audio(audio_path):
    print(f"Processing audio file: {audio_path}")  # Debug statement

    # Load only the first 30 seconds of the audio file at a lower sampling rate
    y, sr = librosa.load(audio_path, duration=30, sr=22050)
    
    duration = librosa.get_duration(y=y, sr=sr)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    shape = y.shape

    print(f"Duration: {duration}")  # Debug statement
    print(f"Tempo: {tempo}")  # Debug statement
    print(f"Shape: {shape}")  # Debug statement

    return {
        "duration": duration,
        "tempo": tempo.tolist(),  # Convert numpy array to list
        "shape": shape
    }

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/process', methods=['GET'])
def process_file():
    print(f"Current working directory: {os.getcwd()}")  # Debug statement
    audio_data = process_audio(AUDIO_FILE_PATH)
    return jsonify(audio_data)

if __name__ == '__main__':
    app.run(debug=True)
