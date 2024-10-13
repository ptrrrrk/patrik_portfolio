import base64
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Set up the page layout and title
st.set_page_config(page_title="Keszőcze Patrik", layout="wide")

# Function to create a circular image and keep it in the top-left corner
def add_profile_picture(image_path):
    image = Image.open(image_path)
    st.sidebar.markdown(
        f"""
        <style>
        .profile-pic {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
        }}
        </style>
        <img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" class="profile-pic">
        """,
        unsafe_allow_html=True
    )

# Add circular profile picture in the sidebar
add_profile_picture(r"D:\Data Science\Projects\StreamLit_Portfolio\DSC06681.png")

# Sidebar - About Section
with st.sidebar:
    st.write("### About Me")
    st.write("""Hi, I'm Patrik, a data science enthusiast with a passion for solving problems 
    through data. I have experience in data analysis, visualization, and automation. 
    I am currently working at UNHCR's Stabilization Team.
    """)
    st.markdown("[LinkedIn](https://www.linkedin.com/in/patrik-kesz%C5%91cze-32889a24b/)")
    st.markdown("[GitHub](https://github.com/ptrrrrk)")
    st.markdown("[Kaggle](https://www.kaggle.com/patrikkeszcze)")

    # Download Resume Button
    with open(r"D:\Data Science\Projects\StreamLit_Portfolio\Keszőcze Patrik CV.pdf", "rb") as file:
        btn = st.download_button(label="Download Resume", data=file, file_name="Resume.pdf", mime="application/pdf")

# Navigation Menu
selected = option_menu(None, ["Projects", "Experience", "Education", "Contact"],
                       icons=['kanban', 'briefcase', 'book', 'envelope'],
                       menu_icon="cast", default_index=0, orientation="horizontal",
                       styles={
                           "nav-link": {"--hover-color": "#d76d77"}
                       })

# Projects Section
if selected == "Projects":
    st.title("Projects")
    st.write("""
    ### Project 1: 
    - 
    - 
    ### Project 2: 
    - 
    -
    ### Project 3: Sales Analysis for XYZ Company
    - 
    -
    """)

# Experience Section
if selected == "Experience":
    st.title("Experience")

    # UNHCR Experience
    st.subheader("ADMINISTRATIVE SUPPORT ASSISTANT – UNHCR, STABILISATION TEAM")
    st.write("Budapest // GSC1 // September 2023 - Present")
    st.write("""
    I am a member of the Stabilization team at UNHCR working with PROMS. My responsibilities include overseeing PFRs from 
    their inception to budget revisions and preparing them for execution through Oracle's executable files. 
    I resolve unexpected issues quickly, helping streamline the process. Additionally, I am well-versed in manual 
    invoice creation procedures to support financial activities.
    """)

    # Data Analyst Trainee
    st.subheader("DATA ANALYST TRAINEE – ELTE TinLab")
    st.write("Budapest // April 2023 – June 2023")
    st.write("""
    - Data Analysis using SPSS, Excel, and PowerBI
    - Reducing sampling errors
    - Report writing, data visualization
    - Tackling statistical methodological problems
    """)

    # Collage Manager, Secretary
    st.subheader("COLLAGE MANAGER, SECRETARY – Társadalomelméleti Kollégium")
    st.write("Budapest // September 2022 - August 2023")
    st.write("""
    - Preparing and monitoring yearly budget
    - Tender writing
    - Administrative tasks
    - Coordinating the operative teams
    """)

    # Game Master
    st.subheader("GAME MASTER – Időcsapda Escaperoom")
    st.write("Budapest // September 2019 – July 2023")
    st.write("""
    - Conducting games, team building events
    - Online invoice processing
    - Developing dashboard about monthly income
    """)

# Education Section
if selected == "Education":
    st.title("Education")
    st.write("""
    ### Eötvös Lóránd University, Sociology Bsc, 2019-2023
    - Statistics, Data visualization 
    - Political economy
    - Urban Sociology
    """)
    st.write("""
        ### Collage for Advanced Social Science, 2019-2022
        - Macroeconomics
        - Economics of sustainability
        - Academic Research
        """)

# Contact Section
if selected == "Contact":
    st.title("Contact Me")
    contact_form = """
    <form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
