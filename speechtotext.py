import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('DhIN3LWVXzaNTbEZ1X2Shm12o12-bxUSNZgCQ3QbfVPI')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/d8ae2efd-eedd-4749-a50d-e7a35b49e52e')

with open(join(dirname(__file__), './.', 'medicine.mp3'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
        
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))
