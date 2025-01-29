import telebot
from yt_search import *
from image_download import *
from video_download import *
import mimetypes
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


API_URL = ""
bot = telebot.TeleBot("")


def send_video_to_chat(chat_id, video_path, caption=None, thumb_path=None):
	url = f"{API_URL}/sendVideo"

	video_mime_type, _ = mimetypes.guess_type(video_path)
	video_mime_type = video_mime_type or "video/mp4" 

	thumb_mime_type = None
	if thumb_path:
		thumb_mime_type, _ = mimetypes.guess_type(thumb_path)
		thumb_mime_type = thumb_mime_type or "image/jpeg" 

	with open(video_path, "rb") as video_file:
		files = {
			"video": (os.path.basename(video_path), video_file, video_mime_type),
		}

		if thumb_path:
			with open(thumb_path, "rb") as thumb_file:
				files["thumb"] = (os.path.basename(thumb_path), thumb_file, thumb_mime_type)

				data = {"chat_id": chat_id}

				if caption:
					data["caption"] = caption

				response = requests.post(url, files=files, data=data)
				if response.status_code != 200:
					print(f"Error: {response.text}")
				else:
					print("Video sent successfully")
		else:
			data = {"chat_id": chat_id}

			if caption:
				data["caption"] = caption

			response = requests.post(url, files=files, data=data)
			if response.status_code != 200:
				print(f"Error: {response.text}")
			else:
				print("Video sent successfully")




@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "To download video /video <Youtube url>\n"
						  "To send search request /search <words>\n"
						  "You can request up to 8 video:\n"
						  "example with 8 /search8\n"
						  "WARNING! /search11 will be seen as /search1, you can't request more than 8\n"
						  "except if you're willing to eddit my code")



@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
	print(call.data)
	if call.data.startswith('/video'):
		video_url = call.data.replace("/video", "")
		video_url2 = video_url.replace("_", "-")
		video_url1 = f'https://www.youtube.com/watch?v={video_url2}'

		video = url_download(video_url1)

		answer_info = search_youtube_info(video_url1)

		# duration
		time_sec = answer_info.get("duration")
		if time_sec is not None:
			time_min = time_sec // 60  
			time_sec_remainder = time_sec % 60 
			time_form_full = f"{time_min}:{time_sec_remainder:02d}"
		else:
			time_form_full = "Unknown"

		answer_ready = f"({time_form_full}) {answer_info.get('title')}"

		image_load = download_image(answer_info.get('thumbnail'))
		image_prep = prepare_thumbnail(image_load)

		try:
			if image_prep is None:
				bot.send_message(call.message.chat.id, "[Sending without thumbnail]")
				send_video_to_chat(call.message.chat.id, video, caption=answer_ready, thumb_path=None)
			else:
				bot.send_message(call.message.chat.id, "[Sending]")
				send_video_to_chat(call.message.chat.id, video, caption=answer_ready, thumb_path=image_prep)
		except BaseException as e:
			print(f"can't send: {e}")
			bot.send_message(call.message.chat.id, "Something went wrong")

@bot.message_handler(content_types=['text'])
def button_handler(message):

	if "/video " in message.text:
		try:
			video_url1 = message.text.replace("/video ", "")
		except:
			video_url1 = message.text
		video_url_id = video_id_get(video_url1)
		print(video_url_id)
		video_url = f'https://www.youtube.com/watch?v={video_url_id}'

		print(video_url)
		video = url_download(video_url)

		answer_info = search_youtube_info(video_url)

		time_sec = answer_info.get("duration")
		if time_sec is not None:
			time_min = time_sec // 60  
			time_sec_remainder = time_sec % 60  

			time_form_full = f"{time_min}:{time_sec_remainder:02d}"
		else:
			time_form_full = "Unknown"  

		answer_ready = f"({time_form_full}){answer_info.get("title")}"


		image_load = download_image(answer_info.get('thumbnail'))
		image_prep = prepare_thumbnail(image_load)
		try:
			if image_prep is None:
				bot.send_message(message.chat.id, "[Sending without thumbnail]")
				send_video_to_chat(message.chat.id, video, caption=answer_ready, thumb_path=None)
			else:
				bot.send_message(message.chat.id, "[Sending]")
				send_video_to_chat(message.chat.id, video, caption=answer_ready, thumb_path=image_prep)
		except BaseException as e:
			print(f"can't send: {e}")
			bot.send_message(message.chat.id, "Something went wrong")

	elif "/video" in message.text:
		video_url = message.text.replace("/video", "")
		video_url2 = video_url.replace("_", "-")
		video_url1 = f'https://www.youtube.com/watch?v={video_url2}'
		video = url_download(video_url1)
		answer_info = search_youtube_info(video_url1)

		time_sec = answer_info.get("duration")
		if time_sec is not None:
			time_min = time_sec // 60  
			time_sec_remainder = time_sec % 60  

			time_form_full = f"{time_min}:{time_sec_remainder:02d}"
		else:
			time_form_full = "Unknown"  
		answer_ready = f"({time_form_full}){answer_info.get("title")}"
		print("Got:   ", answer_info.get('thumbnail'))

		image_load = download_image(answer_info.get('thumbnail'))
		print("image path:  ", image_load)
		image_prep = prepare_thumbnail(image_load)
		try:
			if image_prep is None:
				bot.send_message(message.chat.id, "[Sending without thumbnail]")
				send_video_to_chat(message.chat.id, video, caption=answer_ready, thumb_path=None)
			else:
				bot.send_message(message.chat.id, "[Sending]")
				send_video_to_chat(message.chat.id, video, caption=answer_ready, thumb_path=image_prep)
		except BaseException as e:
			print(f"can't send: {e}")
			bot.send_message(message.chat.id, "Something went wrong")


	elif "/search" in message.text:
		search_amount = message.text[7]
		print(f"they ask: {search_amount}")
		any_num = True
		try:
			search_amount_to_send = int(search_amount)
		except:
			any_num = False


		if any_num:
			if int(search_amount) > 8:
				search_amount_to_send = 8
				bot.send_message(message.chat.id, "You can't ask more than 8. Asking 8")
			elif int(search_amount) <= 0:
				search_amount_to_send = 1
				bot.send_message(message.chat.id, "You can't ask 0 or lower. Asking 1")

			search_remove = f"/search{search_amount}"
			search = ""
			if message.text[8] == " ":
				search_remove1 = search_remove + " "
				search = message.text.replace(search_remove1, "")
			elif message.text[8] != " ":
				search = message.text.replace(search_remove, "")
			else:
				bot.send_message(message.chat.id, "Something went wrong. Maybe no search text?")
			get_video = search_youtube(search, search_amount_to_send)
		else:
			search1 = message.text
			search = search1.replace("/search", "")
			search_amount_to_send = 5
			get_video = search_youtube(search, search_amount_to_send)

		for i in get_video:
			answer = ""
			try:
				time_sec = int(i.get("duration"))
			except:
				time_sec = None

			try:
				title1 = i.get("title")
			except:
				title1 = "Unknown"

			if time_sec is not None:
				time_min = time_sec // 60  
				time_sec_remainder = time_sec % 60  

				time_form_full = f"{time_min}:{time_sec_remainder:02d}"
			else:
				time_form_full = "Unknown"  
			answer += f'({time_form_full}) {title1}'
			buttontext =  f'/video{video_id_get(i.get('url')).replace("-", "_")}'
			image_path = download_image(i.get('thumbnail'))
			markup = InlineKeyboardMarkup()
			button = InlineKeyboardButton("Watch", callback_data=buttontext)
			markup.add(button)
			if image_path is None:
				bot.send_message(message.chat.id, "Can't load")
			else:
				with open(image_path, "rb") as image_video:
					bot.send_photo(message.chat.id, image_video, caption=answer, reply_markup=markup)
	else:
		pass




bot.infinity_polling()
