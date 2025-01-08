import streamlit as st
from openai import OpenAI
from elevenlabs import play
from elevenlabs.client import ElevenLabs

# Configuración de la página
st.set_page_config(page_title="Interfaz GPT", page_icon="🤖", layout="centered")

# Configuración de las API Keys
api_key1 = "sk-proj-10i34S5wUAheuXfHQPeCT3BlbkFJBUhEi9uTUBr8D4HfPocx"
client = OpenAI(api_key=api_key1)

client1 = ElevenLabs(
    api_key="sk_14cac717d9ad564aecc426b05e0478f77802ffd84f04d117",
)

# Sesión para mantener la memoria de la conversación
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Eres un asistente útil"}
    ]

# Logo centrado
st.image("https://via.placeholder.com/150", width=150)
st.title("Interfaz GPT")

# Campo de texto para el prompt
prompt = st.text_input("Escribe tu mensaje aquí (presiona Enter para enviar):")

if prompt:
    # Añadir mensaje del usuario a la memoria
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generar respuesta con OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.messages
    )

    assistant_response = completion.choices[0].message.content

    # Añadir respuesta del asistente a la memoria
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    # Mostrar la conversación completa
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**Tú:** {msg['content']}")
        elif msg["role"] == "assistant":
            st.markdown(f"**Asistente:** {msg['content']}")

    # Generar y reproducir audio con ElevenLabs
    audio = client1.generate(
        text=assistant_response,
        model="eleven_multilingual_v2"
    )
    play(audio)


