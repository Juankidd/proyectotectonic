# main.py
import whisper
model = whisper.load_model('large')

def get_transcribe(audio: str, language: str = 'it'):
    return model.transcribe(audio=audio, language=language, verbose=True)

if __name__ == "__main__":
    result = get_transcribe(audio='audio.wav')
    print('-'*50)
    print(result.get('text', ''))