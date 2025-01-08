from openai import OpenAI
from elevenlabs import play
from elevenlabs.client import ElevenLabs

api_key1 = "sk-proj-10i34S5wUAheuXfHQPeCT3BlbkFJBUhEi9uTUBr8D4HfPocx"

client = OpenAI(api_key = api_key1)

client1 = ElevenLabs(
  api_key="sk_14cac717d9ad564aecc426b05e0478f77802ffd84f04d117", 
)

messages = [
    {"role":"system", "content":"Eres un asistente útil"}

]

while True:
    user_input = input("Tu: ")

    if user_input.lower() == "salir":
        break
    messages.append({"role":"user","content":user_input})

    completion = client.chat.completions.create(
        model = "gpt-4o",
        messages = messages

    )

    assistant_response = completion.choices[0].message.content
    print(f"Assistant:{assistant_response}")

    audio = client1.generate(
    text=assistant_response,
    model="eleven_multilingual_v2"
    )
    play(audio)

