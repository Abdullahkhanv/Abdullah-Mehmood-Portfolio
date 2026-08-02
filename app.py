import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Abdullah Mehmood | Portfolio",
    page_icon="💻",
    layout="wide"
)


# ---------------- CUSTOM ANIMATIONS & STYLES (CSS) ----------------

st.markdown(
    """
    <style>
    /* Dark Theme Background */
    .stApp {
        background-color: #0b0b0b;
        color: white;
    }

    /* Typography */
    h1, h2, h3 {
        color: white !important;
        font-family: 'Poppins', sans-serif;
    }

    /* Red Accent Hover Buttons */
    div.stButton > button, div[data-testid="stLinkButton"] > a {
        background-color: #d31820 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        display: inline-block !important;
        transition: all 0.3s ease-in-out !important;
    }

    div.stButton > button:hover, div[data-testid="stLinkButton"] > a:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0px 8px 20px rgba(211, 24, 32, 0.5) !important;
        background-color: #ff1f28 !important;
        color: white !important;
    }

    /* Animated Stat Metric Cards */
    div[data-testid="stMetric"] {
        background: #141414;
        padding: 15px 20px;
        border-radius: 12px;
        border: 1px solid #262626;
        transition: all 0.4s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border-color: #d31820;
        box-shadow: 0 10px 25px rgba(211, 24, 32, 0.2);
    }

    /* Animated Work Experience Info Boxes */
    div[data-baseweb="notification"] {
        background-color: #141414 !important;
        border-left: 4px solid #d31820 !important;
        color: white !important;
        transition: all 0.3s ease-in-out;
    }

    div[data-baseweb="notification"]:hover {
        transform: translateX(8px);
        box-shadow: 0 5px 15px rgba(211, 24, 32, 0.2);
    }

    /* Skill Tags Hover Effects */
    .skill-tag {
        background: #1f1f1f;
        color: #e0e0e0;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 4px;
        display: inline-block;
        border: 1px solid #333;
        font-size: 13px;
        transition: all 0.3s ease;
    }

    .skill-tag:hover {
        background: #d31820;
        color: white;
        border-color: #d31820;
        transform: scale(1.08);
        cursor: pointer;
    }

    /* Pulsing Glow Animation for Availability Badge */
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(211, 24, 32, 0.7); }
        70% { box-shadow: 0 0 0 12px rgba(211, 24, 32, 0); }
        100% { box-shadow: 0 0 0 0 rgba(211, 24, 32, 0); }
    }

    .status-badge {
        background-color: #d31820;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: bold;
        display: inline-block;
        animation: pulse 2s infinite;
        text-align: center;
        margin: 15px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- HEADER ----------------

st.title("ABDULLAH MEHMOOD")
st.subheader("BS IT STUDENT & AI TOOLS DEVELOPER")
st.write("---")


# ---------------- ABOUT ----------------

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## Hi, I'm Abdullah Mehmood 👋")
    st.write(
        "I am an Information Technology student who loves building "
        "functional web applications and AI-powered tools."
    )
    
    st.write("**Currently Learning & Tech Stack:**")
    
    # Interactive Skill Badges with Hover Animation
    skills_list = [
        "HTML5", "CSS3", "JavaScript", "Python", 
        "Generative AI", "Streamlit", "React", "SQL", 
        "Git", "GitHub", "Figma", "Prompt Engineering", 
        "Digital Marketing", "E-Commerce"
    ]
    badges_html = "".join([f'<span class="skill-tag">✅ {skill}</span>' for skill in skills_list])
    st.markdown(badges_html, unsafe_allow_html=True)

    st.markdown("<br>📍 **Location:** Multan Cantt, Pakistan", unsafe_allow_html=True)

with col2:
    st.metric("Live Streamlit Apps", "3+")
    st.metric("Current CGPA", "3.09")
    st.metric("BS IT Session", "2024-2028")


# ---------------- PROJECTS ----------------

st.write("---")
st.header("⚡ Featured Projects")

projects = [
    {
        "name": "AI Research Paper Summarizer & Plagiarism Corrector",
        "tech": "Python | Streamlit | GPT API",
        "url": "https://ai-driven-research-paper-summarizer-plagiarism-corrector-9pdyf.streamlit.app/"
    },
    {
        "name": "AI Mentor For Learning Personalized Assistant",
        "tech": "Python | Streamlit | AI Chatbot",
        "url": "https://ai-mentor-for-learning-personalized-learning-assistant-odcr4p9.streamlit.app/"
    },
    {
        "name": "AI Code Reviewer & Bug Explainer",
        "tech": "Python | Streamlit | LLM",
        "url": "https://ai-powered-code-reviewer-bug-explainer-uus4oprxmhrasquzwbqwzb.streamlit.app/"
    }
]

for project in projects:
    with st.container():
        st.subheader(project["name"])
        st.caption(f"🛠️ **Tech:** {project['tech']}")
        st.link_button("Launch Live App ↗", project["url"])
        st.write("")


# ---------------- EDUCATION & CERTIFICATIONS ----------------

st.write("---")
col1, col2 = st.columns(2)

with col1:
    st.header("🎓 Education")
    st.markdown(
        """
        🎓 **BS Information Technology**  
        *University of Education Lahore — Multan Campus*  
        • **Duration:** 2024 - 2028  
        • **CGPA:** 3.09  

        ---  

        🎓 **F.Sc Pre Engineering**  
        *Govt Graduate College of Science Multan*  

        ---  

        🎓 **Matric Science**  
        *FG Public School Multan Cantt*  
        """
    )

with col2:
    st.header("📜 Certifications & Training")
    st.markdown(
        """
        • **E-Commerce Certificate** — ACE College / NAVTTC (2024)  
        • **Youth Internship Certificate** — Friends of Police (2025)  
        """
    )


# ---------------- EXPERIENCE ----------------

st.write("---")
st.header("💼 Work Experience")

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
st.header("📫 Let's Work Together")

st.write(
    """
    Currently available for:
    - Web Development Projects
    - AI Applications
    - Freelancing
    - Internship Opportunities
    """
)

# Pulsing Glowing Badge Animation
st.markdown('<div class="status-badge">🟢 AVAILABLE FOR FREELANCE & INTERNSHIP</div>', unsafe_allow_html=True)

st.write(
    """
    📧 **Email:** abdullahmehmood2n4l@gmail.com  
    📞 **Phone:** 0326 7636648  
    📍 **Location:** Multan Cantt, Pakistan  
    """
)

st.caption("© 2026 Abdullah Mehmood. All Rights Reserved.")
