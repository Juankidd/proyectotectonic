from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="sk_14cac717d9ad564aecc426b05e0478f77802ffd84f04d117", # Defaults to ELEVEN_API_KEY or ELEVENLABS_API_KEY
)

audio = client.generate(
  text="""Gracias productor por usar SmartNode, con base a los datos recolectados
  del sistema IoT, los rangos recomendados para mejorar la productividad son:
  Temperatura: 22 a 24 grados celsius, Humedad: 75 a 77 %, Luminosidad: 89%""",
  model="eleven_multilingual_v2"
)
play(audio)

