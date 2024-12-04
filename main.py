from src.audio_analysis import load_audio, get_beats, get_frequency_spectrum
from src.visualizer import plot_spectrogram

def main():
    audio_file = "data/audio/sample.mp3"
    
    # Step 1: Load audio
    y, sr = load_audio(audio_file)
    
    # Step 2: Analyze audio
    tempo, beat_times = get_beats(y, sr)
    spectrogram = get_frequency_spectrum(y, sr)
    
    # Step 3: Visualize
    print(f"Detected tempo: {tempo} BPM")
    plot_spectrogram(spectrogram, sr, hop_length=512)

if __name__ == "__main__":
    main()
