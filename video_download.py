import yt_dlp
import os



def video_id_get(url):
    if "www.youtube.com/watch" in url:
        new_id = url.replace("https://www.youtube.com/watch?v=", "")
        if "&" in new_id:
            new_id2 = new_id.split("&", 1)[0]
            return new_id2
        else:
            return new_id

    elif "https://youtu.be/" in url:
        new_id = url.replace("https://youtu.be/", "")
        if "?" in new_id:
            new_id2 = new_id.split("?", 1)[0]
            return new_id2
        else:
            return new_id

    elif "https://open.spotify.com/track/" in url:
        new_id = url.replace("https://open.spotify.com/track/", "")
        if "?" in new_id:
            new_id2 = new_id.split("?", 1)[0]
            return new_id2
        else:
            return new_id

    elif "https://music.youtube.com/watch?v=" in url:
        new_id = url.replace("https://music.youtube.com/watch?v=", "")
        if "&" in new_id:
            new_id2 = new_id.split("&", 1)[0]
            return new_id2
        else:
            return new_id

    elif "https://www.youtube.com/shorts/" in url:
        new_id = url.replace("https://www.youtube.com/shorts/", "")
        if "?" in new_id:
            new_id2 = new_id.split("?",1)[0]
            return new_id2
        else:
            return new_id

    else:
        return None

def url_download(url):
    output_dir = "save"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "%(title)s.%(ext)s")

    ydl_opts = {
        'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/mp4',
        'outtmpl': output_path,
        'cookiefile': r"Please enter path to cookies.txt. If same path then write name of file like cookies.txt",
        'merge_output_format': 'mp4',
        'get_filesize': True,
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print("I load: ", url)
            result = ydl.extract_info(url, download=False)
            video_duration = result.get('duration', 0)  # Duration in seconds

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(url, download=True)
                file_path = ydl.prepare_filename(result)  # Returns the actual file path
                return file_path

        except yt_dlp.utils.DownloadError as e:
            print(f"Error downloading video: {e}")
            return None