import streamlit as st
import os
import pandas as pd
from model import read_name_from_image, crop_and_read_names, save_to_csv, count_names_in_csv

# สร้างโฟลเดอร์สำหรับอัปโหลดถ้าไม่มี
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CSV_FILE = 'backend/names.csv'  # แก้ไขให้ตรงตามพาธไฟล์

# กำหนด URL ของรูปโปรไฟล์
user_avatar = "https://firebasestorage.googleapis.com/v0/b/posto-ai-app.appspot.com/o/user.png?alt=media&token=f22ea9fc-4de4-4ed9-801b-4a2875312905"  # URL ของรูปโปรไฟล์ผู้ใช้
bot_avatar = "https://firebasestorage.googleapis.com/v0/b/posto-ai-app.appspot.com/o/robot.png?alt=media&token=99e37f4c-dbef-4d07-86a5-75e70585ac54"    # URL ของรูปโปรไฟล์ Chatbot

# CSS เพื่อปรับแต่งเลย์เอาต์
st.markdown("""
    <style>
        .center {
            text-align: center;
        }
        .upload-image {
            display: block;
            margin: 0 auto;
            width: 300px;  /* ปรับขนาดรูปภาพตามต้องการ */
        }
    </style>
""", unsafe_allow_html=True)
st.markdown('<h1 class="center">หน้าอัปโหลด</h1>', unsafe_allow_html=True)
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)  # เปลี่ยนค่า 30px ตามต้องการ
uploaded_file = st.file_uploader("อัปโหลดไฟล์", type=['jpg', 'png'])

if uploaded_file is not None:
    image_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    # บันทึกไฟล์ภาพ
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # ตรวจจับชื่อจากภาพ
    detected_names, boxes = read_name_from_image(image_path)

    if detected_names:
        cropped_names = crop_and_read_names(image_path, boxes)
        save_to_csv(cropped_names)

        # แสดงผลลัพธ์
        st.write("Detected Names: ", ", ".join(detected_names))
        st.write("Cropped Names: ", ", ".join(cropped_names))
        st.write("Name Counts: ", count_names_in_csv().to_dict(orient='records'))
    else:
        st.warning("ไม่พบชื่อในภาพ")

    # แสดงรูปภาพที่อัปโหลด
    st.image(image_path, caption='รูปภาพที่อัปโหลด', use_column_width=True)  # ใช้ use_column_width=True เพื่อให้รูปภาพปรับขนาดให้พอดีกับคอลัมน์
