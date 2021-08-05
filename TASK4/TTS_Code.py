# This file represents the work done to use the text to speech feature using IBM service
# The main code belongs to Nicholas Renotte




# This parts includes the needed imports from ibm_watson module and ibm_cloud_sdk_core module 

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1

# This is the text to speech code, starts by defining API key variable and URL variable taken from IBM service credentials section
# Defining the authenticator and setting the service URL : 

authenticator = IAMAuthenticator('Wo6ySNvTLh1t4hYbcogC6B-108km0dWlRkqBOu2DL_vh')
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/96e07616-aaa3-406d-a585-0fd0a75c59fd')

# Using the file created from the speech to text feature named (user_speech) and modifying it (removing \n )

with open('user_speech.txt', 'r') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)


# Creating an mp3 file to save the speech and determining the voice 

with open('./audio.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)


