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
        height: 45px;
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
    .container {
        display: flex;
        justify-content: space-between;
    }
    .form-container {
        width: 50%;
        padding: 20px;
    }
    .image-container {
        width: 50%;
        background-size: cover;
        background-position: center;
    }
    .link {
        color: #f55;
        cursor: pointer;
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

def sign_up():
    if "signup_status" not in st.session_state:
        st.session_state.signup_status = None  # ตั้งค่าเริ่มต้นเป็น None

    # สร้างเลย์เอาต์สำหรับแบ่งครึ่งหน้า
    col1, col2 = st.columns([1, 1])  # สร้างสองคอลัมน์

    with col1:
        st.markdown("<h1 style='color:#f55; font-size: 50px;'>Welcome to POSTO!</h1>", unsafe_allow_html=True)
        st.markdown("<div class='image-container'></div>", unsafe_allow_html=True)
        st.image("https://png.pngtree.com/png-clipart/20190904/original/pngtree-green-plant-path-png-image_4461980.jpg", width=300)
        # เปลี่ยนคำว่า POSTO ให้เล็กลงและเป็นสีแดง
        st.markdown("<h1 style='color:#f55; font-size: 36px;'>POSTO</h1>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 style='color:#f55; font-size: 50px;'>Sign Up</h1>", unsafe_allow_html=True)
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        # เพิ่มช่องว่างด้านบนของปุ่ม Sign Up
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)  # เปลี่ยนค่า 30px ตามต้องการ

        if st.button("Sign Up"):
            try:
                auth.create_user_with_email_and_password(email, password)
                st.session_state.signup_status = "success"
            except:
                st.error("Sign Up ไม่สำเร็จ กรุณาตรวจสอบข้อมูลอีกครั้ง.")

        if st.session_state.signup_status == "success":
            st.success("Sign Up สำเร็จ! กรุณาเข้าสู่ระบบ.")
            st.session_state.current_page = "login"  # เปลี่ยนไปยังหน้า Home
            st.switch_page("pages/1_Login.py")  # สลับไปยังหน้า Login

        # ข้อความกลับไปยังหน้า Login
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)  # เพิ่มระยะห่าง
        if st.button("Back to LOGIN"):
            st.session_state.current_page = "login"  # เปลี่ยนไปยังหน้า Sign Up
            st.switch_page("pages/1_Login.py")  # สลับไปยังหน้า Sign Up
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    sign_up()
