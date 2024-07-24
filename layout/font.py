import streamlit as st

def font():
    return(
        st.markdown(
    """
            <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital@0;1&display=swap" rel="stylesheet">
            <style>
            * {
                font-family: "Montserrat", sans-serif;
            }
            img[data-testid="stLogo"] {
            height: 25rem;
            width: 22rem
}
h1, .title {
    font-weight: 800;
}
</style>
</style>""",
    unsafe_allow_html=True,
)
    )