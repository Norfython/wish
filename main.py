import streamlit as st
import time
import random

st.set_page_config(page_title="Code thâu đêm", page_icon="🌙", layout="centered")

cute_colors = ['#DDA0DD', '#FFB6C1', '#B0E0E6', '#E6E6FA', '#F08080', '#87CEFA']

st.markdown("""
    <style>
        body {
            background-color: #fff0f5;
        }
        .title-text {
            font-size: 36px;
            color: #ff69b4;
            font-family: "Comic Sans MS", cursive, sans-serif;
            text-align: center;
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
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">🌙 Thâu đêm để code 🌙</div>', unsafe_allow_html=True)
st.write("")

messages = ["Nói chớ..", "Ngủ sớm đi mẹeee", "Chúc ngủ ngon :3"]

for i, msg in enumerate(messages):
    time.sleep(1)

    color = cute_colors[i % len(cute_colors) + 1] 

    st.markdown(
        f"""
        <div style="
            font-size:32px;
            color:{color};
            font-family:'Comic Sans MS', cursive, sans-serif;
            text-align:center;
            animation: fadeIn 2s ease-in-out;">
            {msg}
        </div>
        """,
        unsafe_allow_html=True
    )

# Hiển thị hình ảnh
time.sleep(1)
st.image("cat-sleep.gif")
