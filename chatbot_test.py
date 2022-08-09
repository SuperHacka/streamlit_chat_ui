import base64
import random

import numpy as np
# import gmaps
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_chat import message as st_message

import training_page

chat_container = st.container()
example_image = Image.open("01.png")
example_dict = {"id": [1, 2, 3, 4],
                "value": ["This row contains example data", "Second row", "Third row", "Fourth row"]}
example_table = pd.DataFrame(example_dict)
file_path = "example_pdf.pdf"
with open(file_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    PDFbyte = f.read()
pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="250" height="200" type="application/pdf"></iframe>'

map_df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])


# gmaps.configure(api_key='AIzaSyCur_PPMlQlquZqOiT1ZXOYspfuqY9vbFs')


def app():
    # example_image = Image.open("01.png")
    # example_image = np.array(example_image)

    if "history" not in st.session_state:
        st.session_state.history = []
    if "input_text" not in st.session_state:
        st.session_state.input_text = " "
    if "texter" not in st.session_state:
        st.session_state.texter = "Hi"

    # with st.container():
    st.title("Streamlit-Chat interface")
    if len(st.session_state.history) == 0:
        st_message(
            message="Hello there welcome to the chatbot interface testing, Please type something to continue")

    for chat in st.session_state.history:
        st_message(**chat)  # unpacking

    ccol1, ccol2 = st.columns((0.06, 1))
    ccol1.button(" \U0001F44D ", key=random.randint(0, 1000))
    ccol2.button(" \U0001F44E ", key=random.randint(0, 1000))

    col1, col2, col3 = st.columns((0.319, 0.6, 1))

    url_button = col1.button(
        "Display URL")
    image_button = col2.button(
        "Display Image")

    temp_container = st.container()
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

    # texter = cola.text_input(label="", key="input_text",
    #                          placeholder="Type something to command the chatbot", on_change=generate_answer)
    print(f"--> before the initialisation, {st.session_state.texter}")

    st.session_state.texter = cola.text_input(label="", key="input_text",
                                              placeholder="Type something to command the chatbot")

    print(f"--> after the initialisation, {st.session_state.texter}")

    if st.session_state.texter is not None and len(st.session_state.texter.strip()) > 0:
        generate_answer(st.session_state.texter, temp_container)
    # if len(texter) != 0:
    #     generate_answer(texter)

    colb.markdown("##")

    send_message_button = colb.button(" \U0001F4AC ")

    colc.markdown("##")
    upload_files_button = colc.button(" \U0001F4E4 ")
    if upload_files_button:
        st.session_state.file_store = st.file_uploader("Upload files here")

    suggestion_button = st.button("Some suggestion answer")
    if suggestion_button:
        user_response = "This is the generated answer"
        # user_message = user_response[:]
        generate_answer(user_response, temp_container)
        # st.session_state.input_text = user_response[:]

        # st.text_input(label="", key="input_text", value=user_response)


# @st.experimental_singleton  # not implementing model atm just testing chat ui
# def get_models():
#     # it may be necessary for other frameworks to cache the model
#     # seems pytorch keeps an internal state of the conversation
#     model_name = "facebook/blenderbot-400M-distill"
#     tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
#     model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
#     return tokenizer, model


def generate_answer(texter, container):
    pizza_response = ""
    default_message = "default response"
    # tokenizer, model = get_models()
    # user_message = st.session_state.input_text
    user_message = texter
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

    if "help" in user_message:
        bot_response = "Click on the options below"
        bot_message = bot_response[:]
        chat_suggest = container.button(label="Helper button")
        if chat_suggest:
            option = "Here are possible leads for your queries"
            bot_message = option[:]
            st.button("What topics are available in this bot knowledge base")
            st.button("How to use this application")
            print("something")

    elif "hi" in user_message:
        bot_response = "Hello there!, do you need help with anything?"
        bot_message = bot_response[:]

    elif "hungry" in user_message:
        bot_response = "Here grab a kitkat, do you want to order from our selection? (Pizza, Drinks)"
        bot_message = bot_response[:]
        # if "order" in bot_response:
        #     sub_response = "Selections are: Pizza, Drinks"
        #     bot_message = sub_response[:]

    elif "pizza" in user_message:
        bot_response = "What flavour"
        bot_message = bot_response[:]

        # last user message is not able to be capture
        if "chicken" in user_message:
            bot_response = "coming right up"
            bot_message = bot_response[:]

    elif "image" in user_message:
        bot_response = "Here is the example image"
        bot_message = bot_response[:]
        container.image(example_image)  # will be displayed outside the chat box and disappear after widget key change
        st.button("Image example button")

    elif "table" in user_message:
        bot_response = "Here is the example table"
        bot_message = bot_response[:]
        container.table(example_table)  # will be displayed outside the chat box

    elif "document" in user_message:
        container.markdown(pdf_display, unsafe_allow_html=True)
        container.download_button(label="\U0001F4E5",
                                  data=PDFbyte,
                                  file_name="streamlit_chat_pdf.pdf",
                                  mime="application/pdf")

    elif "map" in user_message:
        container.map(map_df, use_container_width=False)

    # Trying expander inside a container
    elif "expander" in user_message:
        expander_with_buttons = container.expander(label="Sample Suggestion on an expander")
        with expander_with_buttons:
            st.write("This expander contains lots of buttons")
            st.button("Button 1")
            st.button("Button 2")
            st.button("Button 3")
            st.button("Button 4")
            st.button("Button 5")
            st.button("Button 6")

    elif "change" in user_message:
        page = list(training_page.keys())
        page.app()

    elif "bye" in user_message:
        bot_response = "Please leave a feedback"
        bot_message = bot_response[:]
        container.text_area("Feedback form")

    elif "other" in user_message:
        container.button("Selection A")
        container.button("Selection B")
        container.button("Selection C")

    elif "pengenalan" in user_message:
        bot_response = "Soalan berkaitan"
        bot_message = bot_response[:]
        choice_1 = container.button("Syarat Permohonan Kad Pengenalan", key=random.randint(0, 1000))
        choice_2 = container.button("Apakah dokumen permohonan kad pengenalan", key=random.randint(0, 1000))
        choice_3 = container.button("Bagaimana kalau kecurian kad pengenalan", key=random.randint(0, 1000))

        # current implementation have problem where only the first choice answer will be transferred to user_response
        if choice_1:
            user_response = "Syarat Permohonan Kad Pengenalan"
            generate_answer(user_response, container)
        if choice_2:
            user_response = "Apakah dokumen permohonan kad pengenalan"
            generate_answer(user_response, container)
        if choice_3:
            user_response = "Bagaimana kalau kecurian kad pengenalan"
            generate_answer(user_response, container)

    else:
        bot_response = "Sorry could not quite get the message"
        bot_message = bot_response[:]
    # if "help" in bot_message:
    #     user_response = "Thanks for the info"  # does not work as intended
    #     user_message = user_response[:]

    # order of message appearing in the chat interface, from user followed by bot
    st.session_state.history.append(
        {"message": user_message, "is_user": True, "avatar_style": "female",
         "key": random.randint(0, 1000)})
    st.session_state.history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

# css styling for the chat interface that allow scrolling
# chat_element_style = """
# <style>
# .css-12oz5g7 {
#     flex: 1 1 0%;
#     width: 100%;
#     padding: 6rem 1rem 10rem;
#     max-width: 46rem;
#     overflow: scroll;
# }
# </style>
# """
# st.markdown(body=chat_element_style, unsafe_allow_html=True)
