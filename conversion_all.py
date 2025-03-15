import os
import shutil
import subprocess

# Chemins des dossiers
base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")
input_dir = os.path.join(base_dir, "uncompressed")
output_dir = os.path.join(base_dir, "compressed")

# 1️⃣ Supprimer complètement compressed/ s'il existe
if os.path.exists(output_dir):
    print("🗑️ Suppression de l'ancien dossier 'compressed/'...")
    shutil.rmtree(output_dir)

# 2️⃣ Recréer le dossier compressed/
os.makedirs(output_dir)

# 3️⃣ Trouver et convertir tous les fichiers WAV de manière récursive
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.lower().endswith(".wav"):
            # Chemin absolu du fichier d'origine
            input_path = os.path.join(root, file)

            # Créer le même chemin dans compressed/
            relative_path = os.path.relpath(root, input_dir)  # Récupérer le sous-dossier relatif
            output_folder = os.path.join(output_dir, relative_path)

            # Créer les sous-dossiers s'ils n'existent pas
            os.makedirs(output_folder, exist_ok=True)

            # Chemin du fichier converti
            output_path = os.path.join(output_folder, file)

            print(f"🎵 Conversion de {input_path}...")

            # Commande FFmpeg pour convertir en PCM 16-bit
            command = [
                "ffmpeg", "-i", input_path,
                "-acodec", "pcm_s16le", "-ar", "44100",
                output_path
            ]

            # Exécuter la commande (supprime les logs pour éviter le spam)
            subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print(f"✅ Fichier converti : {output_path}")

print("🚀 Conversion terminée pour tous les fichiers !")