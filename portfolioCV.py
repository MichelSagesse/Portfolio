import streamlit as st
from PIL import Image, ImageDraw
import base64
from io import BytesIO

# ✅ Page Config
st.set_page_config(
    page_title="Portfolio - Michel Sagesse Kolie",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Charger le CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# ✅ Portfolio Info
name = "MICHEL SAGESSE KOLIE"
title = "Data Scientist | AI & Big Data Engineer"
email = "michelsagesse16@gmail.com"
phone = "+212710871157"
address = "Tetouan, Morocco"
linkedin = "https://www.linkedin.com/in/michel-sagesse-koli%C3%A9-9313a9281/"
github = "https://github.com/MichelSagesse"

# ✅ Profile Picture
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

# Load profile image
try:
    img = Image.open("38da26ec-abab-46b9-9836-12c19d8376eb.jpeg")
    circular_image = make_circle(img)
    profile_img = f"data:image/png;base64,{image_to_base64(circular_image)}"
except:
    profile_img = None

# Load project images
def load_image(path, size=(300, 200)):
    try:
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)
        return f"data:image/png;base64,{image_to_base64(img)}"
    except:
        return None

# Placeholder images - replace with your actual project images
project_images = {
    "stock": load_image("stock_prediction.jpg"),
    "house": load_image("house_price.jpg"),
    "face": load_image("face_recognition.jpg"),
    "movie": load_image("movie_recommendation.jpg")
}

# Function to display social icons
def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
    <a href="{url}" target="_blank" style="margin-right: 15px;">
        <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
    </a>
    '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src = {
            "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
            "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
            "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png",
            "phone": "https://cdn-icons-png.flaticon.com/512/126/126341.png"
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(
                url=url, 
                icon_src=icon_src, 
                alt_text=name.capitalize(), 
                width=width, 
                height=height
            )

    return icons_html

# ✅ Hero Section (version Streamlit native)
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.title(name)
    st.markdown(f"#### {title}")
    
    # Social icons
    st.markdown("""
    <div style="display: flex; gap: 15px; margin-top: 20px;">
        <a href="{linkedin}" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="32">
        </a>
        <a href="{github}" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="32">
        </a>
        <a href="mailto:{email}">
            <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width="32">
        </a>
        <a href="tel:{phone}">
            <img src="https://cdn-icons-png.flaticon.com/512/126/126341.png" width="32">
        </a>
    </div>
    """.format(linkedin=linkedin, github=github, email=email, phone=phone), 
    unsafe_allow_html=True)

with col2:
    if profile_img:
        st.image(profile_img, width=200)

# Ligne de séparation stylisée
st.markdown("---")

# ✅ Navigation Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🏠 Accueil", "🎓 Éducation", "🚀 Compétences", "📂 Projets", "📜 Certifications", "📩 Contact"])

with tab1:
    st.header("👋 Bienvenue sur mon Portfolio")
    st.write("Je suis un élève ingénieur en Data Science, Big data et Intelligence Artificielle passionné par la résolution de problèmes complexes grâce à la puissance des données.")
    
    # Cartes de compétences clés
    cols = st.columns(3)
    with cols[0]:
        with st.container(border=True):
            st.markdown("### 📈 Data Science")
            st.write("Analyse et modélisation de données pour extraire des insights précieux")
    
    with cols[1]:
        with st.container(border=True):
            st.markdown("### 🤖 IA & ML")
            st.write("Développement de modèles d'apprentissage automatique et deep learning")
    
    with cols[2]:
        with st.container(border=True):
            st.markdown("### 💾 Big Data")
            st.write("Traitement et analyse de volumes massifs de données")
    
    # CV Download
    try:
        with open("resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Télécharger mon CV complet",
            data=PDFbyte,
            file_name="MICHEL_SAGESSE_KOLIE_CV.pdf",
            mime='application/pdf',
            use_container_width=True
        )
    except FileNotFoundError:
        st.warning("⚠️ Fichier 'resume.pdf' introuvable.")

with tab2:
    st.header("🎓 Parcours Académique")
    
    st.markdown("""
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-content">
                <h3>2023 - Présent</h3>
                <h4>Cycle Ingénieur - Data Science, IA & Big Data</h4>
                <p>ENSA Tétouan, Maroc</p>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-content">
                <h3>2021 - 2023</h3>
                <h4>Classes Préparatoires</h4>
                <p>ENSA Tétouan, Maroc</p>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-content">
                <h3>2019 - 2020</h3>
                <h4>BAC Scientifique - Mention Très Bien</h4>
                <p>GSP Saint Jean, N'Zérékoré</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.header("🚀 Compétences Techniques")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Langages de Programmation")
        st.markdown("""
        <div class="skill-bar">
            <div class="skill-name">Python</div>
            <div class="skill-level" style="width: 90%;">90%</div>
        </div>
        <div class="skill-bar">
            <div class="skill-name">SQL</div>
            <div class="skill-level" style="width: 85%;">85%</div>
        </div>
        <div class="skill-bar">
            <div class="skill-name">R</div>
            <div class="skill-level" style="width: 70%;">70%</div>
        </div>
        <div class="skill-bar">
            <div class="skill-name">C</div>
            <div class="skill-level" style="width: 65%;">65%</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Outils & Technologies")
        st.markdown("""
        - 🛠️ **IDE**: VS Code, Jupyter, PyCharm
        - 📊 **Data Science**: Pandas, NumPy, Scikit-learn
        - 🧠 **ML/DL**: TensorFlow, Keras, PyTorch
        - 💾 **Big Data**: Hadoop, Spark, Hive,Kafka, Impala
        """)
    
    with col2:
        st.subheader("Bases de Données")
        st.markdown("""
        <div class="skill-bar">
            <div class="skill-name">MySQL</div>
            <div class="skill-level" style="width: 85%;">85%</div>
        </div>
        <div class="skill-bar">
            <div class="skill-name">MongoDB</div>
            <div class="skill-level" style="width: 75%;">75%</div>
        </div>
        <div class="skill-bar">
            <div class="skill-name">PostgreSQL</div>
            <div class="skill-level" style="width: 80%;">80%</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Soft Skills")
        st.markdown("""
        - 🧩 Résolution de problèmes
        - 🤝 Travail d'équipe
        - 📝 Communication efficace
        - ⏱️ Gestion du temps
        - 🔍 Esprit d'analyse
        """)

with tab4:
    st.header("📂 Projets Réalisés")
    
    st.subheader("🧠 Projets IA & Data Science")
    
    # Project 1
    with st.expander("📈 Prédiction Boursière avec LSTM"):
        col1, col2 = st.columns([1, 2])
        with col1:
            if project_images["stock"]:
                st.image(project_images["stock"], use_column_width=True)
        with col2:
            st.markdown("""
            **Description:** Développement d'un modèle LSTM pour prédire les cours boursiers.
            **Technologies:** Python, TensorFlow, Keras, Pandas
            **Fonctionnalités:**
            - Collecte de données historiques
            - Prétraitement des séries temporelles
            - Architecture LSTM personnalisée
            - Visualisation des prédictions
            """)
    
    # Project 2
    with st.expander("🏠 Estimation du Prix des Maisons"):
        col1, col2 = st.columns([1, 2])
        with col1:
            if project_images["house"]:
                st.image(project_images["house"], use_column_width=True)
        with col2:
            st.markdown("""
            **Description:** Modèle de régression pour estimer les prix immobiliers.
            **Technologies:** Scikit-learn, Pandas, Matplotlib
            **Fonctionnalités:**
            - Feature engineering
            - Sélection de modèles
            - Optimisation hyperparamètres
            - Interface de prédiction
            """)
    
    st.subheader("🌍 Projets Open Source")
    with st.expander("🎬 Système de Recommandation de Films"):
        col1, col2 = st.columns([1, 2])
        with col1:
            if project_images["movie"]:
                st.image(project_images["movie"], use_column_width=True)
        with col2:
            st.markdown("""
            **Description:** Système de recommandation basé sur le contenu et la collaboration.
            **Technologies:** Python, Pandas, Scikit-learn
            **Lien GitHub:** [Voir le projet](https://github.com/MichelSagesse/movie-recommender)
            """)

with tab5:
    st.header("📜 Certifications")
    
    certs = [
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
        }
    ]
    
    for cert in certs:
        with st.expander(f"📜 {cert['title']}"):
            st.markdown(f"""
            **Émetteur:** {cert['issuer']}  
            **Date:** {cert['date']}  
            **Lien:** [Voir certification]({cert['link']})
            """)

with tab6:
    st.header("📩 Contactez-moi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Informations de Contact")
        st.markdown(f"""
        <div class="contact-info">
            <p>📧 <strong>Email:</strong> {email}</p>
            <p>📞 <strong>Téléphone:</strong> {phone}</p>
            <p>📍 <strong>Adresse:</strong> {address}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Réseaux Sociaux")
        st.markdown(social_icons(40, 40, LinkedIn=linkedin, GitHub=github, Email=f"mailto:{email}", Phone=f"tel:{phone}"), 
                   unsafe_allow_html=True)
    
    with col2:
        st.subheader("Envoyez un Message")
        contact_form = """
        <form action="https://formsubmit.co/michelsagesse16@gmail.com" method="POST" class="contact-form">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Votre nom" required>
            <input type="email" name="email" placeholder="Votre email" required>
            <textarea name="message" placeholder="Votre message" required></textarea>
            <button type="submit">Envoyer</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

# ✅ Footer
st.markdown("""
<footer>
    <p>© 2025 Michel Sagesse Kolié - Tous droits réservés</p>
    <p>Dernière mise à jour: Mai 2025</p>
</footer>
""", unsafe_allow_html=True)