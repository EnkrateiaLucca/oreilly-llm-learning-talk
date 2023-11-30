import streamlit as st
import numpy as np
import scipy.io.wavfile as wav
from pydub import AudioSegment
import io

# Function to process and display the waveform
def process_and_plot_audio(file, volume_factor=1.0, start_trim=0, end_trim=0):
    # Load audio
    audio = AudioSegment.from_file(file)
    
    # Modify audio
    modified_audio = audio[start_trim:end_trim] if end_trim > 0 else audio[start_trim:]
    modified_audio = modified_audio + volume_factor

    # Convert to WAV for processing
    buf = io.BytesIO()
    modified_audio.export(buf, format='wav')
    buf.seek(0)
    sample_rate, data = wav.read(buf)

    # Plot waveform
    st.write("Modified Waveform")
    st.line_chart(data)

    return modified_audio

# Streamlit app
def main():
    st.title("Interactive Audio Editor")

    uploaded_file = st.file_uploader("Upload an Audio File", type=['mp3', 'wav'])

    if uploaded_file is not None:
        # Audio editing options
        volume_factor = st.slider("Volume Adjustment", -20, 20, 0)
        start_trim = st.slider("Start Trim (ms)", 0, 10000, 0)
        end_trim = st.slider("End Trim (ms)", 0, 10000, 0)

        # Process and display audio
        modified_audio = process_and_plot_audio(uploaded_file, volume_factor, start_trim, end_trim)

        # Audio playback
        st.audio(modified_audio.export(format='mp3'), format='audio/mp3')

        # Save/export option
        if st.button('Download Modified Audio'):
            st.download_button('Download', modified_audio.export(format='mp3'), file_name='modified_audio.mp3')

if __name__ == "__main__":
    main()
