import yt_dlp
from pydub import AudioSegment
import os

DOWNLOAD_DIR = 'downloads'  # Fix 1: was 'downloades' (typo)
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_youtube_audio(url: str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")  # Fix 2: was 'outpath_path' (typo)
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,  # Fix 2: corrected variable name
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        # Fix 3: replace ALL possible source extensions, not just .webm and .m4a
        for ext in [".webm", ".m4a", ".mp4", ".opus", ".ogg"]:
            filename = filename.replace(ext, ".wav")
        return filename

#converting to monoaudio and 16kHz sample rate
def convert_to_wav(input_path: str) -> str:
    """Convert any audio/file to WAV format using pydub."""
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000) #16000Hz
    audio.export(output_path, format="wav")
    return output_path

#chunking breaking the video into 10 minutes and then creating a list and append one by one 
def chunk_audio(wav_path: str, chunk_minutes: int = 10) -> list:
    audio = AudioSegment.from_wav(wav_path)
    chunk_ms = chunk_minutes * 60 * 1000 #Convert minutes to miliseconds
    
    chunks = []
    
    for i, start in enumerate(range(0, len(audio),chunk_ms)):
        chunk = audio[start : start + chunk_ms]
        chunk_path = f"{wav_path}_chunk_{i}.wav"
        chunk.export(chunk_path)
        
        chunks.append(chunk_path)
        
    return chunks   

#A trigger function for the user to paste the link 
def process_input(source: str) -> list:
    if source.startswith("http://") or source.startswith("https://"):
        print("Detected Youtube URL. Downloading audio...")
        wav_path = download_youtube_audio(source)
    else:
        print("Detected local file. Converting to WAV...")
        wav_path = convert_to_wav(source)

    print("Chunking audio...")
    chunks = chunk_audio(wav_path)
    print(f"Audio ready -- {len(chunks)} chunks created.")    
    return chunks
