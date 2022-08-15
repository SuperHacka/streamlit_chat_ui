import base64
import csv
import gettext
import random

import numpy as np
import pandas as pd
import requests
import streamlit as st
from PIL import Image
from streamlit_chat import message as st_message

# TODO  refactor the code to remove all the global function

# _ = gettext.gettext

example_image = Image.open("01.png")
example_dict = {"id": [1, 2, 3, 4],
                "value": ["This row contains example data", "Second row", "Third row", "Fourth row"]}
example_table = pd.DataFrame(example_dict)
file_path = "example_pdf.pdf"
with open(file_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    PDFbyte = f.read()
pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="250" height="200" ' \
              f'type="application/pdf"></iframe> '

map_df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [87.76, -12.4],
    columns=['lat', 'lon'])

video_file = open('sample_video.mp4', 'rb')
video_bytes = video_file.read()

# response = requests.get("http://192.168.12.169:6969/videos",
#                         auth=HTTPBasicAuth('shabil', 'shabiru'))
response = requests.get("https://catfact.ninja/fact")

file = open('sample_faq.csv', 'r')
csvreader = csv.reader(file)


def generate_answer():
    user_message = st.session_state.user_input
    st.session_state.user_chat_history.append(user_message)
    # user_message = message
    container = st.container()
    cac_center = "cac"
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
        # user_response = "Trying something out"
        # user_message = user_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

    elif "thanks" in user_message:
        bot_response = "You're welcome, anything else I can help you with?"
        bot_message = bot_response[:]
        # user_response = "Trying something out"
        # user_message = user_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

    elif "image" in user_message:
        bot_response = "Here is the example image"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000), "image": example_image})

    elif "table" in user_message:
        bot_response = "Here is the example table"
        bot_message = bot_response[:]
        # container.table(example_table)  # will be displayed outside the chat box
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000),
                                              "container": "table"})

    elif "document" in user_message:
        bot_response = "Here is the pdf document"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000),
                                              "container": "document"})

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
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000),
                                              "video": map_df})

    # Trying expander inside a container
    elif "expander" in user_message:
        bot_response = "The expander will be shown below"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000),
                                              "container": "expander_with_buttons"})

    elif "change" in user_message:
        pass
        # page = list(training_page.keys())
        # page.app()

    elif "bye" in user_message:
        bot_response = "Please leave a feedback"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append({"message": bot_message, "is_user": False, "key": random.randint(0, 1000),
                                              "container": "text_area"})

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
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000),
             "container": "form"})

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

    elif cac_center.casefold() in user_message:
        bot_response = "May I know the city you reside in?"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000), "container": "dialogue"})

    elif "petaling" in st.session_state.user_chat_history[-1]:
        bot_response = "Here are the nearest cac centre in your place..."
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000), "container": "dialogue"})


    else:
        bot_response = "Sorry could not quite get the message, could you repeat that again"
        bot_message = bot_response[:]
        st.session_state.chat_history.append({"message": user_message, "is_user": True, "key": random.randint(0, 1000)})
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

    print(st.session_state.user_chat_history[-1])


def app():
    language_settings = st.sidebar.selectbox(label="Select your preferred languages", options=("en", "my"))

    try:
        localizator = gettext.translation('base', localedir='locales', languages=[language_settings])
        localizator.install()
        _ = localizator.gettext
    except Exception as err:
        print(f"An error of {err} has occur")

    st.title(_("Training Page"))
    program_title = st.text(_("Chat interface using streamlit-chat testing Page"))

    # if language_settings == "en":
    #     st.write("English language")
    #     eng_lang = gettext.translation('base', localedir='locales', languages=[language_settings])
    #     eng_lang.install()
    # else:
    #     st.write("Malay language")
    #     my_lang = gettext.translation('base', localedir='locales', languages=[language_settings])
    #     my_lang.install()

    temp_container = st.container()
    # counter for the key id for every widget in the application
    selection_1_cnt = 1
    selection_2_cnt = 1
    thumbs_cnt = 1
    form_cnt = 1

    if "first_time_run" not in st.session_state:
        st.session_state.first_time_run = True
        st.session_state.chat_history = []
        st.session_state.user_chat_history = []
        st.session_state.texter = None

    if st.session_state.first_time_run is True:
        st.session_state.first_time_run = False
        st.session_state.chat_history = []

    if len(st.session_state.chat_history) == 0:
        st_message(
            message=_("Hello there welcome to the chatbot interface testing, Please type something to continue"))

    for chat in st.session_state.chat_history:
        if "image" in chat.keys():
            # st_message(chat["message"], chat["is_user"], chat["avatar_style"], chat["key"], chat["image"])
            st_message(**chat)
            st.image(chat["image"])

        elif "video" in chat.keys():
            st_message(**chat)
            st.video(video_bytes, format="video/mp4", start_time=0)

        elif "api" in chat.keys():  # FIXME JSON response persist even after other function is called
            st_message(**chat)
            response_json = chat["api"].json()
            st_message(
                message=_(response_json["fact"]), key=random.randint(0, 1000))
            # st.session_state.chat_history.append(
            #     {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})
            # st.write("The status for the API is: " + str(chat["api"].status_code))
            # if chat["api"].status_code == 200:
            #     # st.write("The API request is successful")
            #     response_json = chat["api"].json()
            #     bot_response = str(response_json["fact"])
            #     bot_message = bot_response[:]
            #     st.session_state.chat_history.append(
            #         {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})
            # else:
            #     st.write("There is something wrong with the request")
        elif "link" in chat.keys():
            st_message(**chat)
            st.write(chat["link"])

        elif "map" in chat.keys():
            st_message(**chat)
            st.map(chat["map"])

        elif "container" in chat.keys():
            st_message(**chat)

            if "selection_type_1" in chat["container"]:
                button_a_key = "button_a" + str(selection_1_cnt)
                button_b_key = "button_b" + str(selection_1_cnt)
                button_c_key = "button_c" + str(selection_1_cnt)
                button_a = st.button("Selection A", key=button_a_key)
                button_b = st.button("Selection B", key=button_b_key)
                button_c = st.button("Selection C", key=button_c_key)

                if button_a:
                    user_response = "I choose selection a"
                    st.session_state.user_input = user_response[:]

                elif button_b:
                    user_response = "I choose selection b"
                    st.session_state.user_input = user_response[:]

                elif button_c:
                    user_response = "I choose selection c"
                    st.session_state.user_input = user_response[:]

                selection_1_cnt += 1

            elif "selection_type_2" in chat["container"]:
                choice_1_key = "choice_1" + str(selection_2_cnt)
                choice_2_key = "choice_2" + str(selection_2_cnt)
                choice_3_key = "choice_3" + str(selection_2_cnt)
                choice_1 = st.button("Syarat Permohonan Kad Pengenalan", key=choice_1_key)
                choice_2 = st.button("Apakah dokumen permohonan kad pengenalan", key=choice_2_key)
                choice_3 = st.button("Bagaimana kalau kecurian kad pengenalan", key=choice_3_key)

                if choice_1:
                    user_response = "Syarat Permohonan Kad Pengenalan "
                    st.session_state.user_input = user_response[:]
                    # st.experimental_rerun()
                    # generate_answer()
                if choice_2:
                    user_response = "Apakah dokumen permohonan kad pengenalan "
                    st.session_state.user_input = user_response[:]
                    # generate_answer(user_response, container)
                if choice_3:
                    user_response = "Bagaimana kalau kecurian kad pengenalan "
                    st.session_state.user_input = user_response[:]
                    # generate_answer(user_response, container)
                selection_2_cnt += 1

            elif "document" in chat["container"]:
                st.markdown(pdf_display, unsafe_allow_html=True)
                # FIXME currently file downloaded is corrupted so comment out for time being
                # st.download_button(label="\U0001F4E5",
                #                    data=PDFbyte,
                #                    file_name="streamlit_chat_pdf.pdf",
                #                    mime="application/x-pdf")
            # TODO  disable user input whenever form is present
            elif "form" in chat["container"]:
                form_key = "form_key" + str(form_cnt)
                with st.expander("Feedback form"):
                    with st.form(form_key):
                        question_1 = st.text_input("What are your comments about the application")
                        question_2 = st.text_input("Any additional feedback")

                        submitted = st.form_submit_button("Submit")
                        if submitted:
                            st.write("Thanks for you feedback !")
                            bot_response = "Your feedback will be reflected on our next interaction!"
                            bot_message = bot_response[:]
                            st.session_state.chat_history.append(
                                {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})

                    form_cnt += 1
            elif "text_area" in chat["container"]:
                st.text_area("Feedback form")

            elif "table" in chat["container"]:
                # st.table(example_table)
                st.dataframe(csvreader)

            elif "expander_with_buttons" in chat["container"]:
                expander_with_buttons = st.expander(label="Sample Suggestion on an expander")
                with expander_with_buttons:
                    suggestion_1_key = "suggestion_1" + str(selection_2_cnt)
                    suggestion_2_key = "suggestion_2" + str(selection_2_cnt)
                    suggestion_3_key = "suggestion_3" + str(selection_2_cnt)
                    suggestion_4_key = "suggestion_4" + str(selection_2_cnt)
                    suggestion_5_key = "suggestion_5" + str(selection_2_cnt)
                    suggestion_6_key = "suggestion_6" + str(selection_2_cnt)

                    st.write("This expander contains lots of buttons")
                    suggestion_1 = st.button("Suggestion 1", key=suggestion_1_key)
                    suggestion_2 = st.button("Suggestion 2", key=suggestion_2_key)
                    suggestion_3 = st.button("Suggestion 3", key=suggestion_3_key)
                    suggestion_4 = st.button("Suggestion 4", key=suggestion_4_key)
                    suggestion_5 = st.button("Suggestion 5", key=suggestion_5_key)
                    suggestion_6 = st.button("Suggestion 6", key=suggestion_6_key)

                    if suggestion_1:
                        st.write("You choose suggestion 1!")
                        user_response = "Suggestion 1"
                        st.session_state.user_input = user_response[:]

            elif "dialogue" in chat["container"]:
                pass
            else:
                st_message(message="Try again, option is not available")
        else:
            st_message(**chat)  # unpacking

    ccol1, ccol2 = st.columns((0.06, 1))
    thumbs_up_key = "thumbs_up" + str(thumbs_cnt)
    thumbs_down_key = "thumbs_down" + str(thumbs_cnt)
    thumbs_up = ccol1.button(" \U0001F44D ", key=thumbs_up_key)
    thumbs_down = ccol2.button(" \U0001F44E ", key=thumbs_down_key)

    if thumbs_up:
        temp_container.write(message="Thanks for the feedback")
        bot_response = _("Thanks for the feedback")
        bot_message = bot_response[:]
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})
        thumbs_cnt += 1
        st.experimental_rerun()

    if thumbs_down:
        temp_container.write(message=_("Sorry to hear that, we will try to improve"))
        bot_response = "Sorry to hear that, we will try to improve"
        bot_message = bot_response[:]
        st.session_state.chat_history.append(
            {"message": bot_message, "is_user": False, "key": random.randint(0, 1000)})
        thumbs_cnt += 1
        st.experimental_rerun()

    col1, col2, col3 = st.columns((0.425, 0.6, 1))

    url_button = col1.button(_(
        "Display URL"))
    image_button = col2.button(_(
        "Display Image"))

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

    st.session_state.texter = cola.text_input(_("Talk to the bot"), key="user_input",
                                              on_change=generate_answer)

    # if st.session_state.texter is not None and len(st.session_state.texter.strip()) > 0:
    #     generate_answer(temp_container)

    colb.markdown("##")

    send_message_button = colb.button(" \U0001F4AC ", on_click=generate_answer)
    if send_message_button:
        pass
        # st.experimental_rerun()

    colc.markdown("##")
    upload_files_button = colc.button(" \U0001F4E4 ")
    if upload_files_button:
        st.session_state.file_store = st.file_uploader(_("Upload files here"))

    suggestion_button = st.button(_("Some suggestion answer"))
    if suggestion_button:
        pass
        # user_response = "Here is some suggestion answer"
        # st.session_state.user_input = user_response[:]
    #     user_response = "This is the generated answer"
    #     generate_answer(user_response, temp_container)


if __name__ == "__main__":
    app()
    # for chat in st.session_state.chat_history:
    #     st_message(**chat)  # unpacking

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
