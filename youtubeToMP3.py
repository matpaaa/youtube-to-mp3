from pytube import YouTube
from moviepy.editor import *

def convert_to_mp3(video_link):
    # Téléchargement de la vidéo depuis YouTube
    youtube = YouTube(video_link)
    video = youtube.streams.first()
    video.download()

    # Conversion de la vidéo en fichier audio MP3
    video_path = f"{video.default_filename}"
    mp3_path = f"{video_path[:-4]}.mp3"
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3_path)

    # Suppression de la vidéo originale
    video_clip.close()
    audio_clip.close()
    os.remove(video_path)

    print(f"Conversion terminée. Le fichier audio {mp3_path} a été créé.")

# Exemple d'utilisation
video_link = input("Entrez le lien de la vidéo YouTube : ")
convert_to_mp3(video_link)