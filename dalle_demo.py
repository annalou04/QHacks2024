import openai
from openai import OpenAI
client = OpenAI()


def image_prompt_from_text(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Describe this scene using the following instructions: Use contemplative and introspective verbs to create a contemplative and introspective tone. Use minimal “be” verbs. Use a distant, third person omniscient voice. Reflect on the different scents, sounds, and sights of the scene. Use many wide-ranging descriptive adjectives and nouns to create a rich, vivid, and immersive scene. Please use 100 words to describe the description topic."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']


try:
  response = client.images.create_variation(
    image=open("image_edit_mask.png", "rb"),
    n=1,
    model="dall-e-2",
    size="1024x1024"
  )
  print(response.data[0].url)
except openai.OpenAIError as e:
  print(e.http_status)
  print(e.error)