import streamlit as st
import google.generativeai as genai

# පිටු සැකසුම
st.set_page_config(page_title="Paper Gen", layout="centered")
st.title("📝 AI Paper Generator")

# API Key සකසන්න
# (ඔබ Streamlit Secrets වල 'GEMINI_API_KEY' ලෙස ඔබේ Key එක දමා තිබිය යුතුය)
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("API Key සොයාගත නොහැක. කරුණාකර Streamlit Secrets පරීක්ෂා කරන්න.")
    st.stop()

# අතුරුමුහුණතේ මූලද්‍රව්‍ය (Unique keys ලබා දී ඇත)
grade = st.selectbox("🎓 ශ්‍රේණිය:", [str(i) for i in range(1, 14)], key="g_key")
subject = st.text_input("📚 විෂය නම:", key="s_key")
num = st.slider("🔢 ප්‍රශ්න ගණන:", 1, 20, 5, key="n_key")

# බොත්තම
if st.button("📄 Generate Paper", key="b_key"):
    if not subject:
        st.warning("කරුණාකර විෂය නම ඇතුළත් කරන්න.")
    else:
        with st.spinner("⏳ පත්‍රය සාදමින් පවතී..."):
            try:
                # ස්ථාවර සහ සහය දක්වන මාදිලිය
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Create a {grade} grade exam paper for {subject} with {num} questions. Include a marking scheme."
                
                response = model.generate_content(prompt)
                
                st.success("✅ සාර්ථකයි!")
                st.text_area("ප්‍රශ්න පත්‍රය:", value=response.text, height=400)
                
            except Exception as e:
                st.error(f"දෝෂයක් සිදුවිය: {e}")
