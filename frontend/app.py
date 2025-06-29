import streamlit as st
import requests 
import streamlit as st

def main():
    st.set_page_config(page_title="HealthAI", layout="wide")
    st.title("🏥 HealthAI - Intelligent Healthcare Assistant")
    st.write("Welcome to the SmartInternz IBM project!")
    
    # Example UI
    st.header("👤 Patient Chat")
    user_input = st.text_input("Ask something about your health:")
    if st.button("Submit"):
        st.success(f"(Mock response) You asked: {user_input}")

if __name__ == "__main__":
    main()


st.set_page_config(page_title="HealthAI Assistant", page_icon="🧠")
st.title("🧠 HealthAI - Disease Assistant")

# Input field
prompt = st.text_input("Enter your symptoms (e.g., fever, cough, etc.):")

# Button
if st.button("Submit"):
    if prompt.strip() != "":
        try:
            # Make POST request to FastAPI backend
            response = requests.post(
                "http://127.0.0.1:8000/generate",
                json={"prompt": prompt}
            )

            # Display result
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
