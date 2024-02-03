# importing stuff
from openai import OpenAI

client = OpenAI(
	# defaults to os.environ.get("OPENAI_API_KEY")
	# api_key="My API Key",
)
from docx import Document


def transcribe_audio(audio_file_path):
	"""Uses the Whisper model to take in an audio file and transcribes it"""

	with open(audio_file_path, 'rb') as audio_file:
		transcription = client.audio.transcriptions.create("whisper-1", audio_file)
	return transcription['text']


def save_as_docx(transcription, filename):
    """Converts the raw text to a Word document"""
    doc = Document()
    for key, value in transcription.items():
        # Replace underscores with spaces and capitalize each word for the heading
        heading = ' '.join(word.capitalize() for word in key.split('_'))
        doc.add_heading(heading, level=1)
        doc.add_paragraph(value)
        # Add a line break between sections
        doc.add_paragraph()
    doc.save(filename)
    
audio_file_path = "Earningscall.wav"
transcription = transcribe_audio(audio_file_path)
print(transcription)

save_as_docx(transcription, 'meeting_minutes.docx')