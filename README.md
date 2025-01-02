# YouTube to MP3 Downloader

A simple Python-based YouTube to MP3 downloader that uses `yt-dlp` for downloading audio files and converts them into high-quality MP3s using FFmpeg. This project is perfect for saving your favorite songs or audio from YouTube videos.

---

## Features
- Downloads audio from YouTube videos in the best available quality.
- Converts audio to MP3 format using FFmpeg.
- Saves files to a user-specified location (default: `C:\Users\dhruv\Music\PunjabiSongs`).
- Automatically creates the save directory if it doesn't exist.

---

## Prerequisites

Before running the project, ensure you have the following installed on your system:

1. **Python 3.7 or later**
   - Download and install Python from [Python.org](https://www.python.org/).
2. **yt-dlp**
   - Install using pip:
     ```bash
     pip install yt-dlp
     ```
3. **FFmpeg**
   - Download precompiled binaries from [FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/).
   - Extract and add the `bin` folder to your system PATH. Verify installation:
     ```bash
     ffmpeg -version
     ```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/dumpsterdj/youtube-to-mp3-downloader.git
   cd youtube-to-mp3-downloader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the script with a YouTube URL:
   ```bash
   python mp3.py "<YouTube URL>"
   ```

2. The MP3 file will be saved to the default location:
   ```
   C:\Users\dhruv\Music\PunjabiSongs
   ```

3. To specify a custom save location, modify the `save_path` variable in `mp3.py`.

---

## Example

Command:
```bash
python mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Output:
```
File saved at: C:\Users\dhruv\Music\PunjabiSongs\Never Gonna Give You Up.mp3
```

---

## Troubleshooting

- **Error: `ffprobe and ffmpeg not found`**  
  Ensure FFmpeg is installed and its `bin` folder is added to your system PATH.

- **Invalid URL**  
  Make sure the provided YouTube URL is correct and publicly accessible.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to suggest new features or improvements.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Developed by **[@dumpsterdj](https://github.com/dumpsterdj)**.  
Feel free to connect for any questions or feedback!

---

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)
