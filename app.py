import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Abdullah Mehmood | Portfolio",
    page_icon="💻",
    layout="wide"
)


# ---------------- CSS ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;700&family=Poppins:wght@300;400;600;700&display=swap');


*{
    font-family:'Poppins',sans-serif;
}


.stApp{
    background:#0b0b0b;
    color:white;
}


h1,h2,h3,h4{
    font-family:'Oswald',sans-serif;
}


/* Navbar */
.navbar{
    background:#111;
    padding:20px;
    border-bottom:1px solid #262626;
    text-align:center;
}


.logo{
    font-size:30px;
    font-weight:700;
    color:#d31820;
}
<p class="greeting">Hi, I&apos;m</p>

/* Hero */

.hero-title{
    font-size:70px;
    font-weight:700;
    color:#d31820;
}


.hero-tag{
    color:#d31820;
    font-weight:600;
}


.card{

    background:#141414;
    border:1px solid #262626;
    padding:25px;
    border-radius:12px;
    margin-bottom:20px;

}


.card:hover{
    border-color:#d31820;
}


.badge{

background:#1f1f1f;
padding:8px 15px;
border-radius:20px;
display:inline-block;
margin:5px;
font-size:13px;

}


.project-link{

background:#d31820;
padding:10px 20px;
border-radius:5px;
color:white;
text-decoration:none;

}


.small{
color:#a0a0a0;
font-size:14px;
}



.footer{

text-align:center;
padding:30px;
border-top:1px solid #262626;
color:#aaa;

}


</style>

""", unsafe_allow_html=True)



# ---------------- HEADER ----------------

st.markdown("""
<div class="navbar">

<div class="logo">
ABDULLAH MEHMOOD
</div>

</div>
""",unsafe_allow_html=True)



# ---------------- HERO ----------------


col1,col2,col3 = st.columns([1,1.2,0.8])


with col1:

    st.markdown("""
    <h1 class="hero-title">
    Hi, I'm<br>
    ABDULLAH
    </h1>


    <h3 class="hero-tag">
    BS IT STUDENT & AI TOOLS DEVELOPER
    </h3>


    <p class="small">

    I'm an IT student who loves building things for the web.
    Currently learning HTML, CSS, JS, Python and Generative AI
    to convert ideas into working applications.

    </p>


    📍 MULTAN CANTT, PAKISTAN

    """,unsafe_allow_html=True)



with col2:

    st.image(
        "assets/Abdullah.jpeg",
        width=350
    )


    st.info(
        "✨ Turning ideas into functional AI web apps."
    )



with col3:


    st.markdown("""
    
<div class="card">

<h2>3+</h2>
<p>LIVE STREAMLIT APPS</p>

</div>


<div class="card">

<h2>3.09</h2>
<p>CURRENT CGPA</p>

</div>


<div class="card">

<h2>2024-28</h2>
<p>BS IT SESSION</p>

</div>


""",unsafe_allow_html=True)




# ---------------- PROJECTS ----------------


st.divider()

st.header("FEATURED PROJECTS")


projects=[


(
"AI Research Paper Summarizer & Plagiarism Corrector",
"Python | Streamlit | GPT-4 API",
"https://ai-driven-research-paper-summarizer-plagiarism-corrector-9pdyf.streamlit.app/"
),


(
"AI Mentor for Learning Personalized Assistant",
"Python | Streamlit | AI Chatbot",
"https://ai-mentor-for-learning-personalized-learning-assistant-odcr4p9.streamlit.app/"
),


(
"AI Code Reviewer & Bug Explainer",
"Python | Streamlit | LLM",
"https://ai-powered-code-reviewer-bug-explainer-uus4oprxmhrasquzwbqwzb.streamlit.app/"
)

]



for name,tech,link in projects:

    st.markdown(f"""

<div class="card">

<h3>{name}</h3>

<p class="small">

{tech}

</p>


<a class="project-link" href="{link}" target="_blank">

LAUNCH LIVE APP

</a>

</div>

""",unsafe_allow_html=True)




# ---------------- EDUCATION ----------------


st.divider()

col1,col2=st.columns(2)



with col1:

    st.header("EDUCATION")


    st.markdown("""
<div class="card">

<b>2024-2028</b>

<h4>
BS Information Technology
</h4>

University of Education Lahore
Multan Campus

<br><br>

<b>CGPA:</b> 3.09


</div>


<div class="card">

<h4>F.Sc Pre Engineering</h4>

Govt Graduate College of Science Multan


</div>


<div class="card">

<h4>Matric Science</h4>

FG Public School Multan Cantt


</div>

""",unsafe_allow_html=True)



with col2:


    st.header("SKILLS")


    skills=[
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

        st.markdown(
        f'<span class="badge">{skill}</span>',
        unsafe_allow_html=True
        )




# ---------------- CONTACT ----------------


st.divider()


st.header("LET'S WORK TOGETHER")


st.write(
"""
Currently open for Web Development,
AI projects, Freelancing and Internship opportunities.
"""
)


st.success(
"AVAILABLE FOR FREELANCE & INTERNSHIP"
)


st.markdown("""
📧 abdullahmehmood2n4l@gmail.com

📞 0326 7636648

📍 Multan Cantt Pakistan

""")


st.markdown("""

<div class="footer">

© 2026 Abdullah Mehmood. All Rights Reserved.

</div>

""",unsafe_allow_html=True)
