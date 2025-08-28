#!/usr/bin/env python3
"""
Script d'optimisation des images pour le portfolio
Optimise automatiquement les images des certifications
"""

import os
from PIL import Image, ImageOps
from pathlib import Path

def optimize_certification_image(input_path, output_path, size=(200, 200), quality=85):
    """
    Optimise une image de certification
    
    Args:
        input_path (str): Chemin vers l'image d'entrée
        output_path (str): Chemin vers l'image optimisée
        size (tuple): Taille de sortie (largeur, hauteur)
        quality (int): Qualité JPEG (1-100)
    """
    try:
        # Ouvrir l'image
        img = Image.open(input_path)
        
        # Convertir en RGB si nécessaire
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        
        # Redimensionner en conservant les proportions
        img.thumbnail(size, Image.LANCZOS)
        
        # Créer une nouvelle image avec la taille exacte
        new_img = Image.new('RGB', size, (255, 255, 255))
        
        # Centrer l'image
        offset = ((size[0] - img.size[0]) // 2, (size[1] - img.size[1]) // 2)
        new_img.paste(img, offset)
        
        # Sauvegarder avec optimisation
        new_img.save(output_path, 'PNG', optimize=True)
        
        return True
    except Exception as e:
        print(f"Erreur lors de l'optimisation de {input_path}: {e}")
        return False

def get_file_size_kb(file_path):
    """Retourne la taille du fichier en KB"""
    if os.path.exists(file_path):
        return round(os.path.getsize(file_path) / 1024, 2)
    return 0

def main():
    """Fonction principale"""
    print("🖼️ Optimiseur d'Images pour Portfolio")
    print("=" * 50)
    
    # Images attendues
    expected_images = [
        "mlops_datacamp.png",
        "cloud_computing_datacamp.png",
        "deep_learning_coursera.png"
    ]
    
    # Créer le dossier images s'il n'existe pas
    images_dir = Path("images")
    images_dir.mkdir(exist_ok=True)
    
    # Créer le dossier optimized s'il n'existe pas
    optimized_dir = Path("optimized_images")
    optimized_dir.mkdir(exist_ok=True)
    
    print(f" Dossier d'images: {images_dir}")
    print(f" Dossier d'optimisation: {optimized_dir}")
    print()
    
    # Traiter chaque image
    for image_name in expected_images:
        input_path = images_dir / image_name
        
        if not input_path.exists():
            print(f" Image non trouvée: {image_name}")
            print(f"   Placez l'image dans le dossier: {images_dir}")
            continue
        
        output_path = optimized_dir / f"optimized_{image_name}"
        
        # Afficher les informations de l'image originale
        original_size = get_file_size_kb(input_path)
        print(f"{image_name}")
        print(f"   Taille originale: {original_size} KB")
        
        # Optimiser l'image
        if optimize_certification_image(str(input_path), str(output_path)):
            optimized_size = get_file_size_kb(output_path)
            reduction = round((original_size - optimized_size) / original_size * 100, 1)
            print(f"   Taille optimisée: {optimized_size} KB")
            print(f"   Réduction: {reduction}%")
        else:
            print(f" Échec de l'optimisation")
        
        print()
    
    print("Optimisation terminée!")
    print(f"Images optimisées dans: {optimized_dir}")
    print()
    print("Conseils:")
    print("   - Remplacez les images originales par les optimisées")
    print("   - Vérifiez la qualité avant de remplacer")
    print("   - Les images optimisées sont prêtes pour le web")
    print()
    print(" Format recommandé:")
    print("   - Taille: 200x200 pixels")
    print("   - Format: PNG")
    print("   - Taille fichier: < 100 KB")

if __name__ == "__main__":
    main()
