import streamlit as st
import pandas as pd
from streamlit_chat import message
import os

# กำหนดค่าเริ่มต้นสำหรับ messages
st.session_state.setdefault('past', [])
st.session_state.setdefault('generated', [])

# สร้างโฟลเดอร์สำหรับอัปโหลดถ้าไม่มี
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CSV_FILE = 'backend/names.csv'  # แก้ไขให้ตรงตามพาธไฟล์

# กำหนด URL ของรูปโปรไฟล์
user_avatar = "https://firebasestorage.googleapis.com/v0/b/posto-ai-app.appspot.com/o/user.png?alt=media&token=f22ea9fc-4de4-4ed9-801b-4a2875312905"  # URL ของรูปโปรไฟล์ผู้ใช้
bot_avatar = "https://firebasestorage.googleapis.com/v0/b/posto-ai-app.appspot.com/o/robot.png?alt=media&token=99e37f4c-dbef-4d07-86a5-75e70585ac54"  # URL ของรูปโปรไฟล์ Chatbot

# กำหนดค่าเลย์เอาต์
st.set_page_config(page_title="Chatbot", layout="wide")

# CSS เพื่อปรับแต่ง
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .stButton button {
        background-color: #ff4c4c;
        color: white;
        border-radius: 8px;
        height: 45px;
        font-size: 18px;
        width: 150px;
    }
    .stButton button:hover {
        background-color: #ff8787;
    }
    .chat-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Chatbot")

# ฟังก์ชันสำหรับการตรวจสอบคำถามใน CSV
def check_question_in_csv(question):
    try:
        df = pd.read_csv(CSV_FILE)  # อ่านไฟล์ CSV
        return question in df['name'].values
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการอ่านไฟล์ CSV: {e}")
        return False

# ฟังก์ชันที่จัดการคำถาม
def handle_chat(question):
    if question:
        if check_question_in_csv(question):
            return f"✅ คำถาม '{question}' ถูกพบใน CSV."
        else:
            return f"❌ คำถาม '{question}' ไม่ถูกพบใน CSV."
    return "🚫 กรุณาถามคำถามที่ถูกต้อง."

# ฟังก์ชันสำหรับการส่งข้อความ
def on_input_change():
    user_input = st.session_state.user_input
    if user_input:  # ตรวจสอบว่ามีข้อมูล
        st.session_state.past.append(user_input)
        # เรียกใช้ฟังก์ชันเพื่อจัดการคำถามและรับคำตอบ
        answer = handle_chat(user_input)
        st.session_state.generated.append(answer)
        st.session_state.user_input = ""  # ล้างช่องข้อความหลังจากส่ง

# ตรวจสอบการตั้งค่า session_state
if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

# แสดงข้อความใน container
chat_placeholder = st.empty()

# ส่วนที่แสดงข้อความ
with chat_placeholder.container():
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f"user_{i}")
        message(st.session_state['generated'][i], key=f"bot_{i}")
    st.markdown("</div>", unsafe_allow_html=True)

# ช่องป้อนข้อความ
st.text_input("ถามคำถามของคุณที่นี่:", on_change=on_input_change, key="user_input")   

# ปุ่มเพื่อกลับไปยังหน้า login
if st.button("กลับไปยังหน้า Login"):
    st.session_state.current_page = "login"  # เปลี่ยนไปยังหน้า Login
    st.switch_page("pages/1_Login.py")  # สลับไปยังหน้า Login
