import streamlit as st
import requests

st.set_page_config(page_title="HealthAI", layout="wide")

def main():
    st.title("🏥 HealthAI - Intelligent Healthcare Assistant")
    st.write("Welcome to the SmartInternz IBM project!")

    # 👤 Patient Chat
    st.header("👤 Patient Chat")
    user_input = st.text_input("Ask something about your health:")
    if st.button("Submit Chat", key="submit_chat"):
        st.success(f"(Mock response) You asked: {user_input}")

    # 🧠 Disease Prediction
    st.header("🧠 Disease Assistant")
    prompt = st.text_input("Enter your symptoms (e.g., fever, cough, etc.):", key="symptom_input")

    if st.button("Submit Symptoms", key="submit_symptoms"):
        if prompt.strip() != "":
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/generate",
                    json={"prompt": prompt}
                )

                if response.status_code == 200:
                    result = response.json()
                    st.subheader("💡 AI Response:")
                    st.success(result["response"])
                else:
                    st.error(f"❌ Backend error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"⚠️ Request failed: {e}")
        else:
            st.warning("⚠️ Please enter a symptom before submitting.")

if __name__ == "__main__":
    main()
