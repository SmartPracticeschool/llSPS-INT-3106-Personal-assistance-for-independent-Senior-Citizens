from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from playsound import playsound



authenticator = IAMAuthenticator('yci1-exDJ1UrPVWahNl478_0qq3G_9D5XUagkYUqjfCj')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/f4fc8363-62dc-4947-9293-9822fdb56590')

with open('medicine.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Olmat ',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)

    audio_file.write(
        text_to_speech.synthesize(
            '  Met xl',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)
    audio_file.write(
        text_to_speech.synthesize(
            ' Aspirin  ',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)
    audio_file.write(
        text_to_speech.synthesize(
            '  Metformin  ',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)
    audio_file.write(
        text_to_speech.synthesize(
            'Linagliptin',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)

playsound('medicine.mp3')
