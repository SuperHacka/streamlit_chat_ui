import gettext

import streamlit as st

import chatbot_test
import training_page

_ = gettext.gettext


def run():
    # st.set_page_config(layout="wide", page_title="JPJ Image Labeller")

    # noinspection PyPep8Naming
    PAGES = {
        "Training Page": training_page,
        "Streamlit-Chat": chatbot_test,

    }
    st.sidebar.title('Navigation')

    selection = st.sidebar.selectbox('Page directory :', list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

    language_settings = st.sidebar.selectbox(label="Select your preferred languages", options=("English", "Bahasa"))

    if language_settings == "English":
        st.write("English")
    else:
        st.write("Bahasa")

    hide_streamlit_menu = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>

    """
    # st.markdown(hide_streamlit_menu, unsafe_allow_html=True)

    hide_streamlit_style = """
    <style>
    .css-1y0tads {padding-top: 0rem;},
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.markdown("""
    <style>
        .css-hxt7ib {
    padding-top: 2.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
    }

    </style>
    """, unsafe_allow_html=True)

    top_padding_adjustment = """
    <style>
     .css-18e3th9 {
    flex: 1 1 0%;
    width: 100%;
    padding: 2rem 3.5rem 10rem;
    min-width: auto;
    max-width: initial;
    }
    </style>
    """
    st.markdown(top_padding_adjustment, unsafe_allow_html=True)


if __name__ == "__main__":
    run()
