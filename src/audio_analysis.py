import librosa
import numpy as np

def load_audio(file_path):
    y, sr = librosa.load(file_path)
    return y, sr

def get_beats(y, sr):
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    return tempo, beat_times

def get_frequency_spectrum(y, sr):
    stft = np.abs(librosa.stft(y))
    spectrogram = librosa.amplitude_to_db(stft, ref=np.max)
    return spectrogram
