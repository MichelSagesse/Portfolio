import streamlit as st
from PIL import Image, ImageDraw
import base64
from io import BytesIO
import os

# Configuration de base
st.set_page_config(
    page_title="Portfolio Michel Sagesse",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Données du portfolio (texte simple sans caractères spéciaux)
PORTFOLIO_DATA = {
    "name": "MICHEL SAGESSE KOLIE",
    "title": "Data Scientist AI Big Data Engineer",
    "email": "michelsagesse16@gmail.com",
    "phone": "212710871157",
    "address": "Tetouan Morocco",
    "linkedin": "https://www.linkedin.com/in/michel-sagesse-kolie-9313a9281/",
    "github": "https://github.com/MichelSagesse",
    "about": "Passionate about AI and Data Science I transform data into innovative solutions",
    
    "skills": {
        "Python": 95,
        "SQL": 90,
        "R": 80,
        "TensorFlow": 85,
        "PyTorch": 80,
        "Scikit learn": 90,
        "Pandas": 95,
        "NumPy": 90,
        "Hadoop": 75,
        "Spark": 80,
        "MySQL": 90,
        "PostgreSQL": 85,
        "MongoDB": 80
    },
    
    "projects": [
        {
            "title": "Heart Rate Prediction and Patient Monitoring System",
            "description": "XGBoost algorithm estimates heart rate by filtering arm movement interferences through PPG and accelerometer signal comparison",
            "technologies": "Python XGBoost PCA Sensors Pandas",
            "category": "AI ML"
        },
        {
            "title": "Movie Recommendation System",
            "description": "Hybrid recommendation engine combining collaborative filtering and content based approaches",
            "technologies": "Collaborative Filtering Content Based Pandas Scikit learn",
            "category": "Recommendation Systems"
        }
    ],
    
    "experience": [
        {
            "title": "AI NLP Intern",
            "company": "Smart Automation Technologies",
            "period": "July 2025 August 2025",
            "description": "Development of intelligent multilingual translation assistant with automatic language detection",
            "technologies": "Python Scikit learn Transformers Hugging Face NLP Langchain"
        }
    ],
    
    "education": [
        {
            "degree": "Engineering Cycle Data Science AI Big Data",
            "institution": "ENSA Tetouan",
            "period": "2023 Present",
            "description": "Specialization in artificial intelligence and massive data processing"
        },
        {
            "degree": "Preparatory Classes",
            "institution": "ENSA Tetouan",
            "period": "2021 2023",
            "description": "Intensive training in mathematics and engineering sciences"
        },
        {
            "degree": "Scientific BAC High Honors",
            "institution": "GSP Saint Jean NZerekore",
            "period": "2019 2020",
            "description": "Diploma with high honors in sciences"
        }
    ],
    
    "certifications": [
        {
            "title": "MLOps Concepts",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/24c0596b019268b75c8bee3a6aa3869f2420d7b1?raw=1"
        },
        {
            "title": "Understanding Cloud Computing",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/completed/statement-of-accomplishment/course/c2c7770fb5a03701ed749850724f4af5a7412e49"
        },
        {
            "title": "Cleaning Data with PySpark",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/893998791b120ac1ffd69bb7e87b057e152b80bd?raw=1"
        },
        {
            "title": "Feature Engineering with PySpark",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/0e2331ad3e6b1ab4876a821f1d879e8b6924f847?raw=1"
        },
        {
            "title": "Introduction to Python",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/08591f150a4fdf0dcfd60c08cc63bee9d1d4ab8e?raw=1"
        },
        {
            "title": "Big Data Fundamentals with PySpark",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/442a9465ee316fdb56192d9d9deeea9b7f267da0?raw=1"
        },
        {
            "title": "Introduction to PySpark",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/c7b2236fe5ba62d686704292ea016b3fcc2b1de8?raw=1"
        }
    ]
}

# Fonctions utilitaires
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def make_circle(image, new_size=(200, 200)):
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    image = image.resize((size, size), Image.LANCZOS)
    circular_img = Image.new("RGBA", (size, size))
    circular_img.paste(image, (0, 0), mask)
    circular_img = circular_img.resize(new_size, Image.LANCZOS)
    return circular_img

def load_profile_image():
    try:
        profile_img = Image.open("michel.jpeg")
        circular_profile = make_circle(profile_img)
        return f"data:image/png;base64,{image_to_base64(circular_profile)}"
    except:
        return None

# Chargement de l'image de profil
profile_base64 = load_profile_image()

# CSS simple et efficace
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .skill-bar {
        background-color: #f0f0f0;
        border-radius: 10px;
        height: 20px;
        margin: 10px 0;
        overflow: hidden;
    }
    
    .skill-progress {
        background: linear-gradient(90deg, #667eea, #764ba2);
        height: 100%;
        border-radius: 10px;
        transition: width 1s ease;
    }
    
    .project-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
    }
    
    .education-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #764ba2;
    }
    
    .contact-info {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .social-links a {
        padding: 0.5rem 1rem;
        background: #667eea;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        transition: background 0.3s;
    }
    
    .social-links a:hover {
        background: #764ba2;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown(f"""
<div class="main-header">
    <h1>{PORTFOLIO_DATA['name']}</h1>
    <h2>{PORTFOLIO_DATA['title']}</h2>
    <p>{PORTFOLIO_DATA['about']}</p>
</div>
""", unsafe_allow_html=True)

# Navigation par onglets
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Home", "Skills", "Projects", "Experience", "Education", "Contact"
])

# Onglet Home
with tab1:
    st.header("Welcome to my Portfolio")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if profile_base64:
            st.image(profile_base64, width=200)
    
    with col2:
        st.write("I am an engineering student passionate about Artificial Intelligence and Data Science.")
        st.write("My goal is to create innovative solutions that transform data into valuable insights.")
        
        st.markdown("""
        <div class="social-links">
            <a href="https://www.linkedin.com/in/michel-sagesse-kolie-9313a9281/" target="_blank">LinkedIn</a>
            <a href="https://github.com/MichelSagesse" target="_blank">GitHub</a>
            <a href="mailto:michelsagesse16@gmail.com">Email</a>
        </div>
        """, unsafe_allow_html=True)

# Onglet Skills
with tab2:
    st.header("Technical Skills")
    
    for skill, level in PORTFOLIO_DATA["skills"].items():
        st.write(f"{skill}: {level}%")
        st.markdown(f"""
        <div class="skill-bar">
            <div class="skill-progress" style="width: {level}%;"></div>
        </div>
        """, unsafe_allow_html=True)

# Onglet Projects
with tab3:
    st.header("Projects")
    
    for project in PORTFOLIO_DATA["projects"]:
        st.markdown(f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p><strong>Description:</strong> {project['description']}</p>
            <p><strong>Technologies:</strong> {project['technologies']}</p>
            <p><strong>Category:</strong> {project['category']}</p>
        </div>
        """, unsafe_allow_html=True)

# Onglet Experience
with tab4:
    st.header("Professional Experience")
    
    for exp in PORTFOLIO_DATA["experience"]:
        st.markdown(f"""
        <div class="project-card">
            <h3>{exp['title']}</h3>
            <p><strong>Company:</strong> {exp['company']}</p>
            <p><strong>Period:</strong> {exp['period']}</p>
            <p><strong>Description:</strong> {exp['description']}</p>
            <p><strong>Technologies:</strong> {exp['technologies']}</p>
        </div>
        """, unsafe_allow_html=True)

# Onglet Education
with tab5:
    st.header("Education")
    
    for edu in PORTFOLIO_DATA["education"]:
        st.markdown(f"""
        <div class="education-card">
            <h3>{edu['degree']}</h3>
            <p><strong>Institution:</strong> {edu['institution']}</p>
            <p><strong>Period:</strong> {edu['period']}</p>
            <p><strong>Description:</strong> {edu['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Onglet Contact
with tab6:
    st.header("Contact Information")
    
    st.markdown(f"""
    <div class="contact-info">
        <p><strong>Email:</strong> {PORTFOLIO_DATA['email']}</p>
        <p><strong>Phone:</strong> {PORTFOLIO_DATA['phone']}</p>
        <p><strong>Address:</strong> {PORTFOLIO_DATA['address']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.header("Certifications")
    
    for cert in PORTFOLIO_DATA["certifications"]:
        st.markdown(f"""
        <div class="project-card">
            <h3>{cert['title']}</h3>
            <p><strong>Issuer:</strong> {cert['issuer']}</p>
            <p><strong>Date:</strong> {cert['date']}</p>
            <a href="{cert['link']}" target="_blank">View Certificate</a>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
---
**Portfolio Michel Sagesse Kolié** - Data Scientist & AI Engineer
""")