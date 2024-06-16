import streamlit as st
from streamlit_option_menu import option_menu
from app_utils import switch_page
import streamlit as st
from PIL import Image

im = Image.open("icon.png")
st.set_page_config(page_title = "Interviewing-System", layout = "centered",page_icon=im)

lan = st.selectbox("#### Language", ["English"])

if lan == "English":
    home_title = "Interviewing-System"
    home_introduction = "Welcome to Interviewing-System, empowering your interview preparation with generative AI."
    with st.sidebar:
        st.markdown('Interviewing-System  -  Final Year Project ')
        st.markdown("""
        #### Let's contact:
        [Satyam Kumar](https://www.linkedin.com/in/satyam-kumar-b40b04168/)


        #### Powered by

        [OpenAI](https://openai.com/)

        [FAISS](https://github.com/facebookresearch/faiss)

        [Langchain](https://github.com/hwchase17/langchain)

                    """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    #st.markdown("#### Greetings")
    st.markdown("Welcome to Interviewing-System! 👏 AI Interviewer is your personal interviewer powered by generative AI that conducts mock interviews."
                "You can upload your resume and enter job descriptions, and Interviewing-System will ask you customized questions. Additionally, you can configure your own Interviewer!")
    st.markdown("""\n""")
    with st.expander("Updates"):
        st.write("""
        18/03/2024
        - OpenAI API Access is not available. """)
    with st.expander("What's coming next?"):
        st.write("""
        Added openAI API Access and Improved voice interaction for a seamless experience. """)
    st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")
    selected = option_menu(
            menu_title= None,
            options=["Professional", "Resume", "Behavioral","Customize!"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Professional':
        st.info("""
            📚In this session, the Interviewing-System will assess your technical skills as they relate to the job description.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start introduce yourself and enjoy！ """)
        if st.button("Start Interview!"):
            switch_page("Professional Screen")
    if selected == 'Resume':
        st.info("""
        📚In this session, the Interviewing-System will review your resume and discuss your past experiences.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ """
        )
        if st.button("Start Interview!"):
            switch_page("Resume Screen")
    if selected == 'Behavioral':
        st.info("""
        📚In this session, the Interviewing-System will assess your soft skills as they relate to the job description.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！
        """)
        if st.button("Start Interview!"):
            switch_page("Behavioral Screen")
    if selected == 'Customize!':
        st.info("""
            📚In this session, you can customize your own Interviewing-System and practice with it!
             - Configure Interviewing-System in different specialties.
             - Configure Interviewing-System in different personalities.
             - Different tones of voice.

             Coming at the end of July""")
    st.markdown("""\n""")
   # st.markdown("#### Wiki")
    # st.write('[Click here to view common FAQs, future updates and more!](  )')
    #st.write(
    #        f'<iframe src="https://17nxkr0j95z3vy.embednotionpage.com/AI-Interviewer-Wiki-8d962051e57a48ccb304e920afa0c6a8" style="width:100%; height:100%; min-height:500px; border:0; padding:0;"/>',
    #        unsafe_allow_html=True,
    #    )
