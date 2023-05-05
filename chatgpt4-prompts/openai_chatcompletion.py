import openai
openai.api_key = "Private Key"

resultado = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the between Campinas and São Paulo"}]
)

print(resultado)

#print('Hello only test')