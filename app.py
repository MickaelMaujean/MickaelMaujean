import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Personal Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")
img_contact_form = Image.open("Electric-cars.png")
img_lottie_animation = Image.open("POimage.jpeg")
img_hobbies = Image.open("")
img_skills = Image.open("")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, My name is Mickael Maujean :wave:")
    st.title("An IT Product owner & Scrum Master - PMP certified")
    st.write(
        "I am passionate about tech. and leading product from the doscovery and roadmap creation to the different deliveries accross the lifecycle. ."
    )
    st.write("[Learn More >](https://mickaelmaujean.github.io/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Formely working as Technical Project Manager within the Automotive Industry in both waterfall and hybrid management approach,
            I am now acting as IT Prodict Owner and Scrum (PMP) in cloud based Agile environment managing products roadmap from the discovery to the delivery in the following area:
            - Mobile Development
            - Web site, web app
            - Data Science
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Experience")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("IT Product Owner & Scrum Master - PMP")
        st.write(
            """
            This project uses twitter api and extracts tweets from twitter. Code-mixed text further complicates the process with it’s unstructured and incomplete information. We propose experiments with different machine learning classification algorithms with word, character and lexical features. The algorithms we experimented with are Decision tree, Long Short-Term Memory (LSTM), and Conditional Random Field (CRF).
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Technical Project Manager")
        st.write(
            """
            MRPs are passports that can be automatically read and processed using OCR. Parsing the passport MRZ using OCR is an important part of our data extraction.
            """
        )

# ---- SKILLS & HOBBIES----
with st.container():
    st.write("---")
    st.header("My Skills & Hobbies")
    st.write("##")
    skills_image, skills_column, hobbies_image, hobbies_column = st.columns((1, 2, 3, 4))
    with skills_image:
        st.image()
    with skills_column:
        st.write(
            """
            Mobile Development:
            - Flutter cross platform
            - Native iOS and Android SDK
            - Application deployment, release note and publication on stores

            Software Development:
            - Backend with python knowledge and expertise
            - APIs with python and fastAPI, postman test
            - Frontend knowledge with Javascript
            """
        )
    with hobbies_column:
        st.write(
            """
            Football:
            - 
            - 
            Chess
            Travel:
            - 
            - 
            Trail / Running:
            - 
            - 
            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mickael.maujean@hotmail.fr" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
