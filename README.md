# Portfolio Michel Sagesse Kolié

Un portfolio moderne et interactif développé avec **Streamlit** et **Python**, présentant mes compétences en Data Science, Intelligence Artificielle et Big Data.

## Fonctionnalités

-  **Design moderne** avec animations et transitions fluides
-  **Responsive** - Optimisé pour tous les appareils
-  **Graphiques interactifs** avec Plotly
-  **Navigation intuitive** avec onglets organisés
-  **Barres de compétences** animées
- **Gestion d'images** optimisée
- **Formulaire de contact** fonctionnel
- **Mode sombre/clair** (optionnel)
- **Vidéos de démonstration** pour chaque projet
- ** Images des certifications** personnalisées

## Technologies Utilisées

- **Frontend**: Streamlit, HTML/CSS
- **Visualisation**: Plotly
- **Traitement d'images**: Pillow (PIL)
- **Langage**: Python 3.8+

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/MichelSagesse/portfolio.git
   cd portfolio
   ```

2. **Créer un environnement virtuel** (recommandé)
   ```bash
   python -m venv venv
   
   # Sur Windows
   venv\Scripts\activate
   
   # Sur macOS/Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Lancement

### Mode développement
```bash
python -m streamlit run portfolioCV.py
```

### Mode production
```bash
python -m streamlit run portfolioCV.py --server.port 8501 --server.address 0.0.0.0
```

Le portfolio sera accessible à l'adresse : `http://localhost:8501`

## Structure du Projet

```
portfolio/
├── portfolioCV.py          # Application principale
├── style.css              # Styles CSS personnalisés
├── requirements.txt       # Dépendances Python
├── README.md             # Documentation
├── resume.pdf            # CV (à ajouter)
├── michel.jpeg           # Photo de profil
├── stock_prediction.jpg  # Images des projets
├── house_price.jpg
├── face_recognition.jpg
├── movie_recommendation.jpg
├── stock_prediction.mp4  # Vidéos de démonstration
├── house_price.mp4
├── face_recognition.mp4
├── movie_recommendation.mp4
├── images/               # Images des certifications
│   ├── mlops_datacamp.png
│   ├── cloud_computing_datacamp.png
│   └── deep_learning_coursera.png
└── optimized_videos/     # Vidéos optimisées (optionnel)
```

## Ajout des Vidéos de Démonstration

### Format des Vidéos
- **Format**: MP4 (recommandé)
- **Résolution**: 720p ou 1080p
- **Durée**: 1-3 minutes par projet
- **Taille**: Optimiser pour le web (< 50MB par vidéo)

### Noms des Fichiers Vidéo
Ajoutez vos vidéos dans le dossier `portfolio/` avec les noms suivants :

| Projet | Nom du fichier vidéo |
|--------|---------------------|
| Système de Prédiction Boursière | `stock_prediction.mp4` |
| Estimateur de Prix Immobilier | `house_price.mp4` |
| Système de Reconnaissance Faciale | `face_recognition.mp4` |
| Système de Recommandation de Films | `movie_recommendation.mp4` |

### Contenu Recommandé pour les Vidéos
1. **Introduction** (10-15 secondes)
   - Nom du projet
   - Objectif principal

2. **Démonstration** (1-2 minutes)
   - Fonctionnalités principales
   - Interface utilisateur
   - Résultats obtenus

3. **Conclusion** (10-15 secondes)
   - Technologies utilisées
   - Résultats finaux

### Optimisation des Vidéos
```bash
# Avec FFmpeg (recommandé)
ffmpeg -i video_original.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k video_optimise.mp4

# Paramètres recommandés
# - crf 23: Qualité équilibrée
# - preset medium: Compression équilibrée
# - b:a 128k: Audio de qualité web
```

##  Ajout des Images des Certifications

### Format des Images
- **Format**: PNG ou JPG (recommandé)
- **Résolution**: 200x200px minimum
- **Taille**: < 2MB par image
- **Style**: Logos officiels des plateformes

### Noms des Fichiers Images
Ajoutez vos images dans le dossier `images/` avec les noms suivants :

| Certification | Nom du fichier image |
|---------------|---------------------|
| MLOps Concepts (DataCamp) | `mlops_datacamp.png` |
| Understanding Cloud Computing (DataCamp) | `cloud_computing_datacamp.png` |
| Deep Learning Specialization (Coursera) | `deep_learning_coursera.png` |

### Sources des Images
- **DataCamp**: Téléchargez depuis votre dashboard DataCamp
- **Coursera**: Téléchargez depuis votre profil Coursera
- **Autres plateformes**: Utilisez les logos officiels

### Optimisation des Images
```bash
# Avec Python Pillow
from PIL import Image

# Redimensionner et optimiser
img = Image.open("certification.png")
img = img.resize((200, 200), Image.LANCZOS)
img.save("certification_optimized.png", optimize=True, quality=85)
```

## Personnalisation

### Modifier les informations personnelles
Éditez la section `PORTFOLIO_DATA` dans `portfolioCV.py` :

```python
PORTFOLIO_DATA = {
    "personal": {
        "name": "Votre Nom",
        "title": "Votre Titre",
        "email": "votre.email@example.com",
        # ... autres informations
    },
    # ... autres sections
}
```

### Modifier le style
Éditez le fichier `style.css` pour personnaliser :
- Couleurs et thème
- Animations
- Mise en page
- Responsive design

### Ajouter des projets
Ajoutez vos projets dans la section `projects` de `PORTFOLIO_DATA` :

```python
{
    "title": "Nom du Projet",
    "description": "Description du projet",
    "image": "image_du_projet.jpg",
    "technologies": ["Python", "TensorFlow", "..."],
    "github": "https://github.com/...",
    "video": "nom_du_projet.mp4",
    "category": "AI/ML"
}
```

### Ajouter des certifications
Ajoutez vos certifications dans la section `certifications` de `PORTFOLIO_DATA` :

```python
{
    "title": "Nom de la Certification",
    "issuer": "Plateforme",
    "date": "2024",
    "link": "https://lien-vers-certification.com",
    "image": "nom_de_l_image.png"
}
```

## Sections du Portfolio

1. **🏠 Accueil** - Présentation et vue d'ensemble
2. **🎓 Éducation** - Parcours académique
3. **💼 Expérience** - Expérience professionnelle
4. **🚀 Compétences** - Compétences techniques et soft skills
5. **📂 Projets** - Projets réalisés avec vidéos de démonstration
6. **📜 Certifications** - Certifications obtenues avec images
7. **📩 Contact** - Informations de contact et formulaire

## Configuration Avancée

### Variables d'environnement
Créez un fichier `.env` pour les configurations sensibles :

```env
EMAIL_SERVICE=formsubmit
CONTACT_EMAIL=votre.email@example.com
```

### Déploiement
Le portfolio peut être déployé sur :
- **Streamlit Cloud** (recommandé)
- **Heroku**
- **VPS personnel**
- **Docker**

### Exemple de déploiement Streamlit Cloud
1. Poussez votre code sur GitHub
2. Connectez-vous à [share.streamlit.io](https://share.streamlit.io)
3. Sélectionnez votre repository
4. Configurez le fichier principal : `portfolioCV.py`
5. Déployez !

##  Fonctionnalités Avancées

- **Graphiques interactifs** : Visualisation des compétences avec Plotly
- **Animations CSS** : Transitions fluides et effets visuels
- **Responsive design** : Adaptation automatique aux écrans
- **Optimisation des images** : Chargement optimisé des images
- **Formulaire de contact** : Intégration avec FormSubmit
- **Navigation par onglets** : Organisation claire du contenu
- **🎬 Vidéos intégrées** : Démonstrations visuelles des projets
- ** Images des certifications** : Logos officiels des plateformes
- **Mode sombre** : Interface adaptative



## Licence



## Contact

- **Email**: michelsagesse16@gmail.com
- **LinkedIn**: [Michel Sagesse Kolié](https://www.linkedin.com/in/michel-sagesse-koli%C3%A9-9313a9281/)
- **GitHub**: [MichelSagesse](https://github.com/MichelSagesse)

---

N'hésitez pas à donner une étoile si ce portfolio vous a été utile !
