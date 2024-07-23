import streamlit as st

def header():
    return (
        st.markdown("""
                    <style>
                        [data-testid="stHeader"] {
                        background: none;
                        color: white;
                        }
                      
                        .logo {
                            position: relative;
                            width: 100px;
                            left: 100px;
                            padding: 0.5rem 0 0.5rem 0; 
                        }
                    </style>
<div class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #034ea2;">
    <img class="logo" src="https://portal.pi.gov.br/jucepi/wp-content/themes/academica_pro_3/img/logo-rodape.png"></img
    
</div>
""", unsafe_allow_html=True))