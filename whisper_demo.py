"""
This is a demo of using Whisper-1 to create text from an audio file, and save it to a Word document for QHACKS 2024.
Author: Anna Lou
Date: February 3, 2024
"""
# import stuff
import openai
from openai import OpenAI
client = OpenAI()
from docx import Document


def transcribe_audio(audio_file_path):
	"""Take in an audio file and transcribes it (Whisper model)"""  
	audio_file= open(audio_file_path, "rb")
	transcript = client.audio.transcriptions.create(
		model="whisper-1", 
		file=audio_file
	)
	print(transcript)
	stripped_transcript = str(transcript)[20:-2]
	return(stripped_transcript)

def save_as_docx(transcription, filename):
	"""Converts the raw text to a Word document"""
	doc = Document()
	doc.add_paragraph(str(transcription))
	doc.save(filename)

# Change this variable to the path your audio is in
audio_file_path = "/Users/anna/Downloads/QHACKS24/QHacks2024/harvard.wav"

# converts the audio into text
transcription = transcribe_audio(audio_file_path)

# change the name to whatever you want the name of the file to be
save_as_docx(transcription, 'text_from_audio.docx')
