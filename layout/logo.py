import streamlit as st

def logo():
    return(
        st.logo(image='assets/logo3.png', icon_image='assets/logo.png'),
        st.markdown('''<style>
            img[data-testid="stLogo"] {
            height: 4rem;
            }</style>''', unsafe_allow_html=True)
    )