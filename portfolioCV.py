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

# ✅ Portfolio Info
name = "MICHEL SAGESSE KOLIE"
email = "michelsagesse16@gmail.com"
phone = "+212710871157"
address = "Tetouan, Morocco"
linkedin = "https://www.linkedin.com/in/michel-sagesse-koli%C3%A9-9313a9281/"
github = "https://github.com/MichelSagesse"

# ✅ Profile Picture
image_path = "38da26ec-abab-46b9-9836-12c19d8376eb.jpeg"
img = Image.open(image_path)

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

circular_image = make_circle(img)

# Function to display social icons
def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
    <a href="{url}" target="_blank" style="margin-right: 10px;">
        <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
    </a>
    '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src = {
            "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
            "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
            "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

    return icons_html

# ✅ Sidebar toggle state
if "show_contact" not in st.session_state:
    st.session_state.show_contact = True

# ✅ Top section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image_to_base64(circular_image)}" 
                 style="width: 200px; border-radius: 50%;" />
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="text-align: center;">
            <h1 style="font-size: 36px;">{name}</h1>
            <p style="font-size: 18px; color: gray;">Data Scientist | AI &  Big data Engineer</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .stButton>button {
            font-size: 16px !important;
            padding: 6px 20px !important;
            width: 410px !important;
            margin: 0 auto !important;
            display: block !important;
            background-color: #2C3E50 !important;
            color: white !important;
            border: none !important;
            border-radius: 5px !important;
        }
        .stButton>button:hover {
            background-color: #34495E !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("📬 Contact Info"):
        st.session_state.show_contact = not st.session_state.get("show_contact", True)

# ✅ Contact Info Sidebar
if st.session_state.show_contact:
    st.sidebar.header("📬 Contact Information")
    st.sidebar.write(f"📧 Email: {email}")
    st.sidebar.write(f"📞 Phone: {phone}")
    st.sidebar.write(f"📍 Address: {address}")
    
    # Social icons in the sidebar
    st.sidebar.markdown(social_icons(32, 32, LinkedIn=linkedin, GitHub=github, Email=f"mailto:{email}"), unsafe_allow_html=True)


# ✅ CV Download
try:
    with open("resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="📄 Télécharger mon CV",
                       data=PDFbyte,
                       file_name="MICHEL_SAGESSE_KOLIE_CV.pdf",
                       mime='application/pdf')
except FileNotFoundError:
    st.warning("⚠️ Fichier 'resume.pdf' introuvable. Ajoutez-le au dossier pour activer le bouton de téléchargement.")

# ✅ Navigation Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🎓 Éducation", "🚀 Compétences", "📂 Projets", "📜 Certifications", "💡 Intérêts","Contact"])

with tab1:
    st.header("🎓 Mon parcours académique")
    st.markdown("""
    - 🏅 **BAC avec la mention Très Bien** - GSP Saint Jean, N'Zérékoré (2019-2020)  
    - 📘 **Classes préparatoires** - ENSA Tétouan (2021-2023)  
    - 👨‍🎓 **Cycle Ingénieur - Data Science, IA & Big Data** - ENSA Tétouan (2023-présent)  
    """)
with tab2:
    st.header("🚀 Compétences")
    st.write("### Langages")
    st.write("Python")
    st.progress(90)
    st.write("C")
    st.progress(50)
    st.write("R")
    st.progress(50)

    st.write("### Outils & IDEs")
    st.write("VS Code, Jupyter, Visual Studio, PyCharm, Google Colab")

    st.write("### Bases de données")
    st.write("SQL, MongoDB, MySQL")

    st.write("### Autres")
    st.write("Git, Méthodes Agiles, Prétraitement de données, Visualisation des données,Security,Data Science,Big data Tools")

with tab3:
    st.header("📂 Mes projets")
    st.subheader("🧠 Projets IA & Python")
    st.markdown("""
    - 📈 Prédiction boursière avec LSTM  
    - 🏠 Estimation du prix des maisons  
    - 🤖 Système de reconnaissance faciale  
    - 💼 Prédiction de salaires par régression  
    - 🌍 Système de traduction de langues  
    - 🎬 Système de recommandation de films  
    """)

    st.subheader("💻 Projets GitHub")
    st.markdown("""
    - 🌍 Traduction de langue  
    - 🎬 Recommandation de films  
    """)

    #st.subheader("🧩 C Projects")
    

with tab4:
    st.header("📜 Certifications")
    st.write("""
    - **MLOps Concepts**
      - [View](https://www.datacamp.com/statement-of-accomplishment/course/24c0596b019268b75c8bee3a6aa3869f2420d7b1?raw=1)
    - **Understanding Cloud Computing**
      - [View](https://www.datacamp.com/completed/statement-of-accomplishment/course/c2c7770fb5a03701ed749850724f4af5a7412e49)
    """)

with tab5:
    st.header("💡 Intérêts")
    st.markdown("""
    - 🤖 Intelligence Artificielle (IA)  
    - 📊 Data Science  
    - 🧠 Apprentissage automatique (ML)  
    - 🗣️ Traitement du langage naturel (NLP)  
    - 🔬 Deep Learning  
    - 💾 Big Data  
    """)

# Content for each tab
with tab6:
    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css(r"C:\Users\user\Downloads\Projet ML\pages\style\style.css")
    #
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/michelsagesse16@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
    

# ✅ Footer
st.markdown("---")
st.write(f"Merci de votre visite ! Connectez-vous via [LinkedIn]({linkedin}) ou explorez mon [GitHub]({github}) 🚀")
