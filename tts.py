from openai import OpenAI
from pathlib import Path
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 

def tts(fileinput):
    f = open(fileinput, 'r')
    text = f.read()
    fname = fileinput.strip('.txt') + '.mp3'
    f.close()

    client = OpenAI()

    speech_file_path = Path(__file__).parent / fname
    response = client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=text
    )

    response.stream_to_file(speech_file_path)

tts('panagrams.txt')