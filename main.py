import streamlit as st
import time

# Thiết lập trang
st.set_page_config(page_title="Code thâu đêm", page_icon="🌙", layout="centered")

# CSS dễ thương
st.markdown("""
    <style>
        body {
            background-color: #fff0f5;
        }
        .cute-text {
            font-size: 32px;
            color: #ff69b4;
            font-family: "Comic Sans MS", cursive, sans-serif;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(255, 105, 180, 0.5);
            max-width: 300px;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề
st.markdown('<div class="cute-text">🌙 Good Night 🌙</div>', unsafe_allow_html=True)
st.write("")

# Danh sách các câu sẽ hiện ra lần lượt
messages = ["Nói chứ..", "Ngủ sớm đi mẹeee", "Chúc ngủ ngon :3"]

# Hiển thị từng dòng sau mỗi 2 giây
for msg in messages:
    time.sleep(2)
    st.markdown(f'<div class="cute-text">{msg}</div>', unsafe_allow_html=True)

# Hiển thị hình ảnh dễ thương sau cùng
time.sleep(1)
st.markdown("""
    <div class="image-container">
        <img src="https://i.pinimg.com/originals/3c/0c/34/3c0c340509ab0c7ef1c799e0a388e645.gif" alt="Cute cat saying good night">
    </div>
""", unsafe_allow_html=True)
