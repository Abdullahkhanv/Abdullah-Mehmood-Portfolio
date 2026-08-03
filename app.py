import streamlit as st
import requests
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Abdullah Mehmood | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Helper function to load Lottie JSON from URL
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Load Lottie Animations
lottie_coder = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json")

# ---------------- CUSTOM CSS & ANIMATIONS ----------------

st.markdown(
    """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;700&family=Poppins:wght@300;400;600;700&display=swap');

    html {
        scroll-behavior: smooth;
    }

    /* Dark Theme Base */
    .stApp {
        background: #0b0b0b !important;
        color: white;
        font-family: 'Poppins', sans-serif;
        position: relative;
        overflow-x: hidden;
    }

    /* ---------- ANIMATED PARTICLE / GLOW BACKDROP (pure CSS) ---------- */
    .stApp::before {
        content: "";
        position: fixed;
        top: -20%;
        left: -10%;
        width: 60vw;
        height: 60vw;
        background: radial-gradient(circle, rgba(211,24,32,0.18) 0%, rgba(211,24,32,0) 70%);
        z-index: 0;
        pointer-events: none;
        animation: floatBlob 18s ease-in-out infinite alternate;
    }
    .stApp::after {
        content: "";
        position: fixed;
        bottom: -25%;
        right: -15%;
        width: 55vw;
        height: 55vw;
        background: radial-gradient(circle, rgba(211,24,32,0.12) 0%, rgba(211,24,32,0) 70%);
        z-index: 0;
        pointer-events: none;
        animation: floatBlob 22s ease-in-out infinite alternate-reverse;
    }
    @keyframes floatBlob {
        0%   { transform: translate(0, 0) scale(1); }
        50%  { transform: translate(4vw, 3vw) scale(1.08); }
        100% { transform: translate(-3vw, 5vw) scale(0.96); }
    }

    header[data-testid="stHeader"] { display: none !important; }

    .block-container {
        padding-top: 5.5rem !important;
        padding-bottom: 3rem !important;
        position: relative;
        z-index: 1;
    }

    /* ---------- ENTRANCE ANIMATIONS ---------- */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-40px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeInRight {
        from { opacity: 0; transform: translateX(40px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes popIn {
        0%   { opacity: 0; transform: scale(0.7); }
        70%  { transform: scale(1.05); }
        100% { opacity: 1; transform: scale(1); }
    }
    @keyframes gradientShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes blinkCursor {
        0%, 45% { border-color: #d31820; }
        50%, 100% { border-color: transparent; }
    }
    @keyframes typing {
        from { width: 0; }
        to   { width: 100%; }
    }
    @keyframes bounceIn {
        0%   { opacity: 0; transform: scale(0.3); }
        50%  { opacity: 1; transform: scale(1.08); }
        70%  { transform: scale(0.95); }
        100% { transform: scale(1); }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50%      { transform: translateY(-10px); }
    }
    @keyframes pulse {
        0%   { box-shadow: 0 0 0 0 rgba(211, 24, 32, 0.7); }
        70%  { box-shadow: 0 0 0 14px rgba(211, 24, 32, 0); }
        100% { box-shadow: 0 0 0 0 rgba(211, 24, 32, 0); }
    }
    @keyframes shimmer {
        0%   { background-position: -500px 0; }
        100% { background-position: 500px 0; }
    }

    .animate-fade-in { animation: fadeInUp 0.8s ease-out forwards; }

    /* Scroll-reveal targets: hidden until JS (below) marks them visible */
    .reveal {
        opacity: 0;
        transform: translateY(40px);
        transition: opacity 0.8s cubic-bezier(0.22, 1, 0.36, 1), transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .reveal.visible {
        opacity: 1;
        transform: translateY(0);
    }
    .reveal-left {
        opacity: 0;
        transform: translateX(-50px);
        transition: opacity 0.8s ease, transform 0.8s ease;
    }
    .reveal-left.visible { opacity: 1; transform: translateX(0); }
    .reveal-right {
        opacity: 0;
        transform: translateX(50px);
        transition: opacity 0.8s ease, transform 0.8s ease;
    }
    .reveal-right.visible { opacity: 1; transform: translateX(0); }

    /* Staggered children delays */
    .reveal:nth-of-type(1) { transition-delay: 0.05s; }
    .reveal:nth-of-type(2) { transition-delay: 0.15s; }
    .reveal:nth-of-type(3) { transition-delay: 0.25s; }
    .reveal:nth-of-type(4) { transition-delay: 0.35s; }

    /* ---------- TOP NAVIGATION BAR ---------- */
    .custom-navbar {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        height: 70px;
        background: rgba(11, 11, 11, 0.95);
        backdrop-filter: blur(12px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 5%;
        border-bottom: 1px solid #262626;
        z-index: 999999;
        animation: fadeInUp 0.6s ease-out;
    }

    .nav-logo {
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        font-weight: 700;
        background: linear-gradient(90deg, #d31820, #ff5b5b, #d31820);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 1.5px;
        animation: gradientShift 4s linear infinite;
    }

    .nav-links { display: flex; gap: 25px; list-style: none; margin: 0; padding: 0; }

    .nav-links a {
        color: #a0a0a0;
        text-decoration: none;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        position: relative;
        padding: 5px 0;
        transition: all 0.3s ease;
    }
    .nav-links a::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0;
        width: 0%;
        height: 2px;
        background-color: #d31820;
        transition: width 0.3s ease;
    }
    .nav-links a:hover { color: #ffffff; transform: translateY(-2px); }
    .nav-links a:hover::after { width: 100%; }

    /* ---------- HERO BACKGROUND WATERMARK ---------- */
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
        background: linear-gradient(90deg, #d31820, #4a0508, #d31820);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        opacity: 0.18;
        font-weight: 700;
        letter-spacing: 4px;
        line-height: 0.8;
        margin: 0;
        animation: fadeInUp 1s ease-out, gradientShift 6s linear infinite;
    }

    /* ---------- HERO DETAILS ---------- */
    .greeting-text {
        font-style: italic;
        font-size: 22px;
        color: #a0a0a0;
        margin-bottom: 5px;
        animation: fadeInLeft 0.7s ease-out;
    }

    .hero-main-name {
        font-family: 'Oswald', sans-serif;
        font-size: 52px;
        line-height: 1.05;
        color: #ffffff;
        font-weight: 700;
        margin: 0 0 10px 0;
        letter-spacing: 1px;
        animation: fadeInLeft 0.9s ease-out;
    }

    /* Typewriter role tag */
    .hero-role-tag {
        color: #d31820;
        font-weight: 700;
        letter-spacing: 1.5px;
        font-size: 13px;
        margin-bottom: 15px;
        display: inline-block;
        overflow: hidden;
        white-space: nowrap;
        border-right: 2px solid #d31820;
        width: 0;
        animation: typing 2.5s steps(34, end) 0.8s forwards, blinkCursor 0.75s step-end infinite;
    }

    .hero-bio {
        color: #a0a0a0;
        font-size: 14px;
        line-height: 1.6;
        margin-bottom: 20px;
        animation: fadeInUp 1.1s ease-out;
    }

    .hero-location {
        color: #ffffff;
        font-size: 13px;
        font-weight: 600;
        animation: fadeInUp 1.3s ease-out;
    }
    .hero-location span {
        color: #d31820;
        display: inline-block;
        animation: float 2.4s ease-in-out infinite;
    }

    /* ---------- FLOATING BADGE ---------- */
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
        transition: all 0.3s ease;
        animation: float 3.2s ease-in-out infinite;
    }
    .floating-badge:hover {
        border-color: #d31820;
        transform: translateY(-6px) scale(1.04);
        box-shadow: 0 8px 20px rgba(211, 24, 32, 0.25);
    }
    .floating-badge span { color: #d31820; }

    /* ---------- METRIC CARDS ---------- */
    div[data-testid="stMetric"] {
        background: #141414;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #262626;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: popIn 0.7s ease-out backwards;
    }
    div[data-testid="stMetric"]:nth-of-type(1) { animation-delay: 0.2s; }
    div[data-testid="stMetric"]:nth-of-type(2) { animation-delay: 0.35s; }
    div[data-testid="stMetric"]:nth-of-type(3) { animation-delay: 0.5s; }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-8px) scale(1.03);
        border-color: #d31820;
        box-shadow: 0 10px 25px rgba(211, 24, 32, 0.3);
    }

    /* ---------- BUTTONS ---------- */
    div.stButton > button, div[data-testid="stLinkButton"] > a {
        background-color: #d31820 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        transition: all 0.3s ease-in-out !important;
        position: relative;
        overflow: hidden;
    }
    div.stButton > button:hover, div[data-testid="stLinkButton"] > a:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0px 10px 25px rgba(211, 24, 32, 0.6) !important;
        background-color: #ff1f28 !important;
    }
    div.stButton > button:active, div[data-testid="stLinkButton"] > a:active {
        transform: translateY(-1px) scale(0.98);
    }

    /* ---------- SECTION HEADERS ---------- */
    h1, h2, h3 {
        animation: fadeInUp 0.7s ease-out;
    }

    /* ---------- WORK EXPERIENCE BOXES ---------- */
    div[data-baseweb="notification"] {
        background-color: #141414 !important;
        border-left: 4px solid #d31820 !important;
        color: white !important;
        transition: all 0.3s ease-in-out;
        animation: fadeInRight 0.6s ease-out backwards;
    }
    div[data-baseweb="notification"]:nth-of-type(1) { animation-delay: 0.1s; }
    div[data-baseweb="notification"]:nth-of-type(2) { animation-delay: 0.2s; }
    div[data-baseweb="notification"]:nth-of-type(3) { animation-delay: 0.3s; }
    div[data-baseweb="notification"]:nth-of-type(4) { animation-delay: 0.4s; }
    div[data-baseweb="notification"]:hover {
        transform: translateX(10px) scale(1.01);
        box-shadow: 0 5px 20px rgba(211, 24, 32, 0.3);
    }

    /* ---------- SKILL PILLS ---------- */
    .skill-tag {
        background: #1f1f1f;
        color: #e0e0e0;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        display: inline-block;
        border: 1px solid #333;
        font-size: 13px;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: bounceIn 0.5s ease-out backwards;
    }
    .skill-tag:nth-of-type(3n+1)  { animation-delay: 0.05s; }
    .skill-tag:nth-of-type(3n+2)  { animation-delay: 0.15s; }
    .skill-tag:nth-of-type(3n+3)  { animation-delay: 0.25s; }
    .skill-tag:hover {
        background: #d31820;
        color: white;
        border-color: #d31820;
        transform: translateY(-3px) scale(1.1);
        box-shadow: 0 5px 15px rgba(211, 24, 32, 0.4);
        cursor: pointer;
    }

    /* ---------- PROJECT CARDS ---------- */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        transition: transform 0.35s ease, box-shadow 0.35s ease;
    }

    /* ---------- PULSING STATUS BADGE ---------- */
    .status-badge {
        background-color: #d31820;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: bold;
        display: inline-block;
        animation: pulse 2s infinite, fadeInUp 0.6s ease-out;
        text-align: center;
        margin: 15px 0;
        transition: transform 0.3s ease;
    }
    .status-badge:hover { transform: scale(1.05); }

    /* ---------- PROGRESS / SKILL BARS (shimmer) ---------- */
    .bar-track {
        background: #1a1a1a;
        border-radius: 8px;
        overflow: hidden;
        height: 10px;
        margin: 4px 0 14px 0;
        border: 1px solid #262626;
    }
    .bar-fill {
        height: 100%;
        border-radius: 8px;
        background: linear-gradient(90deg, #d31820, #ff5b5b, #d31820);
        background-size: 300px 100%;
        animation: shimmer 2.5s linear infinite, growBar 1.4s ease-out forwards;
        width: 0%;
    }
    @keyframes growBar { to { width: var(--target-width); } }

    /* Scrollbar flair */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #0b0b0b; }
    ::-webkit-scrollbar-thumb { background: #d31820; border-radius: 4px; }
    </style>

    <!-- NAVIGATION BAR -->
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

# ---------------- SCROLL-REVEAL ENGINE (JS via component, targets parent doc) ----------------
# This finds every element with class "reveal" / "reveal-left" / "reveal-right"
# in the *main* Streamlit document and toggles "visible" as it enters the viewport.
components.html(
    """
    <script>
    const doc = window.parent.document;
    function initReveal() {
        const targets = doc.querySelectorAll('.reveal, .reveal-left, .reveal-right');
        if (!targets.length) return;
        const io = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.classList.add('visible');
                }
            });
        }, { threshold: 0.15 });
        targets.forEach(t => io.observe(t));
    }
    // Streamlit re-renders async, so retry briefly until elements exist
    let tries = 0;
    const interval = setInterval(() => {
        const found = doc.querySelectorAll('.reveal, .reveal-left, .reveal-right').length;
        if (found > 0 || tries > 40) {
            initReveal();
            clearInterval(interval);
        }
        tries++;
    }, 150);
    </script>
    """,
    height=0,
)

# ---------------- HERO SECTION ----------------

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

# Giant Watermark Text
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
        <div id="about" class="animate-fade-in">
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
    if lottie_coder:
        st_lottie(lottie_coder, height=350, key="coder_animation")
    else:
        st.markdown("<div style='height:350px;'></div>", unsafe_allow_html=True)

    st.markdown(
        """
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
    st.markdown('<div class="reveal">', unsafe_allow_html=True)
    with st.container(border=True):
        st.subheader(project["name"])
        st.caption(f"🛠️ **Tech:** {project['tech']}")
        st.link_button("LAUNCH LIVE APP ↗", project["url"])
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")


# ---------------- EDUCATION SECTION ----------------

st.write("---")
st.markdown('<div id="education"></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.header("🎓 Education")
    st.markdown('<div class="reveal-left">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.header("📜 Certifications & Training")
    st.markdown('<div class="reveal-right">', unsafe_allow_html=True)
    st.markdown(
        """
        • **E-Commerce Certificate** — ACE College / NAVTTC (2024)
        • **Youth Internship Certificate** — Friends of Police (2025)
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)


# ---------------- SKILLS & EXPERIENCE SECTION ----------------

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

    st.write("")
    st.caption("Core proficiency")
    proficiency = [("HTML / CSS", 90), ("Python", 80), ("JavaScript", 70), ("SQL", 65)]
    bars_html = "".join(
        f"""
        <div>
          <span style="font-size:12px;color:#a0a0a0;">{name}</span>
          <div class="bar-track">
            <div class="bar-fill" style="--target-width:{pct}%;"></div>
          </div>
        </div>
        """
        for name, pct in proficiency
    )
    st.markdown(bars_html, unsafe_allow_html=True)

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

col_c1, col_c2 = st.columns([1.5, 1])

with col_c1:
    st.header("📫 Let's Work Together")
    st.markdown('<div class="reveal">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

with col_c2:
    if lottie_contact:
        st_lottie(lottie_contact, height=220, key="contact_animation")

st.caption("© 2026 Abdullah Mehmood. All Rights Reserved.")
