import yt_dlp
from video_download import video_id_get


def search_youtube(query, search_amount):

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'noplaylist': True,
        'extract_flat': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch{search_amount}:{query}", download=False)
        videos = []
        if 'entries' in search_results:
            for entry in search_results['entries']:
                video_id = video_id_get(entry.get('url'))
                thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
                videos.append({
                    'title': entry.get('title'),
                    'url': entry.get('url'),
                    'thumbnail': thumbnail_url,
                    'duration': entry.get('duration')
                })
        print("asked:", len(videos))
        return videos

def search_youtube_info(url):

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'noplaylist': True,
        'extract_flat': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results1 = ydl.extract_info(url, download=False)
        video_id = video_id_get(url)
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        videos = {
            'title': search_results1.get('title'),
            'thumbnail': thumbnail_url,
            'url': search_results1.get('url'),
            'duration': search_results1.get('duration')}
        print("asked load info:", search_results1.get('title'))
        print(videos)
        return videos