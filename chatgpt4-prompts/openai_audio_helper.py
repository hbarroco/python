import openai
openai.api_key = "Private Key"

audio_file = open("audios/german1.mp3", "rb")
result = openai.Audio.translate("whisper-1", audio_file)

print(result)