import streamlit as st
import sounddevice as sd
import numpy as np
import wave
import speech_recognition as sr
from docx import Document

st.title("Ghi âm và Chuyển đổi âm thanh thành văn bản")

def record_audio(duration):
    fs = 44100  # Tần số mẫu
    st.write("Đang ghi âm...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Chờ cho đến khi ghi âm xong
    st.write("Ghi âm hoàn tất.")
    return audio

def save_audio_to_wav(audio, filename):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for int16
        wf.setframerate(44100)
        wf.writeframes(audio)

def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language='vi-VN')
    except sr.UnknownValueError:
        text = "Không thể nhận diện được giọng nói"
    except sr.RequestError:
        text = "Lỗi khi yêu cầu dịch vụ nhận diện giọng nói"
    return text

duration = st.number_input("Thời gian ghi âm (giây)", min_value=1, max_value=60, value=5)
if st.button("Bắt đầu ghi âm"):
    audio = record_audio(duration)
    audio_filename = "recorded_audio.wav"
    save_audio_to_wav(audio, audio_filename)

    text = convert_audio_to_text(audio_filename)
    st.write("Kết quả:", text)

    # Tạo file Word
    doc = Document()
    doc.add_heading('Transcript', level=1)
    doc.add_paragraph(text)
    doc.save("transcript.docx")
    st.download_button("Tải về transcript", "transcript.docx")
