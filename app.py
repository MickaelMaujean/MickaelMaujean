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
img_hobbies = Image.open("hobbies.png")
img_skills = Image.open("skills.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, My name is Mickael Maujean :wave: :fr:")
    st.title("An IT Product Owner & Scrum Master - PMP certified")
    st.write(
        "I am passionate about tech. and leading product from the discovery and roadmap creation to the different deliveries accross the lifecycle."
    )
    st.write("[Learn More LinkedIn >](https://www.linkedin.com/in/mickael-maujean-992932bb/)")
    st.write("[Learn More GitHub >](https://github.com/MickaelMaujean)")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do :office_worker:")
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

# ---- EXPERIENCE ----
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
            The company is a SaaS developping a core platform capable of collecting mobile phone data, adding context (traffic, road conditions and wethear) and providing metrics for any driver behavior.
            It was also ensuring development of mobile app, web dhasboards as well a web app using this platform. 

            I was responsible of the following missions;
            - Responsible of the comnpany products roadmap and discovery
            - Creating/Maintaining backlog and elaboration of user stories
            - Change agent
            - APIs and Products review
            - Ownership of the different Agile ceremonies as Scrum Master
            - Main gateway between development and business
            - Contact point to stakeholders

            The working environement was including product management tool such as Jira, Confluence and Jira Service Management as well as tech. stack such as python, flutter, bitbucket for code repositories and version control.
            Our services are deployed and stored in the cloud.

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
            Part of the electrical powerdrive business unit within an Automotive Tier 1 supplier, I was in charge of the whole SW implementation, quality, testing and delivery.
            Working at first in a pure waterfall approach including the need to drive and lead different produt management aspect such as change management, commiunication management or configuration management.

            During this period I have also ensured and managed the migration to a hybrid methodology for our SW branch, creating different iterations, collecting lesson's learned and building sprints demos/reports
            """
        )

# ---- SKILLS----
with st.container():
    st.write("---")
    st.header("My Technical skills & knowledge")
    st.write("##")
    left_skills, right_skills = st.columns((1, 2))
    with left_skills:
        st.write(
            """
            :iphone: Mobile Development:
            - Flutter cross platform
            - Native iOS and Android SDK
            - Application deployment, release note and publication on stores

            :computer: Software Development:
            - Backend with python knowledge and expertise
            - APIs with python and fastAPI, postman test
            - Data Science with Python
            """
        )
    with right_skills:
        st.write(
            """
            :cloud: Infra / Devops:
            - Digital Ocean
            - PostgreSQL and MongoDB
            - Docker / k8s

            :bar_chart: Date Science:
            - Python libraries (numpy, pandas, matplotlib)
            - Reporting via Jupuyter Notebook

            """
        )

# ---- HOBBIES----
with st.container():
    st.write("---")
    st.header("My Hobbies")
    st.write("##")
    left_hobbies, right_hobbies= st.columns((1,2))
    with left_hobbies:
        st.write(
            """
            :soccer: Football: Club member from 5 years old to 25 years old

            :chess_pawn: Chess: Passionate and online players

            :snow_capped_mountain: Mountain Lover: Hiking, Skiing, enjoying mountains view in all seasons

            :runner: Trails : Running in wild places (forest, mountains)

            """
        )
    with right_hobbies:
        st.empty()

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

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
