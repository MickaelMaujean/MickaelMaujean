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


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Amogh :wave:")
    st.title("A Data Analyst From India")
    st.write(
        "I am passionate about finding ways to use Python and BI tools to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://amogh9594.github.io/amoghkawleportfolio/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Formerly working as an Software Developer at Parekh Integrated Services Pvt.Ltd. Developed a Software for Company and done some automation project also. 1.6 years of industry experience as a Data Analyst. Experience in python for data science work. Experience of dashboard development in Power BI, Tableau and Data Studio.
            - Programming Languages: Java, Python, R, Julia, Android, Web Development.
            - Databases: Oracle, MySQL, SqlLite.
            - Reporting Tools: Tableau, Google Data Studio, Power BI.
            """
        )
        #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Named Entity Recognition for Hindi-English Code-Mixed Twitter Text")
        st.write(
            """
            This project uses twitter api and extracts tweets from twitter. Code-mixed text further complicates the process with it’s unstructured and incomplete information. We propose experiments with different machine learning classification algorithms with word, character and lexical features. The algorithms we experimented with are Decision tree, Long Short-Term Memory (LSTM), and Conditional Random Field (CRF).
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Passport OCR Using Python")
        st.write(
            """
            MRPs are passports that can be automatically read and processed using OCR. Parsing the passport MRZ using OCR is an important part of our data extraction.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/rkawle23@gmail.com" method="POST">
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
