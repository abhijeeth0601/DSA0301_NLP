import openai

api_key = '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'
openai.api_key = api_key

pr = "'Hello, How are you?'"
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=pr,
    max_tokens=5)
generated_text = response.choices[0].text.strip()
print(generated_text)
