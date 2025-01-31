import streamlit as st
import pyrebase

# Firebase config
firebaseConfig = {
    'apiKey': "AIzaSyCt7JaHwmHCS9Lm_hiZQv1B2XM_1eR4zPM",
    'authDomain': "posto-ai-app.firebaseapp.com",
    'databaseURL': "https://YOUR_PROJECT_ID.firebaseio.com",
    'projectId': "posto-ai-app",
    'storageBucket': "posto-ai-app.appspot.com",
    'messagingSenderId': "408360408985",
    'appId': "1:408360408985:web:55ec7842c40203f28c6508",
    'measurementId': "G-HL46XMRBKM"
}

# Firebase initialization
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# ตั้งค่าเลย์เอาต์ให้เต็มหน้าจอ
st.set_page_config(layout="wide")

# CSS เพื่อปรับแต่งพื้นหลัง สีฟอนต์ และปุ่ม
st.markdown("""
    <style>
    body {
        background-color: #232b55;
    }
    .stButton button {
        background-color: #f55;
        color: white;
        width: 100%;
        border-radius: 8px;
        height: 35px;
        font-size: 18px;
    }
    .stButton button:hover {
        background-color: #ff8787;
    }
    .big-font {
        font-size:50px !important;
        color: #f55;
    }
    .small-font {
        font-size: 18px;
        color: white;
    }
    .full-width-button {
        width: 100%; /* ทำให้ปุ่มกว้างเต็ม */
        border-radius: 8px;
        height: 35px;
        font-size: 18px;
        background-color: #f55;
        color: white;
    }
    .full-width-button:hover {
        background-color: #ff8787;
    }
    </style>
    """, unsafe_allow_html=True)

def login():
    # แบ่งหน้าจอออกเป็นสองฝั่ง
    col1, col2 = st.columns([1, 1])

    # ฝั่งซ้าย: แสดงภาพและข้อความต้อนรับ
    with col1:
        st.markdown("<h1 style='color:#f55;'>Welcome to POSTO!</h1>", unsafe_allow_html=True)
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
        st.image("https://png.pngtree.com/png-clipart/20190904/original/pngtree-green-plant-path-png-image_4461980.jpg", width=300)  # ใส่ลิงก์ภาพ
        st.markdown("<h2 style='color:#f55;'>POSTO</h2>", unsafe_allow_html=True)

    # ฝั่งขวา: ฟอร์มล็อกอิน
    with col2:
        st.markdown("<h2 style='text-align: center; color: #f55;'>Login</h2>", unsafe_allow_html=True)

        if "login_status" not in st.session_state:
            st.session_state.login_status = None  # ตั้งค่าเริ่มต้นเป็น None

        # สร้างฟอร์มล็อกอิน
        email = st.text_input("Email", placeholder="Email")
        password = st.text_input("Password", placeholder="Password", type="password")
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)  # เปลี่ยนค่า 30px ตามต้องการ
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.login_status = "success"
            except:
                st.error("Login ไม่สำเร็จ กรุณาตรวจสอบข้อมูลอีกครั้ง.")
                st.session_state.current_page = "Sign Up"  # เปลี่ยนไปยังหน้า Sign Up
                st.switch_page("pages/2_SignUp.py")  # สลับไปยังหน้า Sign Up

        if st.session_state.login_status == "success":
            st.success("Login สำเร็จ!")
            st.session_state.current_page = "home"  # เปลี่ยนไปยังหน้า Home
            st.switch_page("pages/4_Chatbot.py")  # สลับไปยังหน้า Home
        st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)  # เปลี่ยนค่า 30px ตามต้องการ
        # ลิงก์ไปยังหน้า Sign Up
        st.markdown("""<div style='text-align: center;'><span class='small-font'>Don't have an account?</span></div>""", unsafe_allow_html=True)
        
        # สร้างปุ่ม Sign Up
        if st.button("Sign Up"):
            st.session_state.current_page = "Sign Up"  # เปลี่ยนไปยังหน้า Sign Up
            st.switch_page("pages/2_SignUp.py")  # สลับไปยังหน้า Sign Up

if __name__ == "__main__":
    login()
