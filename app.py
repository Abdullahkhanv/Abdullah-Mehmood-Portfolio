import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Abdullah Mehmood | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------- CUSTOM CSS FOR NAVBAR, HERO, & ANIMATIONS ----------------

st.markdown(
    """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;700&family=Poppins:wght@300;400;600;700&display=swap');

    /* Overall Theme */
    .stApp {
        background-color: #0b0b0b !important;
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    /* Hide Streamlit Header & Footer Padding */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    .block-container {
        padding-top: 5rem !important;
        padding-bottom: 3rem !important;
    }

    /* --- TOP NAVIGATION BAR --- */
    .custom-navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 70px;
        background: rgba(11, 11, 11, 0.95);
        backdrop-filter: blur(10px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 5%;
        border-bottom: 1px solid #262626;
        z-index: 999999;
    }

    .nav-logo {
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        font-weight: 700;
        color: #d31820;
        letter-spacing: 1.5px;
    }

    .nav-links {
        display: flex;
        gap: 25px;
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .nav-links a {
        color: #a0a0a0;
        text-decoration: none;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: color 0.3s ease;
    }

    .nav-links a:hover {
        color: #ffffff;
    }

    /* --- HERO BACKGROUND "PORTFOLIO" TEXT --- */
    .hero-bg-wrapper {
        position: relative;
        text-align: center;
        margin-bottom: -120px;
        z-index: 0;
        pointer-events: none;
    }

    .hero-bg-text {
        font-family: 'Oswald', sans-serif;
        font-size: 14vw;
        color: #d31820;
        opacity: 0.18;
        font-weight: 700;
        letter-spacing: 4px;
        line-height: 0.8;
        margin: 0;
    }

    /* --- HERO TEXT & DETAILS --- */
    .greeting-text {
        font-style: italic;
        font-size: 22px;
        color: #a0a0a0;
        margin-bottom: 5px;
    }

    .hero-main-name {
        font-family: 'Oswald', sans-serif;
        font-size: 52px;
        line-height: 1.05;
        color: #ffffff;
        font-weight: 700;
        margin: 0 0 10px 0;
        letter-spacing: 1px;
    }

    .hero-role-tag {
        color: #d31820;
        font-weight: 700;
        letter-spacing: 1.5px;
        font-size: 13px;
        margin-bottom: 15px;
    }

    .hero-bio {
        color: #a0a0a0;
        font-size: 14px;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .hero-location {
        color: #ffffff;
        font-size: 13px;
        font-weight: 600;
    }

    .hero-location span {
        color: #d31820;
    }

    /* --- IMAGE FRAME --- */
    .profile-frame {
        background: #141414;
        border: 1px solid #262626;
        border-radius: 12px;
        height: 420px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #a0a0a0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        transition: transform 0.4s ease, border-color 0.4s ease;
    }

    .profile-frame:hover {
        transform: translateY(-5px);
        border-color: #d31820;
    }

    /* --- QUOTE BADGE --- */
    .floating-badge {
        background: rgba(20, 20, 20, 0.9);
        border: 1px solid #262626;
        padding: 10px 20px;
        border-radius: 20px;
        font-size: 12px;
        color: #a0a0a0;
        text-align: center;
        margin: 15px auto;
        width: max-content;
    }

    .floating-badge span {
        color: #d31820;
    }

    /* --- METRIC CARDS --- */
    div[data-testid="stMetric"] {
        background: #141414;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #262626;
        transition: all 0.4s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border-color: #d31820;
        box-shadow: 0 10px 25px rgba(211, 24, 32, 0.25);
    }

    /* --- BUTTON & LINK HOVER ANIMATIONS --- */
    div.stButton > button, div[data-testid="stLinkButton"] > a {
        background-color: #d31820 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        transition: all 0.3s ease-in-out !important;
    }

    div.stButton > button:hover, div[data-testid="stLinkButton"] > a:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0px 8px 20px rgba(211, 24, 32, 0.5) !important;
        background-color: #ff1f28 !important;
    }

    /* --- WORK EXPERIENCE BOX HOVER --- */
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

    /* --- SKILL PILLS --- */
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

    /* Pulsing Badge */
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

    <!-- FIXED TOP NAVBAR -->
    <div class="custom-navbar">
        <div class="nav-logo">ABDULLAH MEHMOOD</div>
        <ul class="nav-links">
            <li><a href="#home">HOME</a></li>
            <li><a href="#about">ABOUT</a></li>
            <li><a href="#projects">PROJECTS</a></li>
            <li><a href="#education">EDUCATION</a></li>
            <li><a href="#skills">SKILLS & EXP</a></li>
            <li><a href="#contact">CONTACT</a></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------- HERO SECTION ----------------

# Anchor target for navigation
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

# Giant Background Text
st.markdown(
    """
    <div class="hero-bg-wrapper">
        <h1 class="hero-bg-text">PORTFOLIO</h1>
    </div>
    """,
    unsafe_allow_html=True
)

col_left, col_center, col_right = st.columns([1.2, 1.1, 0.8])

with col_left:
    st.markdown(
        """
        <div id="about">
            <p class="greeting-text">Hi, I'm</p>
            <h1 class="hero-main-name">ABDULLAH<br>MEHMOOD</h1>
            <p class="hero-role-tag">BS IT STUDENT & AI TOOLS DEVELOPER</p>
            <p class="hero-bio">
                I'm an IT student who loves building things for the web. I recently took a short course on local e-commerce, giving me hands-on experience in online store setup and management. Always learning — currently deep into HTML, CSS, JS, Python, and generative AI to turn ideas into working projects.
            </p>
            <p class="hero-location"><span>📍</span> MULTAN CANTT, PAKISTAN</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_center:
    # Frame for image or placeholder
    st.markdown(
        """
        <div class="profile-frame">
            <div style="text-align:center;">
                <p style="font-size: 40px; margin:0;">👤</p>
                <p>Abdullah Mehmood</p>
            </div>
        </div>
        <div class="floating-badge">
            <span>🪄</span> Turning ideas into functional AI web apps.
        </div>
        """,
        unsafe_allow_html=True
    )

with col_right:
    st.write("")
    st.write("")
    st.metric("Live Streamlit Apps", "3+")
    st.metric("Current CGPA", "3.09")
    st.metric("BS IT Session", "2024-28")


# ---------------- PROJECTS SECTION ----------------

st.write("---")
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.header("⚡ Featured Projects")

projects = [
    {
        "name": "01. AI Research Paper Summarizer & Plagiarism Corrector",
        "tech": "Python | Streamlit | GPT API",
        "url": "https://ai-driven-research-paper-summarizer-plagiarism-corrector-9pdyf.streamlit.app/"
    },
    {
        "name": "02. AI Mentor For Learning Personalized Assistant",
        "tech": "Python | Streamlit | AI Chatbot",
        "url": "https://ai-mentor-for-learning-personalized-learning-assistant-odcr4p9.streamlit.app/"
    },
    {
        "name": "03. AI Code Reviewer & Bug Explainer",
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
st.markdown('<div id="education"></div>', unsafe_allow_html=True)

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
        *Govt Graduate College of Science Multan* (2021 - 2023)  

        ---  

        🎓 **Matric Science**  
        *FG Public School Multan Cantt* (2019 - 2021)  
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


# ---------------- SKILLS & WORK EXPERIENCE ----------------

st.write("---")
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)

col_s1, col_s2 = st.columns(2)

with col_s1:
    st.header("🛠️ Skills")
    skills_list = [
        "HTML5", "CSS3", "JavaScript", "Bootstrap", "React", 
        "Python", "SQL", "Git", "GitHub", "Figma", 
        "Prompt Engineering", "Digital Marketing", "E-Commerce Operations"
    ]
    badges_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills_list])
    st.markdown(badges_html, unsafe_allow_html=True)

with col_s2:
    st.header("💼 Work Experience")
    experience = [
        "Store Backup Associate - Sapphire (Jun 2025 - Jul 2025)",
        "Back Store Associate - Outfitters (Jul 2025 - Aug 2025)",
        "Front of House Staff - Al-Kaif Restaurant",
        "Self Employed Online Marketer - Freelance / E-Commerce"
    ]
    for exp in experience:
        st.info(exp)


# ---------------- CONTACT SECTION ----------------

st.write("---")
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.header("📫 Let's Work Together")

st.write(
    """
    Currently available for web development projects, AI tools, freelancing, and internship opportunities.
    """
)

st.markdown('<div class="status-badge">🟢 AVAILABLE FOR FREELANCE & INTERNSHIP</div>', unsafe_allow_html=True)

st.write(
    """
    📧 **Email:** abdullahmehmood2n4l@gmail.com  
    📞 **Phone:** 0326 7636648  
    📍 **Location:** Multan Cantt, Pakistan  
    """
)

st.caption("© 2026 Abdullah Mehmood. All Rights Reserved.")
