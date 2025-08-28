#!/usr/bin/env python3
"""
Script d'optimisation des vidéos pour le portfolio
Optimise automatiquement les vidéos MP4 pour le web
"""

import os
import subprocess
import sys
from pathlib import Path

def check_ffmpeg():
    """Vérifie si FFmpeg est installé"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def optimize_video(input_path, output_path, crf=23, preset='medium'):
    """
    Optimise une vidéo avec FFmpeg
    
    Args:
        input_path (str): Chemin vers la vidéo d'entrée
        output_path (str): Chemin vers la vidéo optimisée
        crf (int): Constante Rate Factor (18-28, plus bas = meilleure qualité)
        preset (str): Preset de compression (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow)
    """
    cmd = [
        'ffmpeg',
        '-i', input_path,
        '-c:v', 'libx264',
        '-crf', str(crf),
        '-preset', preset,
        '-c:a', 'aac',
        '-b:a', '128k',
        '-movflags', '+faststart',
        '-y',  # Écraser le fichier de sortie s'il existe
        output_path
    ]
    
    try:
        print(f"Optimisation de {input_path}...")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f" Vidéo optimisée : {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'optimisation de {input_path}: {e}")
        print(f"Sortie d'erreur: {e.stderr}")
        return False

def get_file_size_mb(file_path):
    """Retourne la taille du fichier en MB"""
    if os.path.exists(file_path):
        return round(os.path.getsize(file_path) / (1024 * 1024), 2)
    return 0

def main():
    """Fonction principale"""
    print("🎬 Optimiseur de Vidéos pour Portfolio")
    print("=" * 50)
    
    # Vérifier FFmpeg
    if not check_ffmpeg():
        print("❌ FFmpeg n'est pas installé ou n'est pas dans le PATH")
        print("📥 Installez FFmpeg depuis: https://ffmpeg.org/download.html")
        return
    
    # Vidéos attendues
    expected_videos = [
        "stock_prediction.mp4",
        "house_price.mp4", 
        "face_recognition.mp4",
        "movie_recommendation.mp4"
    ]
    
    # Créer le dossier optimized s'il n'existe pas
    optimized_dir = Path("optimized_videos")
    optimized_dir.mkdir(exist_ok=True)
    
    print(f"📁 Dossier d'optimisation: {optimized_dir}")
    print()
    
    # Traiter chaque vidéo
    for video_name in expected_videos:
        input_path = Path(video_name)
        
        if not input_path.exists():
            print(f"⚠️  Vidéo non trouvée: {video_name}")
            continue
        
        output_path = optimized_dir / f"optimized_{video_name}"
        
        # Afficher les informations de la vidéo originale
        original_size = get_file_size_mb(input_path)
        print(f"📹 {video_name}")
        print(f"   Taille originale: {original_size} MB")
        
        # Optimiser la vidéo
        if optimize_video(str(input_path), str(output_path)):
            optimized_size = get_file_size_mb(output_path)
            reduction = round((original_size - optimized_size) / original_size * 100, 1)
            print(f"   Taille optimisée: {optimized_size} MB")
            print(f"   Réduction: {reduction}%")
        else:
            print(f"   ❌ Échec de l'optimisation")
        
        print()
    
    print("🎉 Optimisation terminée!")
    print(f"📂 Vidéos optimisées dans: {optimized_dir}")
    print()
    print("💡 Conseils:")
    print("   - Remplacez les vidéos originales par les optimisées")
    print("   - Vérifiez la qualité avant de remplacer")
    print("   - Les vidéos optimisées sont prêtes pour le web")

if __name__ == "__main__":
    main()
