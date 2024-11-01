import streamlit as st
import os
import requests

st.title("Ghi âm và Chuyển đổi âm thanh thành văn bản")

# Thêm JavaScript để ghi âm
st.markdown("""
    <script>
    var recorder, audioStream;
    async function startRecording() {
        audioStream = await navigator.mediaDevices.getUserMedia({audio: true});
        recorder = new MediaRecorder(audioStream);
        recorder.ondataavailable = async function(e) {
            const blob = new Blob([e.data], { type: 'audio/wav' });
            const url = URL.createObjectURL(blob);
            const response = await fetch(url);
            const audioData = await response.blob();
            const file = new File([audioData], 'audio.wav', {type: 'audio/wav'});
            const formData = new FormData();
            formData.append('file', file);
            const res = await fetch('/upload', {
                method: 'POST',
                body: formData
            });
            console.log(await res.text());
        }
        recorder.start();
        st.write("Ghi âm đang diễn ra...");
    }

    function stopRecording() {
        recorder.stop();
        audioStream.getTracks().forEach(track => track.stop());
        st.write("Ghi âm đã dừng lại.");
    }
    </script>
    <button onclick="startRecording()">Bắt đầu ghi âm</button>
    <button onclick="stopRecording()">Dừng ghi âm</button>
""", unsafe_allow_html=True)

# Xử lý file được ghi âm
upload_url = st.server.url + '/upload'
if st.button("Gửi âm thanh"):
    audio_file = requests.get(upload_url)
    st.audio(audio_file)
