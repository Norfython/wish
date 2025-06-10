import streamlit as st
import time
import random

# Thiết lập trang
st.set_page_config(page_title="Chúc ngủ ngon mẹ", page_icon="🌙", layout="centered")

# Màu sắc dễ thương cho từng dòng
cute_colors = ['#ff69b4', '#9370DB', '#00BFFF', '#FF6347', '#32CD32', '#FFD700']

# CSS cho body và tiêu đề
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

# Tiêu đề
st.markdown('<div class="title-text">🌙 Thâu đêm để code 🌙</div>', unsafe_allow_html=True)
st.write("")

# Danh sách các câu sẽ hiện ra lần lượt
messages = ["Nói chớ..", "Ngủ sớm đi mẹeee", "Chúc ngủ ngon :3"]

# Hiển thị từng dòng với màu riêng
for i, msg in enumerate(messages):
    time.sleep(1)

    color = cute_colors[i % len(cute_colors)]  # Dùng màu theo thứ tự
    # Hoặc nếu muốn ngẫu nhiên:
    # color = random.choice(cute_colors)

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
st.markdown("""
    <div class="image-container">
        <img src="cat-sleep.gif" alt="Cute cat saying good night">
    </div>
""", unsafe_allow_html=True)
