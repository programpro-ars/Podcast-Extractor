from pytube import YouTube
from pytube import Playlist
import os


def download_audio(link, directory=""):
    if link.find("playlist") != -1:
        playlist = Playlist(link)
        os.mkdir(playlist.title)
        print("Downloading Playlist (" + str(playlist.length) + " videos):\n")
        i = 1
        for video in playlist.videos:
            (video.streams.filter(mime_type="audio/mp4", only_audio=True)[-1]
             .download(os.path.join(directory, playlist.title)))
            print("Audio from", video.title, "was extracted")
            i += 1
        print("\nAll audios were successfully extracted.")
    else:
        video = YouTube(link)
        video.streams.filter(mime_type="audio/mp4", only_audio=True)[-1].download(directory)
        print("Audio from", video.title, "was successfully extracted.")


if __name__ == "__main__":
    link = input("Link: ")
    destination = input("Destination: ")
    download_audio(link, destination)
    