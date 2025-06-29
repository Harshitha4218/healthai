import streamlit as st

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
            # ✅ Mocked AI Response
            st.subheader("💡 AI Response:")
            st.success(f"(Mock response) You entered: {prompt}. Possible condition: Flu or Viral Fever.")
        else:
            st.warning("⚠️ Please enter a symptom before submitting.")

if __name__ == "__main__":
    main()
