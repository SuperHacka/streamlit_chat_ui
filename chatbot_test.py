import os
import random

import streamlit as st
from PIL import Image
from streamlit_chat import message as st_message

chat_container = st.container()


def app():
    example_image = Image.open("01.png")
    # example_image = np.array(example_image)
    img = os.path.abspath("01.png")
    if "history" not in st.session_state:
        st.session_state.history = []
    if "input_text" not in st.session_state:
        st.session_state.input_text = " "
    # with st.container():
    st.title("Streamlit-Chat interface")

    if len(st.session_state.history) == 0:
        st_message(
            message="Hello there welcome to the chatbot interface testing, Please type something to continue")

    for chat in st.session_state.history:
        st_message(**chat)  # unpacking

    col1, col2, col3 = st.columns((0.5, 0.6, 1))

    url_button = col1.button(
        "Display URL")
    image_button = col2.button(
        "Display Image")

    # not_assigned = col3.button(
    #     "Placeholder button")

    if url_button:
        st_message("Please click the link below ")
        st.write(
            "check this out [link](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley)")

    if image_button:
        try:
            st_message(example_image)
        except:
            st_message("Here is the image you requested")
            st.image(example_image)

    cola, colb, colc = st.columns((1, 0.1, 0.2))

    texter = cola.text_input(label="", key="input_text", on_change=generate_answer,
                             placeholder="Type something to command the chatbot")
    colb.markdown("##")

    send_message_button = colb.button(" \U0001F4AC ")

    colc.markdown("##")
    upload_files_button = colc.button(" \U0001F4E4 ")
    if upload_files_button:
        st.file_uploader("Upload files here")

    suggestion_button = st.button("Some suggestion answer")
    if suggestion_button:
        user_response = "howdy ho!"
        st.text_input(label="", key="input_text", value=user_response)


# @st.experimental_singleton  # not implementing model atm just testing chat ui
# def get_models():
#     # it may be necessary for other frameworks to cache the model
#     # seems pytorch keeps an internal state of the conversation
#     model_name = "facebook/blenderbot-400M-distill"
#     tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
#     model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
#     return tokenizer, model


def generate_answer():
    default_message = "default response"
    # tokenizer, model = get_models()
    user_message = st.session_state.input_text
    bot_message = default_message[:]
    # inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
    # result = model.generate(**inputs)
    # message_bot = tokenizer.decode(
    #     result[0], skip_special_tokens=True
    # )  # .replace("<s>", "").replace("</s>", "")
    # suggestion_button = st.button("Some suggestion answer")
    # if suggestion_button:
    #     user_response = "howdy ho!"
    #     user_message = user_response[:]
    if "yo" in user_message:
        chat_suggest = st.button(label="Chat suggestions")
        if chat_suggest:
            option = "Please select from this options"
            bot_message = option[:]
            st.write("Button is functioning")
            print("something")

    elif "hi" in user_message:
        bot_response = "Hello there!, do you need help with anything?"
        bot_message = bot_response[:]

    elif "hungry" in user_message:
        bot_response = "Here grab a kitkat"
        bot_message = bot_response[:]

    elif "pizza" in user_message:
        bot_response = "What flavour"
        bot_message = bot_response[:]

    if "chicken" in user_message:
        bot_response = "We will deliver to you shortly"
        bot_message = bot_response[:]

    # if "help" in bot_message:
    #     user_response = "Thanks for the info"  # does not work as intended
    #     user_message = user_response[:]

    # order of message appearing in the chat interface, from user followed by bot
    st.session_state.history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
    st.session_state.history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})


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
