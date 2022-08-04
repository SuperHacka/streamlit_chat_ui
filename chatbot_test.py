import random

import streamlit as st
from streamlit_chat import message as st_message

chat_container = st.container()


def app():
    if "history" not in st.session_state:
        st.session_state.history = []

    # with st.container():
    st.title("Streamlit-Chat interface")

    if len(st.session_state.history) == 0:
        st_message(
            message="Hello there welcome to the chatbot interface testing, Please type something to continue")

    for chat in st.session_state.history:
        st_message(**chat)  # unpacking

    col1, col2, col3 = st.columns((0.3, 0.5, 1))

    ok_button = col1.button(
        "click me")
    no_button = col2.button(
        "no don't click me")

    yes_button = col3.button(
        "yes click me")

    if ok_button:
        # st_message("Please click this link [link](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley)")
        st_message("Please click the link below")
        st.write(
            "check this out [link](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley)")
        print("something")

    cola, colb, colc = st.columns((1, 0.1, 0.2))

    cola.text_input(label="", key="input_text", on_change=generate_answer,
                    placeholder="Type something to command the chatbot")
    colb.markdown("##")
    colb.button(" \U0001F4AC ")

    colc.markdown("##")
    colc.button(" \U0001F4E4 ")


# @st.experimental_singleton  # not implementing model atm just testing chat ui
# def get_models():
#     # it may be necessary for other frameworks to cache the model
#     # seems pytorch keeps an internal state of the conversation
#     model_name = "facebook/blenderbot-400M-distill"
#     tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
#     model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
#     return tokenizer, model

def generate_answer():
    # tokenizer, model = get_models()
    user_message = st.session_state.input_text
    bot_message = "Loading the model"
    # inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
    # result = model.generate(**inputs)
    # message_bot = tokenizer.decode(
    #     result[0], skip_special_tokens=True
    # )  # .replace("<s>", "").replace("</s>", "")

    st.session_state.history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
    st.session_state.history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})
    if "yo" in user_message:
        chat_suggest = st.button(label="Chat suggestions")
        if chat_suggest:
            bot_message = "Please select from this options"
            st.write("Button is functioning")
            print("something")


# css styling for the chat interface that allow scrolling
chat_element_style = """
<style>
.css-12oz5g7 {
    flex: 1 1 0%;
    width: 100%;
    padding: 6rem 1rem 10rem;
    max-width: 46rem;
    overflow: scroll;
}
</style>
"""
st.markdown(body=chat_element_style, unsafe_allow_html=True)
