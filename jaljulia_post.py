import streamlit as st
import requests
import tweepy

# --- إعدادات الأمان ---
def check_password():
    if "password_correct" not in st.session_state:
        st.text_input("أدخل كلمة المرور للوصول إلى لوحة النشر", type="password", key="password_input")
        if st.button("دخول"):
            if st.session_state.password_input == st.secrets["password"]:
                st.session_state["password_correct"] = True
            else:
                st.error("❌ كلمة المرور خاطئة")
        return False
    return True

# --- واجهة التطبيق ---
if check_password():
    st.title("🚀 لوحة النشر الموحد - جلجولية نت")
    st.write("اكتب محتوى الخبر وسيتم توزيعه بضغطة زر واحدة.")

    news_content = st.text_area("محتوى الخبر:", height=200)

    col1, col2, col3 = st.columns(3)
    with col1:
        post_x = st.checkbox("منصة X (تويتر)")
    with col2:
        post_tg = st.checkbox("تلغرام")
    with col3:
        post_wa = st.checkbox("واتساب (عبر الأتمتة)")

    if st.button("انشر الآن على الجميع"):
        if not news_content:
            st.warning("الرجاء كتابة نص الخبر أولاً")
        else:
            with st.spinner('جاري النشر...'):
                # سيتم إضافة دوال النشر الحقيقية هنا باستخدام st.secrets للتوكنات
                st.success("✅ تمت عملية النشر بنجاح!")
                st.balloons()