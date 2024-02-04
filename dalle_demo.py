"""
This is a demo of using DALL-E-3 to create images from an audio file for QHACKS 2024.
Author: Anna Lou
Date: February 3, 2024
"""
# import stuff
import openai
from openai import OpenAI
client = OpenAI()

def transcribe_audio(audio_file_path):
	"""Take in an audio file and transcribes it (Whisper model)"""  
	audio_file= open(audio_file_path, "rb")
	transcript = client.audio.transcriptions.create(
		model="whisper-1", 
		file=audio_file
	)
	print(transcript)
	return(transcript)


def image_prompt_from_text(transcription):
	"""Creates a text description of an transcription (ChatGPT-3.5 model)"""
	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		temperature=0,
		messages=[
			{
				"role": "system",
				"content": "Describe this scene using the following instructions: Use contemplative and introspective verbs to create a contemplative and introspective tone. Use minimal “be” verbs. Use a distant, third person omniscient voice. Reflect on the different scents, sounds, and sights of the scene. Use many wide-ranging descriptive adjectives and nouns to create a rich, vivid, and immersive scene. Please use 70 words to describe the description topic."
			},
			{
				"role": "user",
				"content": transcription
			}
		]
	)
	print(response.choices[0].message.content)

	return(response.choices[0].message.content)


def image_from_prompt(description):
	"""Creates an image from a given description (DALL-E-3 Model)"""
	try:
		response = client.images.generate(
		model="dall-e-3",
		prompt=description,
		size="1024x1792",
		quality="standard",
		n=1,
		)
		image_url = response.data[0].url
		return(image_url)
	except openai.OpenAIError as e:
		print(e.http_status)
		print(e.error)

def main():
	audio_file_path = "/Users/anna/Downloads/QHACKS24/openai-env/harvard.wav"
	transcription = transcribe_audio(audio_file_path)
	description = image_prompt_from_text(transcription)
	print(image_from_prompt(description))

	
main()
