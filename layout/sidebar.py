import streamlit as st

def sidebar():
    return(
        st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #034ea2;
    }
    
    .st-emotion-cache-ue6h4q {
                color: white
            }
</style>
""", unsafe_allow_html=True)
    )