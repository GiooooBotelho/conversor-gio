import azure.cognitiveservices.speech as speechsdk
from config import SPEECH_SUBS_KEY, REGION

def main():
    speech_key = SPEECH_SUBS_KEY
    service_region = REGION
    
    # Configura o serviço para reconhecer Português do Brasil
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "pt-BR"  # Define o idioma para Português do Brasil

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Iniciando a gravação... Fale algo em Português do Brasil.")

    result = speech_recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Reconhecido: {result.text}")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("Não foi possível reconhecer a fala.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Reconhecimento de fala cancelado: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Erro: {cancellation_details.error_details}")

if __name__ == "__main__":
    main()