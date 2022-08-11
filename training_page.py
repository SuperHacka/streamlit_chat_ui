import base64
import random

import numpy as np
import pandas as pd
import requests
import streamlit as st
from PIL import Image
from streamlit_chat import message as st_message

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
    np.random.randn(1000, 2) / [50, 50] + [87.76, -12.4],
    columns=['lat', 'lon'])

video_file = open('sample_video.mp4', 'rb')
video_bytes = video_file.read()

response = requests.get("https://catfact.ninja/docs/api-docs.json")


# TODO  use container inside generate answer function
# TODO  connect to api,
def generate_answer():
    user_message = st.session_state.user_input
    container = st.container()
    if "help" in user_message:
        bot_response = "Click on the options below"
        bot_message = bot_response[:]
        # chat_suggest = container.button(label="Helper button")
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

    elif "hi" in user_message:
        bot_response = "Hello there!, do you need help with anything?"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

    elif "image" in user_message:
        bot_response = "Here is the example image"
        bot_message = bot_response[:]
        # container.image(example_image)  # will be displayed outside the chat box and disappear after widget key change
        # st.session_state.chat_history.append(
        #     {"message": user_message, "is_user": True, "avatar_style": "female",
        #      "key": random.randint(0, 1000), "image": example_image})
        # st.session_state.chat_history.append(
        #     {"message": bot_message, "is_user": False, "avatar_style": "personas", "key": random.randint(0, 1000),
        #      "image": example_image})
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000), "image": example_image})

    elif "table" in user_message:
        bot_response = "Here is the example table"
        bot_message = bot_response[:]
        # container.table(example_table)  # will be displayed outside the chat box
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

    elif "document" in user_message:
        bot_response = "Here is the pdf document"
        bot_message = bot_response[:]
        # container.markdown(pdf_display, unsafe_allow_html=True)
        # container.download_button(label="\U0001F4E5",
        #                           data=PDFbyte,
        #                           file_name="streamlit_chat_pdf.pdf",
        #                           mime="application/x-pdf")
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

    elif "map" in user_message:
        bot_response = "The map will be shown below"
        bot_message = bot_response[:]
        # container.map(map_df, use_container_width=False)
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000)
                                                 , "map": map_df})

    elif "video" in user_message:
        bot_response = "The video will be shown below"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000)
                                                 , "video": map_df})

    # Trying expander inside a container
    elif "expander" in user_message:
        bot_response = "The expander will be shown below"
        bot_message = bot_response[:]
        expander_with_buttons = container.expander(label="Sample Suggestion on an expander")
        with expander_with_buttons:
            st.write("This expander contains lots of buttons")
            st.button("Suggestion 1")
            st.button("Suggestion 2")
            st.button("Suggestion 3")
            st.button("Suggestion 4")
            st.button("Suggestion 5")
            st.button("Suggestion 6")

    elif "change" in user_message:
        pass
        # page = list(training_page.keys())
        # page.app()

    elif "bye" in user_message:
        bot_response = "Please leave a feedback"
        bot_message = bot_response[:]
        # container.text_area("Feedback form")
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

    elif "other" in user_message:
        bot_response = "Here are possible interactions with the bot"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000), "container": "selection_type_1"})

    elif "pengenalan" in user_message:
        bot_response = "Soalan berkaitan"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000),
             "container": "selection_type_2"})

    elif "form" in user_message:
        bot_response = "Here is the form provided"
        bot_message = bot_response[:]
    #     with container.form("Chat Feedback"):
    #         st.write("Feedback form")
    #
    #         question_1 = st.text_input("What are your comments about the application")
    #         question_2 = st.text_input("Any additional feedback")
    #
    #         submitted = st.form_submit_button("Submit")
    #         if submitted:
    #             st.write("Thanks for you feedback !")
    #     st.session_state.history.append(
    #         {"message": bot_message, "is_user": False, "avatar_style": "personas", "key": random.randint(0, 1000)})
    #
    elif "api" in user_message:
        bot_response = "Example api shown below"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000), "api": response})

    elif "link" in user_message:
        bot_response = "Please click the link below "
        bot_message = bot_response[:]

        web_link = "check this out [link](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley)"
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000),
             "link": web_link})

    else:
        bot_response = "Sorry could not quite get the message, could you repeat that again"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})


def app():
    st.title("Training Page")
    st.text("Chatbot Testing Page")
    temp_container = st.container()

    if "first_time_run" not in st.session_state:
        st.session_state.first_time_run = True
        st.session_state.chat_history = []

    if st.session_state.first_time_run is True:
        st.session_state.first_time_run = False

    if len(st.session_state.chat_history) == 0:
        st_message(
            message="Hello there welcome to the chatbot interface testing, Please type something to continue")

    for chat in st.session_state.chat_history:
        if "image" in chat.keys():
            # st_message(chat["message"], chat["is_user"], chat["avatar_style"], chat["key"], chat["image"])
            st_message(**chat)
            st.image(chat["image"])

        elif "video" in chat.keys():
            st_message(**chat)
            st.video(video_bytes, format="video/mp4", start_time=0)

        elif "api" in chat.keys():
            st_message(**chat)
            st.write("The status for the API is: " + str(chat["api"].status_code))

        elif "link" in chat.keys():
            st_message(**chat)
            st.write(chat["link"])

        elif "map" in chat.keys():
            st_message(**chat)
            st.map(chat["map"])

        elif "container" in chat.keys():
            st_message(**chat)

            if "selection_type_1" in chat["container"]:
                st.button("Selection A")
                st.button("Selection B")
                st.button("Selection C")

            elif "selection_type_2" in chat["container"]:
                choice_1 = st.button("Syarat Permohonan Kad Pengenalan", key=random.randint(0, 1000))
                choice_2 = st.button("Apakah dokumen permohonan kad pengenalan", key=random.randint(0, 1000))
                choice_3 = st.button("Bagaimana kalau kecurian kad pengenalan", key=random.randint(0, 1000))

                if choice_1:
                    user_response = "Syarat Permohonan Kad Pengenalan"
                    st.session_state.user_input = user_response[:]
                    # generate_answer(user_response, container)
                if choice_2:
                    user_response = "Apakah dokumen permohonan kad pengenalan"
                    # generate_answer(user_response, container)
                if choice_3:
                    user_response = "Bagaimana kalau kecurian kad pengenalan"
                    # generate_answer(user_response, container)

        else:
            st_message(**chat)  # unpacking

    col1, col2, col3 = st.columns((0.425, 0.6, 1))

    url_button = col1.button(
        "Display URL")
    image_button = col2.button(
        "Display Image")

    # if url_button:
    #     st_message("Please click the link below ")
    #     st.write(
    #         "check this out [link](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley)")
    #
    # if image_button:
    #     try:
    #         st_message(example_image)
    #     except:
    #         st_message("Here is the image you requested")
    #         st.image(example_image)

    cola, colb, colc = st.columns((1, 0.1, 0.2))

    st.session_state.texter = cola.text_input("Talk to the bot", key="user_input",
                                              on_change=generate_answer)

    # if st.session_state.texter is not None and len(st.session_state.texter.strip()) > 0:
    #     generate_answer(temp_container)

    colb.markdown("##")

    send_message_button = colb.button(" \U0001F4AC ")
    if send_message_button:
        st.experimental_rerun()

    colc.markdown("##")
    upload_files_button = colc.button(" \U0001F4E4 ")
    if upload_files_button:
        st.session_state.file_store = st.file_uploader("Upload files here")

    suggestion_button = st.button("Some suggestion answer")
    # if suggestion_button:
    #     user_response = "This is the generated answer"
    #     generate_answer(user_response, temp_container)


if __name__ == "__main__":
    app()
    # for chat in st.session_state.chat_history:
    #     st_message(**chat)  # unpacking
