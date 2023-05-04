import openai
openai.api_key = "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"

resultado = openai.Image.create(
    prompt = "A cute yellow fish",
    n = 2,
    size = "1024x1024"
)

print(resultado)