from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Divya-Disha.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Divya Disha"
PAGE_ICON = ":wave:"
NAME = "Divya Disha"
DESCRIPTION = """
Computer Science Engineer.
"""
EMAIL = "divyadisha004@gmail.com"
SOCIAL_MEDIA = {
    "Instagram": "https://www.instagram.com/_divyadisha_/",
    "LinkedIn": "https://www.linkedin.com/in/divya-disha-ba30981b8/",
    "GitHub": "https://github.com/DivyaDisha004",
    "Leetcode": "https://leetcode.com/divyadisha/",
}
PROJECTS = {
    "🏆 FitMatch:Fashion Recommendation System": "https://github.com/DivyaDisha004/FitMatch_fashion_recommender",
    "🏆 Sign Language Prediction": "https://github.com/DivyaDisha004/Sign-Language-Synthesis",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


    # --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- QUALIFICATION ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- ✔️ B.Tech in CSE(7.4 cg-7th sem) Jaypee Institute of Information Technology,Sector 62 ,Noida (2020-2024)
- ✔️ Class 12th (CBSE)-94.8% Vishwa Bharti Public School,Noida (2018-2020)
- ✔️ Class 10th (CBSE)-96.2% Vishwa Bharti Public School,Noida  (2017-2018)

"""
)

# --- ACHIEVEMENTS ---
st.write('\n')
st.subheader("Achievements")
st.write(
    """
- ✔️Qualified for Google Step Internship 2022 Finalist.
- ✔️Google Cloud Program Member & Conducted two sessions as Google DSC coordinator.
- ✔️Qualified for TalentSprint WE by Google, offered 50% Scholarship
- ✔️Academic Excellence Award – Scholarship and Cash Prize - 2018
- ✔️Certificate of Merit from CBSE for scoring 100/100 in Sanskrit AISSCE exams.
"""
)


# --- RESPONSIBILITIES ---
st.write('\n')
st.subheader("Responsibilities")
st.write(
    """
- ✔️Technical Coordinator-GOOGLE DEVELOPERS STUDENT CLUB(GDSC,Noida)
- ✔️Student Council-Incharge of Cleanliness.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming Languages: C++/Python 
- 📊 Data Science: ML , NLP, Data Analysis
- 📚 Development: HTML,CSS,JavaScript,ASP.NET
- 🗄️ Databases: MySQL, MongoDB
"""
)

# --- SOFTSKILLS ---
st.write('\n')
st.subheader("Soft Skills")
st.write(
    """
      •	Problem Solving
      •	Leadership & Organisation - technical sessions , hackathons, youtube technical tutorials.
      •	Classical Dance
 
"""
)


# --- INTERNSHIPS ---
st.write('\n')
st.subheader("INTERNSHIPS AND EXPERIENCE")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Development Intern | PNB**")
st.write("06/2023 - 08/2023")
st.write(
    """
- ► Helped in designing and implentation of three feautures for the official website of PNB at their website managment firm-CyFutureworks
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Centre of Excellence in Education | JIIT Noida**")
st.write("06/2023 - 08/2023")
st.write(
    """
- ► Worked as an AI/ML Intern for Centre of Excellence in Education (COE) at JIIT Noida for Sign Language Prediction. 
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Science Intern | Twilearn**")
st.write("05/2023 - 06/2023")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
