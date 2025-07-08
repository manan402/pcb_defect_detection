import streamlit as st
import os
from predict import predict
from PIL import Image

# Set page config
st.set_page_config(
    page_title="PCB Defect Classifier",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="auto",
)

# Inject custom CSS for styling
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f5f7fa;
        }
        .title {
            font-size: 2.5em;
            font-weight: 700;
            color: #2E3A59;
            margin-bottom: 0.3em;
        }
        .description {
            font-size: 1.1em;
            color: #555;
            margin-bottom: 2em;
        }
        .prediction-box {
            padding: 20px;
            border-radius: 12px;
            background-color: #e0f7fa;
            color: #006064;
            font-size: 1.5em;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .footer {
            color: #aaa;
            font-size: 0.9em;
            margin-top: 4em;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# UI
st.markdown('<div class="title">🔍 PCB Defect Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Upload a PCB image and the AI model will predict the type of defect.<br>Supports: <b>missing_hole</b>, <b>mouse_bite</b>, <b>open_ckt</b>, etc.</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="🖼 Uploaded Image", use_column_width=True)

    # Save temporarily
    temp_path = "temp.jpg"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    # Predict
    with st.spinner("Predicting... 🧠"):
        label = predict(temp_path)

        st.markdown(f"""
                <div style="
                    background-color: #d0f0c0;
                    color: #1b5e20;
                    padding: 20px;
                    border-radius: 10px;
                    font-size: 1.6em;
                    font-weight: 600;
                    text-align: center;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    margin-top: 20px;">
                    Prediction: <span style="text-transform:uppercase;">{label}</span>
                </div>
            """, unsafe_allow_html=True)

    # Cleanup
    os.remove(temp_path)
else:
    st.info("Please upload a PCB image to get started.")

# Footer
st.markdown('<div class="footer">Built with ❤️ using TensorFlow & Streamlit · Manan Gohel 2025</div>', unsafe_allow_html=True)
