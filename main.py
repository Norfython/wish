import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Tải hình ảnh gà và hoa
chicken_url = "chick.jpg"
flower_url = "bouquet.jpg"

chicken_img = Image.open(chicken_url)
flower_img = Image.open(flower_url)

# Cấu hình giao diện
st.set_page_config(page_title="Chúc mừng 8/3", page_icon="🌸")

# Tiêu đề
st.title("💖 Chúc Mừng Quốc Tế Phụ Nữ 💖")

# Hiển thị hình ảnh
col1, col2 = st.columns(2)
with col1:
    st.image(chicken_img, caption="Một bé gà dễ thương dành tặng chị! 🐥", use_container_width=True)
with col2:
    st.image(flower_img, caption="Và một bó hoa xinh đẹp! 🌸", use_container_width=True)

# Lời chúc
st.write(
    "### 💌 Gửi đến hai thân yêu 💌"
)
st.write(
    "Nhân ngày 8/3, em chúc chị thật vui vẻ, hạnh phúc và luôn rạng rỡ như những bông hoa 💐"
)

st.write(
    "Cảm ơn Nọc đã lun bên cạnh, lắng nghe, giúp đỡ và hiểu pn hơn cả pn tự hiểu mình 🥰 Người đâu vừa giỏi, vừa tốt bụng mà còn dễ huông nựa. Wish you all the bestttt, enjoy life 💖🌸✨"
)

# Hiệu ứng động
st.balloons()
