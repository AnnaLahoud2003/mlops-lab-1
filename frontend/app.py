import os
import requests
import streamlit as st

INFERENCE_URL = os.environ.get("INFERENCE_URL", "http://127.0.0.1:8000")

st.title("Food-11 classifier")

uploaded = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    st.image(uploaded, width=300)
    files = {"file": (uploaded.name, uploaded.getvalue(), uploaded.type)}
    try:
        response = requests.post(f"{INFERENCE_URL}/predict", files=files, timeout=60)
    except requests.exceptions.ConnectionError as e:
        st.error(f"Could not reach inference service at {INFERENCE_URL}: {e}")
        st.stop()

    if response.ok:
        result = response.json()
        # serve.py returns "prediction"; the lab template expected "category"
        label = result.get("category") or result.get("prediction")
        st.write(f"**Prediction:** {label} ({result['confidence']:.1%})")
    else:
        st.error(f"Inference service returned {response.status_code}: {response.text}")