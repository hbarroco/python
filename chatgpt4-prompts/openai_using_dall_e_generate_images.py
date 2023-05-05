import openai
openai.api_key = "Private Key"

resultado = openai.Image.create(
    prompt = "A cute yellow fish",
    n = 2,
    size = "1024x1024"
)

print(resultado)