import streamlit as st


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Abdullah Mehmood | Portfolio",
    page_icon="💻",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

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


.navbar{

    background:#111;
    padding:20px;
    text-align:center;
    border-bottom:1px solid #262626;

}


.logo{

    font-size:32px;
    color:#d31820;
    font-weight:700;

}



.card{

background:#141414;
border:1px solid #262626;
padding:25px;
border-radius:12px;
margin:15px 0;

}


.card:hover{

border-color:#d31820;

}



.tag{

display:inline-block;
background:#1f1f1f;
padding:8px 15px;
margin:5px;
border-radius:20px;
font-size:13px;

}



.project-btn{

background:#d31820;
color:white;
padding:10px 18px;
border-radius:5px;
text-decoration:none;

}


.gray{

color:#aaa;

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
""", unsafe_allow_html=True)



# ---------------- HERO ----------------


left, right = st.columns([2,1])


with left:


    st.markdown("""
    
<h1 style="font-size:60px;">
Hi, I'm<br>
ABDULLAH MEHMOOD
</h1>


<h3 style="color:#d31820;">
BS IT STUDENT & AI TOOLS DEVELOPER
</h3>


<p class="gray">

I'm an IT student who loves building things for the web.
Currently learning HTML, CSS, JavaScript, Python and
Generative AI to create useful applications.

</p>


📍 MULTAN CANTT, PAKISTAN


""", unsafe_allow_html=True)



with right:


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

""", unsafe_allow_html=True)



# ---------------- PROJECTS ----------------


st.divider()


st.header("FEATURED PROJECTS")


projects=[

(
"AI Research Paper Summarizer & Plagiarism Corrector",
"Python | Streamlit | GPT API",
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


for title,tech,link in projects:


    st.markdown(f"""

<div class="card">


<h3>{title}</h3>


<p class="gray">

{tech}

</p>


<a class="project-btn" href="{link}" target="_blank">

LAUNCH LIVE APP

</a>


</div>


""", unsafe_allow_html=True)




# ---------------- EDUCATION ----------------


st.divider()


col1,col2 = st.columns(2)


with col1:


    st.header("EDUCATION")


    st.markdown("""

<div class="card">

<b>2024 - 2028</b>

<h3>
BS Information Technology
</h3>

University of Education Lahore
<br>
Multan Campus

<br><br>

<b>CGPA:</b> 3.09


</div>



<div class="card">

<h3>F.Sc Pre Engineering</h3>

Govt Graduate College of Science Multan


</div>



<div class="card">

<h3>Matric Science</h3>

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
            f'<span class="tag">{skill}</span>',
            unsafe_allow_html=True
        )



# ---------------- EXPERIENCE ----------------


st.divider()


st.header("WORK EXPERIENCE")


experience=[

"Store Backup Associate — Sapphire (Jun 2025 - Jul 2025)",

"Back Store Associate — Outfitters (Jul 2025 - Aug 2025)",

"Front of House Staff — Al-Kaif Restaurant",

"Self-Employed Online Marketer — Freelance / E-Commerce"

]


for item in experience:

    st.markdown(
    f"""
    <div class="card">
    {item}
    </div>
    """,
    unsafe_allow_html=True
    )



# ---------------- CONTACT ----------------


st.divider()


st.header("LET'S WORK TOGETHER")


st.write(
"""
Currently open for Web Development,
AI Projects, Freelancing and Internship opportunities.
"""
)


st.success(
"AVAILABLE FOR FREELANCE & INTERNSHIP"
)



st.markdown("""

📧 abdullahmehmood2n4l@gmail.com

<br>

📞 0326 7636648

<br>

📍 Multan Cantt, Pakistan

""", unsafe_allow_html=True)



st.markdown("""

<div class="footer">

© 2026 Abdullah Mehmood. All Rights Reserved.

</div>

""", unsafe_allow_html=True)
