import random
import os
import wave
import simpleaudio as sa

# Dossier principal des sons
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_PATH = os.path.join(BASE_DIR, "sounds", "compressed")

# Dossiers pour chaque type de son
SOUND_DIRECTORIES = {
    "affirmation": os.path.join(SOUND_PATH, "01_Happy_Thrilled"),
    "negation": os.path.join(SOUND_PATH, "04_Sadness_Deception"),
    "question": os.path.join(SOUND_PATH, "03_Surprise_Questionning"),
    "surprise": os.path.join(SOUND_PATH, "03_Surprise_Questionning"),
    "neutral": os.path.join(SOUND_PATH, "10_Neutral"),
}

# Charger tous les fichiers WAV une seule fois au démarrage
SOUND_FILES = {category: [] for category in SOUND_DIRECTORIES}

for category, folder in SOUND_DIRECTORIES.items():
    if os.path.exists(folder):
        SOUND_FILES[category] = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".wav")]


def get_random_sound(category):
    """Retourne un fichier audio aléatoire pour la catégorie donnée."""
    files = SOUND_FILES.get(category, [])
    
    if not files:
        #print(f"Aucun fichier trouvé pour {category}, utilisation du mode neutre.")
        return random.choice(SOUND_FILES["neutral"]) if SOUND_FILES["neutral"] else None
    
    return random.choice(files)


def play_bd1_sound(sound_file):
    #Lit un fichier WAV avec simpleaudio (plus rapide).
    if not sound_file or not os.path.exists(sound_file):
        #print("ERREUR : Fichier audio introuvable !")
        return
    
    try:
        with wave.open(sound_file, "rb") as wav_file:
            print(f"Lecture : {sound_file}")

            # Jouer le son directement sans attendre
            play_obj = sa.play_buffer(
                wav_file.readframes(wav_file.getnframes()),
                num_channels=wav_file.getnchannels(),
                bytes_per_sample=wav_file.getsampwidth(),
                sample_rate=wav_file.getframerate()
            )
            play_obj.wait_done()
            #print("Lecture terminée.")

    except wave.Error as e:
        print(f"ERREUR : Impossible de lire le fichier WAV ({e})")

def get_sound_category(text):
    #Détecte la catégorie du son en fonction du texte reçu.
    SOUND_MAP = {
        "oui": "affirmation",
        "non": "negation",
        "?": "question",
        "merci": "affirmation",
        "quoi": "question",
        "super": "affirmation",
    }

    for word, category in SOUND_MAP.items():
        if word in text.lower():
            return category

    return "neutral"

# Test avec une phrase
user_input = "Oui, c'est parfait !"
category = get_sound_category(user_input)
sound_file = get_random_sound(category)  # Retourne un son neutre si aucun son dispo

# Lire le fichier
play_bd1_sound(sound_file)