import streamlit as st

def main():
    # กำหนดหน้าแรกเป็น login
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login_for_user"
    
    # ตรวจสอบสถานะของ current_page และเรียก switch_page ตามหน้า
    if st.session_state.current_page == "login_for_user":
        st.switch_page("pages/1_Login.py")  # ไปที่หน้า Login
    elif st.session_state.current_page == "login_for_ad":
        st.switch_page("pages/2_SignUp.py")  # ไปที่หน้า Sign Up
    # elif st.session_state.current_page == "home":
    #     st.switch_page("pages/5_Home.py")  # ไปที่หน้า Sign Up
    # elif st.session_state.current_page == "chat":
    #     st.switch_page("pages/4_Chatbot.py")  # ไปที่หน้า Chatbot
    # elif st.session_state.current_page == "admin":
    #     st.switch_page("pages/3_Admin.py")  # ไปที่หน้า Admin

if __name__ == "__main__":
    main()

