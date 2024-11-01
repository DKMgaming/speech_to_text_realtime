import streamlit as st
import numpy as np
import soundfile as sf
import io

st.title("Ghi âm và Chuyển đổi âm thanh thành văn bản")

# Thêm JavaScript để ghi âm
st.markdown("""
    <script>
    var recorder, audioStream;
    async function startRecording() {
        audioStream = await navigator.mediaDevices.getUserMedia({audio: true});
        recorder = new MediaRecorder(audioStream);
        recorder.ondataavailable = function(e) {
            const blob = new Blob([e.data], { type: 'audio/wav' });
            const url = URL.createObjectURL(blob);
            document.getElementById('audio-preview').src = url; // Hiển thị âm thanh đã ghi
            document.getElementById('audio-file').value = url; // Lưu URL vào input
        }
        recorder.start();
        document.getElementById('status').innerText = "Ghi âm đang diễn ra...";
    }

    function stopRecording() {
        recorder.stop();
        audioStream.getTracks().forEach(track => track.stop());
        document.getElementById('status').innerText = "Ghi âm đã dừng lại.";
    }
    </script>
    <button onclick="startRecording()">Bắt đầu ghi âm</button>
    <button onclick="stopRecording()">Dừng ghi âm</button>
    <p id="status"></p>
    <audio id="audio-preview" controls></audio>
    <input type="hidden" id="audio-file" value="" />
""", unsafe_allow_html=True)

# Upload audio file
if st.button("Gửi âm thanh"):
    audio_url = st.text_input("URL âm thanh:", key="audio-url", value="")
    if audio_url:
        # Chuyển đổi URL thành file âm thanh
        audio_file = requests.get(audio_url).content
        # Lưu âm thanh vào một buffer
        buffer = io.BytesIO(audio_file)
        
        # Chuyển đổi âm thanh thành văn bản (giả định bạn đã cài đặt SpeechRecognition)
        # Đoạn mã dưới đây cần được cập nhật với chức năng chuyển đổi âm thanh
        # text = convert_audio_to_text(buffer)
        
        st.audio(buffer)
        # st.write("Văn bản chuyển đổi: ", text)  # Hiển thị văn bản đã chuyển đổi
