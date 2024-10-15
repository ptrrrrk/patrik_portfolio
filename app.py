import base64
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Set up the page layout and title
st.set_page_config(page_title="Keszőcze Patrik", layout="wide", page_icon=":small_orange_diamond:")

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
            object-position: top;  
        }}
        </style>
        <img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" class="profile-pic">
        """,
        unsafe_allow_html=True
    )

# Add circular profile picture in the sidebar
add_profile_picture(r"profile_picture.jpg")

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
    with open(r"Keszőcze Patrik CV.pdf", "rb") as file:
        btn = st.download_button(label="Download Resume", data=file, file_name="Resume.pdf", mime="application/pdf")

# Navigation Menu
selected = option_menu(None, ["Projects", "Experience", "Education"],
                       icons=['kanban', 'briefcase', 'book', 'envelope'],
                       menu_icon="cast", default_index=0, orientation="horizontal",
                       styles={
                           "nav-link": {"--hover-color": "#d76d77"}
                       })

# Projects Section
if selected == "Projects":
    st.title("Projects")
    st.markdown("#### [Armed Conflicts in Israel and Palestine 2016-2024 - Interactive Data Visualization Project](https://israel-palestine-armed.streamlit.app/)")
    st.write(""" 
    For this project, I utilized curated data from ACLED and employed Python libraries such as Streamlit, Pandas, Plotly, 
    and Seaborn. Users can adjust the filters on the left side to observe changes in both the map and the diagram. The source 
    code is available on my GitHub page. This project is still in progress, as my long-term objective is to create a valuable 
    tool that anyone can use to explore this complex and sensitive topic, irrespective of political perspectives. Please note 
    that this work is entirely personal and not affiliated with my current or previous employers.
    """)
    st.write(""" More projects coming soon""")

# Experience Section
if selected == "Experience":
    st.title("Experience")

    # UNHCR Experience
    st.subheader("Finance Clerk, Administrative Support Assistant – UNHCR, Stabilization Team")
    st.write("Budapest // September 2023 - Present")
    st.write(""" I am a member of the Stabilization team at UNHCR working with PROMS. My responsibilities include overseeing PFRs from 
    their inception to budget revisions and preparing them for execution through Oracle's executable files. 
    I resolve unexpected issues quickly, helping streamline the process. Additionally, I am well-versed in manual 
    invoice creation procedures to support financial activities. I am part of this team since Cloud ERP go-live.
    """)

    # Data Analyst Trainee
    st.subheader("Data Analyst Trainee – ELTE TinLab")
    st.write("Budapest // April 2023 – June 2023")
    st.write(""" - Data Analysis using SPSS, Excel, and PowerBI
    - Reducing sampling errors
    - Report writing, data visualization
    - Tackling statistical methodological problems
    """)

    # College Manager, Secretary
    st.subheader("College Manager Secretary – College For Advanced Social Science")
    st.write("Budapest // September 2022 - August 2023")
    st.write(""" - Preparing and monitoring yearly budget
    - Tender writing
    - Administrative tasks
    - Coordinating the operative teams
    """)

    # Game Master
    st.subheader("Game Master – Időcsapda Escaperoom")
    st.write("Budapest // September 2019 – July 2023")
    st.write(""" - Conducting games, team building events
    - Online invoice processing
    - Developing dashboard about monthly incomes
    """)

# Education Section
if selected == "Education":
    st.title("Education")
    st.write(""" ### Eötvös Lóránd University, Sociology BSc, 2019-2023
    - Statistics, Data visualization, Hypothesis testing
    - Quantitative and Qualitative academic research
    - Political economy
    - Urban Sociology
    """)
    st.write(""" ### College for Advanced Social Science, 2019-2022
    - Macroeconomics
    - Data Analytics
    - Economics of sustainability
    - Academic Research
    """)
