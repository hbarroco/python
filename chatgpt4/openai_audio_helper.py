import openai
openai.api_key = "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"

audio_file = open("audios/german1.mp3", "rb")
result = openai.Audio.translate("whisper-1", audio_file)

print(result)