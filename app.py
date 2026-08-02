import streamlit as st


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Abdullah Mehmood | Portfolio",
    page_icon="💻",
    layout="wide"
)


# ---------------- STYLE ----------------

st.markdown(
    """
    <style>
    
    .stApp {
        background-color: #0b0b0b;
        color: white;
    }

    h1,h2,h3 {
        color: white;
    }

    .main-title {
        color:#d31820;
        font-size:60px;
        font-weight:800;
    }

    .card {
        background:#141414;
        padding:20px;
        border-radius:15px;
        border:1px solid #333;
    }

    .tag {
        background:#222;
        padding:8px 15px;
        border-radius:20px;
        margin:4px;
        display:inline-block;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- HEADER ----------------

st.title("ABDULLAH MEHMOOD")

st.subheader(
    "BS IT STUDENT & AI TOOLS DEVELOPER"
)

st.write("---")


# ---------------- ABOUT ----------------


col1, col2 = st.columns([2,1])


with col1:

    st.markdown(
        """
        ## Hi, I'm Abdullah Mehmood

        I am an Information Technology student who loves
        building web applications and AI-powered tools.

        Currently learning:

        - HTML
        - CSS
        - JavaScript
        - Python
        - Generative AI

        Location:

        📍 Multan Cantt, Pakistan

        """
    )


with col2:

    st.metric(
        "Live Streamlit Apps",
        "3+"
    )

    st.metric(
        "Current CGPA",
        "3.09"
    )

    st.metric(
        "BS IT Session",
        "2024-2028"
    )



# ---------------- PROJECTS ----------------


st.write("---")

st.header("Featured Projects")


projects = [

{
"name":"AI Research Paper Summarizer & Plagiarism Corrector",
"tech":"Python | Streamlit | GPT API",
"url":"https://ai-driven-research-paper-summarizer-plagiarism-corrector-9pdyf.streamlit.app/"
},


{
"name":"AI Mentor For Learning Personalized Assistant",
"tech":"Python | Streamlit | AI Chatbot",
"url":"https://ai-mentor-for-learning-personalized-learning-assistant-odcr4p9.streamlit.app/"
},


{
"name":"AI Code Reviewer & Bug Explainer",
"tech":"Python | Streamlit | LLM",
"url":"https://ai-powered-code-reviewer-bug-explainer-uus4oprxmhrasquzwbqwzb.streamlit.app/"
}

]


for project in projects:

    with st.container():

        st.subheader(project["name"])

        st.write(project["tech"])

        st.link_button(
            "Launch Live App",
            project["url"]
        )

        st.write("")



# ---------------- EDUCATION ----------------


st.write("---")

col1,col2 = st.columns(2)



with col1:

    st.header("Education")

    st.write(
        """
        🎓 BS Information Technology

        University of Education Lahore  
        Multan Campus

        Duration:
        2024 - 2028

        CGPA:
        3.09


        🎓 F.Sc Pre Engineering

        Govt Graduate College of Science Multan


        🎓 Matric Science

        FG Public School Multan Cantt
        """
    )



with col2:

    st.header("Skills")


    skills = [

    "HTML5",
    "CSS3",
    "JavaScript",
    "Bootstrap",
    "React",
    "Python",
    "SQL",
    "Git",
    "GitHub",
    "Figma",
    "Prompt Engineering",
    "Digital Marketing",
    "E-Commerce"

    ]


    for skill in skills:

        st.write(
            "✅ " + skill
        )



# ---------------- EXPERIENCE ----------------


st.write("---")

st.header("Work Experience")


experience = [

"Store Backup Associate - Sapphire (Jun 2025 - Jul 2025)",

"Back Store Associate - Outfitters (Jul 2025 - Aug 2025)",

"Front of House Staff - Al-Kaif Restaurant",

"Self Employed Online Marketer - Freelance / E-Commerce"

]


for exp in experience:

    st.info(exp)



# ---------------- CONTACT ----------------


st.write("---")

st.header("Let's Work Together")


st.write(
"""
Currently available for:

- Web Development Projects
- AI Applications
- Freelancing
- Internship Opportunities
"""
)


st.success(
"AVAILABLE FOR FREELANCE & INTERNSHIP"
)


st.write(
"""
📧 Email:
abdullahmehmood2n4l@gmail.com


📞 Phone:
0326 7636648


📍 Location:
Multan Cantt, Pakistan
"""
)


st.caption(
"© 2026 Abdullah Mehmood. All Rights Reserved."
)
