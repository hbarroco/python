import openai
openai.api_key = "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"

resultado = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the between Campinas and São Paulo"}]
)

print(resultado)

#print('Hello only test')