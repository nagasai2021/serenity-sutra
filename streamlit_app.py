import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's sambar building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Text in a box
st.markdown(
    """
    <div style="
        border: 1px solid #ddd; 
        border-radius: 5px; 
        padding: 10px; 
        background-color: #f9f9f9; 
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <p style="font-size: 16px; margin: 0; color: black">
        ఔనన్నా కాదన్నా నీలోనే నేనున్నా
        ఔనన్నా కాదన్నా నీవేగా నాలోనా
        నీ పిలుపే రోజంతా వింటున్నా
        నా మనసే రొజాగా ఇస్తున్నా
        నీ చెలిమే లోకాలే వద్దన్నా
        నీ వెనకే చిరుగాలై వస్తున్నా
        ప్రేమైనా చావైనా
        నీ తోనే ఏమైనా
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
