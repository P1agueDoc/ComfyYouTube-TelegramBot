import requests
import os
from PIL import Image

def download_image(url):

    save_file = "save"
    print(url)
    os.makedirs(save_file, exist_ok=True)
    image = requests.get(url)

    url_name = url.split("/")
    print(url_name)
    image_path = os.path.join(save_file, url_name[len(url_name) - 2] + ".jpg",)
    print(image_path)

    if image.status_code == 200:
        with open(image_path, "wb") as file:
            file.write(image.content)
        return image_path
    else:
        print("error: not 200")
        return None


def prepare_thumbnail(thumb_path):
    try:
        if thumb_path is not None and os.path.exists(thumb_path):  # Check if the file exists
            print("thumb path loaded correctly")
            directory, original_name = os.path.split(thumb_path)
            prepared_name = f"prep_{os.path.splitext(original_name)[0]}.jpg"
            prepared_thumb_path = os.path.join(directory, prepared_name)

            with Image.open(thumb_path) as img:
                print("thumb path loaded correctly and getting prepared")
                img.thumbnail((320, 320))  # Resize to 320x320
                img.convert("RGB").save(prepared_thumb_path, "JPEG", quality=85)  # Convert to JPEG and save

            return prepared_thumb_path
        else:
            print("Failed image prep. Possible None as path or file does not exist")
            return None
    except Exception as e:
        print(f"Failed image prep: {e}")
        return None
