import streamlit as st
from PIL import Image, ImageDraw, ImageFilter
import base64
from io import BytesIO
import time
import json
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import os

# ===== CONFIGURATION DE LA PAGE =====
st.set_page_config(
    page_title="📄Portfolio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/MichelSagesse',
        'Report a bug': "mailto:michelsagesse16@gmail.com",
        'About': "# Portfolio Michel Sagesse Kolié\nData Scientist & AI Engineer"
    }
)

# ===== GESTION DU MODE SOMBRE =====
def init_dark_mode():
    """Initialise le mode sombre dans la session"""
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False

def toggle_dark_mode():
    """Bascule le mode sombre"""
    st.session_state.dark_mode = not st.session_state.dark_mode

def get_dark_mode_css():
    """Retourne le CSS pour le mode sombre"""
    if st.session_state.dark_mode:
        return """
        <style>
        :root {
            --primary-color: #667eea;
            --secondary-color: #764ba2;
            --accent-color: #f093fb;
            --text-primary: #e2e8f0;
            --text-secondary: #a0aec0;
            --bg-primary: #1a202c;
            --bg-secondary: #2d3748;
            --bg-card: #2d3748;
            --border-color: #4a5568;
            --shadow-light: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            --shadow-medium: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
            --shadow-heavy: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
        }
        
        .stApp {
            background-color: var(--bg-primary) !important;
        }
        
        .main .block-container {
            background-color: var(--bg-primary) !important;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            background-color: var(--bg-secondary) !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: var(--bg-secondary) !important;
            color: var(--text-primary) !important;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary-color) !important;
            color: white !important;
        }
        
        .stSelectbox > div > div {
            background-color: var(--bg-secondary) !important;
            color: var(--text-primary) !important;
        }
        
        .stExpander > div > div {
            background-color: var(--bg-card) !important;
            border-color: var(--border-color) !important;
        }
        
        .stButton > button {
            background-color: var(--primary-color) !important;
            color: white !important;
        }
        
        .stMetric > div > div {
            color: var(--text-primary) !important;
        }
        
        .stMarkdown {
            color: var(--text-primary) !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-primary) !important;
        }
        
        p {
            color: var(--text-secondary) !important;
        }
        
        .stSidebar {
            background-color: var(--bg-secondary) !important;
        }
        
        .stSidebar .sidebar-content {
            background-color: var(--bg-secondary) !important;
        }
        
        .stSidebar .sidebar-content > div {
            color: var(--text-primary) !important;
        }
        </style>
        """
    return ""

# ===== CHARGEMENT CSS =====
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# ===== INITIALISATION =====
init_dark_mode()

# ===== FONCTIONS POUR LES VIDÉOS =====
def get_video_path(project_title):
    """Retourne le chemin de la vidéo pour un projet donné"""
    # Mapping des noms de projets vers les noms de fichiers vidéo
    video_mapping = {
        "Heart Rate Prediction and Patient Monitoring System": "appmedical.mp4",
        "Movie Recommendation System": ""
    }

    video_filename = video_mapping.get(project_title)
    if video_filename and os.path.exists(video_filename):
        return video_filename
    return None

def display_project_video(video_path):
    """Affiche une vidéo de projet avec des contrôles personnalisés"""
    if video_path and os.path.exists(video_path):
        st.markdown(f"""
        <div style="border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-medium);">
            <video width="100%" controls style="border-radius: 12px;">
                <source src="{video_path}" type="video/mp4">
                Votre navigateur ne supporte pas la lecture de vidéos.
            </video>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: var(--bg-secondary); padding: 2rem; border-radius: 12px; text-align: center; color: var(--text-secondary);">
            <p>🎬 Video demonstration in preparation...</p>
        </div>
        """, unsafe_allow_html=True)

# ===== FONCTIONS POUR LES IMAGES DES CERTIFICATIONS =====
def load_certification_image(image_name, size=(80, 80)):
    """Charge et redimensionne une image de certification"""
    try:
        image_path = os.path.join("images", image_name)
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize(size, Image.LANCZOS)
            return f"data:image/png;base64,{image_to_base64(img)}"
        return None
    except Exception as e:
        print(f"Erreur lors du chargement de l'image {image_name}: {e}")
        return None

def display_certification_image(image_path, alt_text, size=(80, 80)):
    """Affiche une image de certification avec style"""
    if image_path:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 1rem;">
            <img src="{image_path}" alt="{alt_text}" style="width: {size[0]}px; height: {size[1]}px; border-radius: 8px; box-shadow: var(--shadow-light);">
        </div>
        """, unsafe_allow_html=True)
    else:
        # Fallback avec une icône par défaut
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="width: {size[0]}px; height: {size[1]}px; background: var(--gradient-primary); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: var(--shadow-light);">
                <span style="font-size: 2rem;">📜</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ===== FONCTIONS POUR LES IMAGES DES CERTIFICATIONS =====
def load_certification_image(image_name, size=(80, 80)):
    """Charge et redimensionne une image de certification"""
    try:
        image_path = os.path.join("images", image_name)
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize(size, Image.LANCZOS)
            return f"data:image/png;base64,{image_to_base64(img)}"
        return None
    except Exception as e:
        print(f"Erreur lors du chargement de l'image {image_name}: {e}")
        return None

def display_certification_image(image_path, alt_text, size=(80, 80)):
    """Affiche une image de certification avec style"""
    if image_path:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 1rem;">
            <img src="{image_path}" alt="{alt_text}" style="width: {size[0]}px; height: {size[1]}px; border-radius: 8px; box-shadow: var(--shadow-light);">
        </div>
        """, unsafe_allow_html=True)
    else:
        # Fallback avec une icône par défaut
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="width: {size[0]}px; height: {size[1]}px; background: var(--gradient-primary); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: var(--shadow-light);">
                <span style="font-size: 2rem;">📜</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ===== DONNÉES DU PORTFOLIO =====
PORTFOLIO_DATA = {
    "personal": {
        "name": "MICHEL SAGESSE KOLIE",
        "title": "Data Scientist | AI & Big Data Engineer",
        "email": "michelsagesse16@gmail.com",
        "phone": "+212710871157",
        "address": "Tetouan, Morocco",
        "linkedin": "https://www.linkedin.com/in/michel-sagesse-kolie-9313a9281/",
        "github": "https://github.com/MichelSagesse",
        "about": "Passionate about AI and Data Science, I transform data into innovative solutions."
    },
    "skills": {
        "programming": {
            "Python": 95,
            "SQL": 90,
            "R": 80,
            "C": 60,
            "JavaScript": 70
        },
        "databases": {
            "MySQL": 90,
            "PostgreSQL": 85,
            "MongoDB": 80,
            "Redis": 75
        },
        "tools": {
            "TensorFlow": 85,
            "PyTorch": 80,
            "Scikit-learn": 90,
            "Pandas": 95,
            "NumPy": 90,
            "Hadoop": 75,
            "Spark": 80,
            "Kafka": 70
        }
    },
    "projects": [
        {
            "title": "Heart Rate Prediction and Patient Monitoring System",
            "description": "XGBoost algorithm estimates heart rate by filtering arm movement interferences through PPG and accelerometer signal comparison.",
            "image": "frequence_cardiaque.jpg",
            "technologies": ["Python", "XGBoost", "PCA", "Sensors", "Pandas"],
            "video": "appmedical.mp4",
            "category": "AI/ML"
        },
        {
            "title": "Movie Recommendation System",
            "description": "Hybrid recommendation engine combining collaborative filtering and content-based approaches",
            "image": "movie_recommendation.jpg",
            "technologies": ["Collaborative Filtering", "Content-Based", "Pandas", "Scikit-learn"],
            "video": "",
            "category": "Recommendation Systems"
        }
    ],
    "experience": [
        {
            "title": "AI (NLP) Intern",
            "company": "Smart Automation Technologies",
            "period": "July 2025 - August 2025",
            "description": "Development of intelligent multilingual translation assistant with automatic language detection",
            "technologies": ["Python", "Scikit-learn", "Transformers", "Hugging Face", "NLP", "Langchain"]
        }
    ],
    "education": [
        {
            "degree": "Engineering Cycle - Data Science, AI & Big Data",
            "institution": "ENSA Tetouan",
            "period": "2023 - Present",
            "description": "Specialization in artificial intelligence and massive data processing"
        },
        {
            "degree": "Preparatory Classes",
            "institution": "ENSA Tetouan",
            "period": "2021 - 2023",
            "description": "Intensive training in mathematics and engineering sciences"
        },
        {
            "degree": "Scientific BAC - High Honors",
            "institution": "GSP Saint Jean, N'Zerekore",
            "period": "2019 - 2020",
            "description": "Diploma with high honors in sciences"
        }
    ],
    "certifications": [
        {
            "title": "MLOps Concepts",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/24c0596b019268b75c8bee3a6aa3869f2420d7b1?raw=1",
            "image": "mlops_datacamp.jpg"
        },
        {
            "title": "Understanding Cloud Computing",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/completed/statement-of-accomplishment/course/c2c7770fb5a03701ed749850724f4af5a7412e49",
            "image": "cloud_computing_datacamp.png"
        },
        {
            "title": "Cleaning Data with PySpark",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/893998791b120ac1ffd69bb7e87b057e152b80bd?raw=1",
            "image": "cleaning.jpg"
        },
        {
            "title": "Feature Engineering with PySpark",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/0e2331ad3e6b1ab4876a821f1d879e8b6924f847?raw=1",
            "image": "feature_engineering.jpg"
        },
        {
            "title": "Introduction to Python",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/08591f150a4fdf0dcfd60c08cc63bee9d1d4ab8e?raw=1",
            "image": "python.jpg"
        },
        {
            "title": "Big Data Fundamentals with PySpark",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/442a9465ee316fdb56192d9d9deeea9b7f267da0?raw=1",
            "image": "big_data_fundamentals.jpg"
        },
        {
            "title": "Introduction to PySpark",
            "issuer": "DataCamp",
            "date": "2025",
            "link": "https://www.datacamp.com/statement-of-accomplishment/course/c7b2236fe5ba62d686704292ea016b3fcc2b1de8?raw=1",
            "image": "intropyspark.jpg"
        }
    ]
}

# ===== FONCTIONS UTILITAIRES =====
def safe_markdown(text, **kwargs):
    """Affiche du texte de manière sécurisée en évitant les problèmes de regex"""
    try:
        # Essayer d'abord avec st.markdown
        st.markdown(text, **kwargs)
    except Exception as e:
        # Si ça échoue, utiliser st.write comme fallback
        st.write(text)

def clean_text_for_markdown(text):
    """Nettoie le texte pour éviter les problèmes de regex dans le markdown"""
    if not text:
        return ""
    
    # Supprimer les caractères de contrôle
    import re
    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    
    # Remplacer tous les caractères spéciaux problématiques
    replacements = {
        '´': "'",
        '`': "'",
        '"': '"',
        '"': '"',
        ''': "'",
        ''': "'",
        '–': '-',
        '—': '-',
        '…': '...',
        '®': '(R)',
        '©': '(C)',
        '™': '(TM)',
        '°': ' degres',
        '±': '+/-',
        '×': 'x',
        '÷': '/',
        '≤': '<=',
        '≥': '>=',
        '≠': '!=',
        '≈': '~',
        '∞': 'infini',
        '√': 'racine',
        '²': '2',
        '³': '3',
        '¼': '1/4',
        '½': '1/2',
        '¾': '3/4',
        '€': 'EUR',
        '£': 'GBP',
        '¥': 'JPY',
        '¢': 'cent',
        '§': 'section',
        '¶': 'paragraphe',
        '†': '+',
        '‡': '++',
        '•': '-',
        '·': '-',
        '‣': '-',
        '◦': '-',
        '▪': '-',
        '▫': '-',
        '◊': '<>',
        '○': 'O',
        '●': 'O',
        '◐': 'O',
        '◑': 'O',
        '◒': 'O',
        '◓': 'O',
        '◔': 'O',
        '◕': 'O',
        '◖': '[',
        '◗': ']',
        '◘': 'O',
        '◙': 'O',
        '◚': 'O',
        '◛': 'O',
        '◜': 'O',
        '◝': 'O',
        '◞': 'O',
        '◟': 'O',
        '◠': 'O',
        '◡': 'O',
        '◢': 'O',
        '◣': 'O',
        '◤': 'O',
        '◥': 'O',
        '◦': 'O',
        '◧': 'O',
        '◨': 'O',
        '◩': 'O',
        '◪': 'O',
        '◫': 'O',
        '◬': 'O',
        '◭': 'O',
        '◮': 'O',
        '◯': 'O',
        '◰': 'O',
        '◱': 'O',
        '◲': 'O',
        '◳': 'O',
        '◴': 'O',
        '◵': 'O',
        '◶': 'O',
        '◷': 'O',
        '◸': 'O',
        '◹': 'O',
        '◺': 'O',
        '◻': 'O',
        '◼': 'O',
        '◽': 'O',
        '◾': 'O',
        '◿': 'O',
        '☀': 'soleil',
        '☁': 'nuage',
        '☂': 'parapluie',
        '☃': 'bonhomme_neige',
        '☄': 'comete',
        '★': '*',
        '☆': '*',
        '☎': 'telephone',
        '☏': 'telephone',
        '☐': 'case',
        '☑': 'case_cochee',
        '☒': 'case_barree',
        '☓': 'X',
        '☚': '<',
        '☛': '>',
        '☜': '<',
        '☝': '^',
        '☞': '>',
        '☟': 'v',
        '☠': 'tete_de_mort',
        '☡': 'attention',
        '☢': 'radioactif',
        '☣': 'biohazard',
        '☤': 'caducee',
        '☥': 'ankh',
        '☦': 'croix_orthodoxe',
        '☧': 'chi_rho',
        '☨': 'croix_latine',
        '☩': 'croix_maltese',
        '☪': 'croissant_etoile',
        '☫': 'farsi',
        '☬': 'khanda',
        '☭': 'marteau_faucille',
        '☮': 'paix',
        '☯': 'yin_yang',
        '☰': 'trigramme',
        '☱': 'trigramme',
        '☲': 'trigramme',
        '☳': 'trigramme',
        '☴': 'trigramme',
        '☵': 'trigramme',
        '☶': 'trigramme',
        '☷': 'trigramme',
        '☸': 'dharma',
        '☹': 'visage_triste',
        '☺': 'visage_heureux',
        '☻': 'visage_heureux',
        '☼': 'soleil',
        '☽': 'lune',
        '☾': 'lune',
        '☿': 'mercure',
        '♀': 'venus',
        '♁': 'terre',
        '♂': 'mars',
        '♃': 'jupiter',
        '♄': 'saturne',
        '♅': 'uranus',
        '♆': 'neptune',
        '♇': 'pluton',
        '♈': 'belier',
        '♉': 'taureau',
        '♊': 'gemeaux',
        '♋': 'cancer',
        '♌': 'lion',
        '♍': 'vierge',
        '♎': 'balance',
        '♏': 'scorpion',
        '♐': 'sagittaire',
        '♑': 'capricorne',
        '♒': 'verseau',
        '♓': 'poissons',
        '♔': 'roi_blanc',
        '♕': 'reine_blanche',
        '♖': 'tour_blanche',
        '♗': 'fou_blanc',
        '♘': 'cavalier_blanc',
        '♙': 'pion_blanc',
        '♚': 'roi_noir',
        '♛': 'reine_noire',
        '♜': 'tour_noire',
        '♝': 'fou_noir',
        '♞': 'cavalier_noir',
        '♟': 'pion_noir',
        '♠': 'pique',
        '♡': 'coeur',
        '♢': 'carreau',
        '♣': 'trefle',
        '♤': 'pique_blanc',
        '♥': 'coeur_rouge',
        '♦': 'carreau_rouge',
        '♧': 'trefle_blanc',
        '♨': 'bain_chaud',
        '♩': 'note',
        '♪': 'note',
        '♫': 'notes',
        '♬': 'notes',
        '♭': 'bemol',
        '♮': 'becarre',
        '♯': 'diese',
        '♰': 'croix',
        '♱': 'croix',
        '♲': 'recyclage',
        '♳': 'recyclage',
        '♴': 'recyclage',
        '♵': 'recyclage',
        '♶': 'recyclage',
        '♷': 'recyclage',
        '♸': 'recyclage',
        '♹': 'recyclage',
        '♺': 'recyclage',
        '♻': 'recyclage',
        '♼': 'recyclage',
        '♽': 'recyclage',
        '♾': 'infini',
        '♿': 'fauteuil_roulant',
        '⚀': 'de_1',
        '⚁': 'de_2',
        '⚂': 'de_3',
        '⚃': 'de_4',
        '⚄': 'de_5',
        '⚅': 'de_6',
        '⚆': 'de_blanc',
        '⚇': 'de_noir',
        '⚈': 'de_blanc',
        '⚉': 'de_noir',
        '⚊': 'ligne',
        '⚋': 'ligne',
        '⚌': 'ligne',
        '⚍': 'ligne',
        '⚎': 'ligne',
        '⚏': 'ligne',
        '⚐': 'ligne',
        '⚑': 'ligne',
        '⚒': 'marteau_pioche',
        '⚓': 'ancre',
        '⚔': 'epees',
        '⚕': 'caducee',
        '⚖': 'balance',
        '⚗': 'alambic',
        '⚘': 'fleur',
        '⚙': 'engrenage',
        '⚚': 'caducee',
        '⚛': 'atome',
        '⚜': 'fleur_de_lys',
        '⚝': 'etoile',
        '⚞': 'etoile',
        '⚟': 'etoile',
        '⚠': 'attention',
        '⚡': 'eclair',
        '⚢': 'femmes',
        '⚣': 'hommes',
        '⚤': 'femme_homme',
        '⚥': 'femme_homme',
        '⚦': 'homme_femme',
        '⚧': 'homme_femme',
        '⚨': 'mars_fleche',
        '⚩': 'venus_fleche',
        '⚪': 'cercle_blanc',
        '⚫': 'cercle_noir',
        '⚬': 'cercle_blanc',
        '⚭': 'cercle_blanc',
        '⚮': 'cercle_blanc',
        '⚯': 'cercle_blanc',
        '⚰': 'cercueil',
        '⚱': 'urne',
        '⚲': 'neutre',
        '⚳': 'ceres',
        '⚴': 'pallas',
        '⚵': 'juno',
        '⚶': 'vesta',
        '⚷': 'chiron',
        '⚸': 'lune_noeud',
        '⚹': 'sextile',
        '⚺': 'semisextile',
        '⚻': 'quincunx',
        '⚼': 'sesquiquadre',
        '⚽': 'football',
        '⚾': 'baseball',
        '⚿': 'cible',
        '⛀': 'cible',
        '⛁': 'cible',
        '⛂': 'cible',
        '⛃': 'cible',
        '⛄': 'bonhomme_neige',
        '⛅': 'soleil_nuage',
        '⛆': 'pluie',
        '⛇': 'neige',
        '⛈': 'orage',
        '⛉': 'soleil',
        '⛊': 'lune',
        '⛋': 'lune',
        '⛌': 'lune',
        '⛍': 'lune',
        '⛎': 'ophiuchus',
        '⛏': 'pioche',
        '⛐': 'lune',
        '⛑': 'casque',
        '⛒': 'route',
        '⛓': 'chaines',
        '⛔': 'interdit',
        '⛕': 'route',
        '⛖': 'route',
        '⛗': 'route',
        '⛘': 'route',
        '⛙': 'route',
        '⛚': 'route',
        '⛛': 'route',
        '⛜': 'route',
        '⛝': 'route',
        '⛞': 'route',
        '⛟': 'route',
        '⛠': 'route',
        '⛡': 'route',
        '⛢': 'uranus',
        '⛣': 'route',
        '⛤': 'route',
        '⛥': 'route',
        '⛦': 'route',
        '⛧': 'route',
        '⛨': 'route',
        '⛩': 'sanctuaire',
        '⛪': 'eglise',
        '⛫': 'eglise',
        '⛬': 'eglise',
        '⛭': 'eglise',
        '⛮': 'eglise',
        '⛯': 'eglise',
        '⛰': 'montagne',
        '⛱': 'parasol',
        '⛲': 'fontaine',
        '⛳': 'golf',
        '⛴': 'ferry',
        '⛵': 'voilier',
        '⛶': 'voilier',
        '⛷': 'ski',
        '⛸': 'patinage',
        '⛹': 'basketball',
        '⛺': 'tente',
        '⛻': 'route',
        '⛼': 'route',
        '⛽': 'essence',
        '⛾': 'route',
        '⛿': 'route'
    }
    
    for old_char, new_char in replacements.items():
        text = text.replace(old_char, new_char)
    
    # Supprimer les caractères restants problématiques
    text = re.sub(r'[^\w\s\-.,!?;:()\[\]{}"\']', '', text)
    
    return text.strip()

def image_to_base64(image):
    """Convertit une image PIL en base64"""
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def make_circle(image, new_size=(200, 200)):
    """Crée une image circulaire"""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    image = image.resize((size, size), Image.LANCZOS)
    circular_img = Image.new("RGBA", (size, size))
    circular_img.paste(image, (0, 0), mask)
    circular_img = circular_img.resize(new_size, Image.LANCZOS)
    return circular_img

def load_image(path, size=(300, 200)):
    """Charge et redimensionne une image"""
    try:
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)
        return f"data:image/png;base64,{image_to_base64(img)}"
    except:
        return None

def create_skill_chart(skills_data):
    """Crée un graphique radar des compétences"""
    categories = list(skills_data.keys())
    values = list(skills_data.values())
    
    # Couleurs adaptées au mode sombre
    colors = ['#667eea', '#764ba2'] if st.session_state.dark_mode else ['#667eea', '#764ba2']
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Compétences',
        line_color=colors[0]
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='rgba(255,255,255,0.1)' if st.session_state.dark_mode else 'rgba(0,0,0,0.1)',
                linecolor='rgba(255,255,255,0.3)' if st.session_state.dark_mode else 'rgba(0,0,0,0.3)',
                tickfont=dict(color='#e2e8f0' if st.session_state.dark_mode else '#2d3748')
            ),
            angularaxis=dict(
                gridcolor='rgba(255,255,255,0.1)' if st.session_state.dark_mode else 'rgba(0,0,0,0.1)',
                linecolor='rgba(255,255,255,0.3)' if st.session_state.dark_mode else 'rgba(0,0,0,0.3)',
                tickfont=dict(color='#e2e8f0' if st.session_state.dark_mode else '#2d3748')
            ),
            bgcolor='rgba(0,0,0,0)' if st.session_state.dark_mode else 'rgba(255,255,255,0)'
        ),
        showlegend=False,
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor='rgba(0,0,0,0)' if st.session_state.dark_mode else 'rgba(255,255,255,0)',
        plot_bgcolor='rgba(0,0,0,0)' if st.session_state.dark_mode else 'rgba(255,255,255,0)'
    )
    
    return fig

def create_project_metrics():
    """Crée des métriques pour les projets"""
    total_projects = len(PORTFOLIO_DATA["projects"])
    ai_ml_projects = len([p for p in PORTFOLIO_DATA["projects"] if "AI" in p["category"] or "ML" in p["category"]])
    data_science_projects = len([p for p in PORTFOLIO_DATA["projects"] if "Data Science" in p["category"]])
    
    return {
        "total": total_projects,
        "ai_ml": ai_ml_projects,
        "data_science": data_science_projects
    }

# ===== CHARGEMENT DES IMAGES =====
try:
    profile_img = Image.open("michel.jpeg")
    circular_profile = make_circle(profile_img)
    profile_base64 = f"data:image/png;base64,{image_to_base64(circular_profile)}"
except:
    profile_base64 = None

project_images = {}
for project in PORTFOLIO_DATA["projects"]:
    project_images[project["title"]] = load_image(project["image"])

# Chargement des images des certifications
certification_images = {}
for cert in PORTFOLIO_DATA["certifications"]:
    certification_images[cert["title"]] = load_certification_image(cert["image"])

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h3>Navigation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Mode sombre/clair avec toggle
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🌙" if st.session_state.dark_mode else "☀️", on_click=toggle_dark_mode):
            pass
    with col2:
        st.markdown(f"**Mode {'Dark' if st.session_state.dark_mode else 'Light'}**")
    
    # Statistiques rapides
    metrics = create_project_metrics()
    st.markdown("### 📊 Statistics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Projects", metrics["total"])
    with col2:
        st.metric("AI/ML", metrics["ai_ml"])
    
    # Liens rapides
    st.markdown("### 🔗 Quick Links")
    if st.button("📄 Download CV"):
        try:
            with open("resume.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(
                label="📄 CV Michel Sagesse Kolié",
                data=PDFbyte,
                file_name="MICHEL_SAGESSE_KOLIE_CV.pdf",
                mime='application/pdf'
            )
        except FileNotFoundError:
            st.error("CV not found")
    
    if st.button("📧 Contact Me"):
        st.markdown(f"[📧 {PORTFOLIO_DATA['personal']['email']}](mailto:{PORTFOLIO_DATA['personal']['email']})")

# ===== APPLICATION DU MODE SOMBRE =====
st.markdown(get_dark_mode_css(), unsafe_allow_html=True)

# ===== HERO SECTION =====
st.markdown(f"""
<div class="hero-section">
    <div class="hero-content">
        <div class="hero-text">
            <h1>{PORTFOLIO_DATA['personal']['name']}</h1>
            <h2>{PORTFOLIO_DATA['personal']['title']}</h2>
            <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 2rem;">
                {PORTFOLIO_DATA['personal']['about']}
            </p>
            <div class="social-icons">
                <a href="{PORTFOLIO_DATA['personal']['linkedin']}" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
                </a>
                <a href="{PORTFOLIO_DATA['personal']['github']}" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
                </a>
                <a href="mailto:{PORTFOLIO_DATA['personal']['email']}">
                    <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" alt="Email">
                </a>
                <a href="tel:{PORTFOLIO_DATA['personal']['phone']}">
                    <img src="https://cdn-icons-png.flaticon.com/512/126/126341.png" alt="Phone">
                </a>
            </div>
        </div>
        <div class="hero-image">
            <img src="{profile_base64}" alt="Michel Sagesse Kolié" width="200">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== NAVIGATION TABS =====
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏠 Home", "🎓 Education", "💼 Experience", "🚀 Skills", 
    "📂 Projects", "📜 Certifications", "📩 Contact"
])

# ===== TAB 1: ACCUEIL =====
with tab1:
    st.header("👋 Welcome to my Portfolio")
    
    # Introduction avec animation
    with st.container():
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-icon">🎯</div>
                <h3>About Me</h3>
            </div>
            <p style="font-size: 1.1rem; line-height: 1.8;">
                I am an engineering student passionate about <strong>Artificial Intelligence</strong> and 
                <strong>Data Science</strong>. My goal is to create innovative solutions that 
                transform data into valuable insights to solve complex problems.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Cartes de compétences clés
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-icon">📈</div>
                <h3>Data Science</h3>
            </div>
            <p>Data analysis and modeling to extract valuable insights</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-icon">🤖</div>
                <h3>AI & ML</h3>
            </div>
            <p>Development of machine learning and deep learning models</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-icon">💾</div>
                <h3>Big Data</h3>
            </div>
            <p>Processing and analysis of massive data volumes</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Graphique des compétences
    st.subheader("📊 Skills Overview")
    skill_chart = create_skill_chart(PORTFOLIO_DATA["skills"]["programming"])
    st.plotly_chart(skill_chart, use_container_width=True)

# ===== TAB 2: ÉDUCATION =====
with tab2:
    st.header("🎓 Academic Background")
    
    for i, education in enumerate(PORTFOLIO_DATA["education"]):
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-content">
                <div class="timeline-date">{education['period']}</div>
                <div class="timeline-title">{education['degree']}</div>
                <div class="timeline-subtitle">{education['institution']}</div>
                <p style="margin-top: 1rem; color: var(--text-secondary);">
                    {education['description']}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ===== TAB 3: EXPÉRIENCE =====
with tab3:
    st.header("💼 Professional Experience")
    
    for experience in PORTFOLIO_DATA["experience"]:
        with st.expander(f"💼 {experience['title']} - {experience['company']}"):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"""
                **Period:** {experience['period']}  
                **Company:** {experience['company']}
                """)
            with col2:
                description = clean_text_for_markdown(experience['description'])
                technologies = ', '.join([clean_text_for_markdown(tech) for tech in experience['technologies']])
                
                safe_markdown(f"""
                **Description:** {description}
                
                **Technologies:** {technologies}
                """)

# ===== TAB 4: COMPÉTENCES =====
with tab4:
    st.header("🚀 Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💻 Programming Languages")
        for skill, level in PORTFOLIO_DATA["skills"]["programming"].items():
            st.markdown(f"""
            <div class="skill-container">
                <div class="skill-info">
                    <span class="skill-name">{skill}</span>
                    <span class="skill-percentage">{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.subheader("🗄️ Databases")
        for skill, level in PORTFOLIO_DATA["skills"]["databases"].items():
            st.markdown(f"""
            <div class="skill-container">
                <div class="skill-info">
                    <span class="skill-name">{skill}</span>
                    <span class="skill-percentage">{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🛠️ Tools & Technologies")
        for skill, level in PORTFOLIO_DATA["skills"]["tools"].items():
            st.markdown(f"""
            <div class="skill-container">
                <div class="skill-info">
                    <span class="skill-name">{skill}</span>
                    <span class="skill-percentage">{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.subheader("🎯 Soft Skills")
        soft_skills = [
            "Problem solving",
            "Teamwork",
            "Effective communication",
            "Time management",
            "Analytical thinking",
            "Creativity",
            "Continuous learning"
        ]
        
        for skill in soft_skills:
            st.markdown(f"• {skill}")

# ===== TAB 5: PROJETS =====
with tab5:
    st.header("📂 Completed Projects")
    
    # Filtres de projets
    col1, col2 = st.columns([1, 3])
    with col1:
        category_filter = st.selectbox(
            "Filter by category",
            ["All", "AI/ML", "Data Science", "Computer Vision", "Recommendation Systems","Big Data"]
        )
    
    # Affichage des projets
    filtered_projects = PORTFOLIO_DATA["projects"]
    if category_filter != "All":
        filtered_projects = [p for p in PORTFOLIO_DATA["projects"] if category_filter in p["category"]]
    
    for project in filtered_projects:
        with st.expander(f"🚀 {project['title']}"):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if project_images.get(project["title"]):
                    st.image(project_images[project["title"]], use_column_width=True)
            
            with col2:
                description = clean_text_for_markdown(project['description'])
                category = clean_text_for_markdown(project['category'])
                technologies = ', '.join([clean_text_for_markdown(tech) for tech in project['technologies']])
                
                safe_markdown(f"""
                **Description:** {description}
                
                **Category:** {category}
                
                **Technologies:** {technologies}
                """)
            
            # Section vidéo de démonstration
            st.markdown("### 🎬 Video Demonstration")
            video_path = get_video_path(project["title"])
            display_project_video(video_path)

# ===== TAB 6: CERTIFICATIONS =====
with tab6:
    st.header("📜 Certifications")
    
    for cert in PORTFOLIO_DATA["certifications"]:
        with st.expander(f"📜 {cert['title']}"):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Affichage de l'image de certification
                cert_image = certification_images.get(cert["title"])
                display_certification_image(cert_image, cert["title"])
            
            with col2:
                st.markdown(f"""
                **Issuer:** {cert['issuer']}  
                **Date:** {cert['date']}
                
                **[View certification]({cert['link']})**
                """)

# ===== TAB 7: CONTACT =====
with tab7:
    st.header("📩 Contact Me")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📞 Contact Information")
        st.markdown(f"""
        <div class="contact-info">
            <p>📧 <strong>Email:</strong> {PORTFOLIO_DATA['personal']['email']}</p>
            <p>📞 <strong>Phone:</strong> {PORTFOLIO_DATA['personal']['phone']}</p>
            <p>📍 <strong>Address:</strong> {PORTFOLIO_DATA['personal']['address']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("🔗 Social Networks")
        st.markdown(f"""
        <div class="social-icons">
            <a href="{PORTFOLIO_DATA['personal']['linkedin']}" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
            </a>
            <a href="{PORTFOLIO_DATA['personal']['github']}" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="40">
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("💬 Send a Message")
        contact_form = f"""
        <form action="https://formsubmit.co/{PORTFOLIO_DATA['personal']['email']}" method="POST" class="contact-form">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">📤 Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("""
<footer>
    <p>© 2025 Michel Sagesse Kolié - All rights reserved</p>
    <p>Last updated: """ + datetime.now().strftime("%B %Y") + """</p>
</footer>
""", unsafe_allow_html=True)

# ===== SCRIPT JAVASCRIPT POUR ANIMATIONS =====
st.markdown("""
<script>
// Animation des barres de compétences
document.addEventListener('DOMContentLoaded', function() {
    const skillBars = document.querySelectorAll('.skill-progress');
    skillBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = width;
        }, 500);
    });
});

// Animation au scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.card, .timeline-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});
</script>
""", unsafe_allow_html=True)