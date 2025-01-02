import os
import yt_dlp as youtube_dl

def download_mp3(url):
    """
    Downloads the audio of a YouTube video as an MP3 file and saves it to the specified directory.
    """
    save_path = r'C:\Users\dhruv\Music\PunjabiSongs'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': r'C:\ffmpeg\bin',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python mp3.py <YouTube URL>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    download_mp3(youtube_url)
