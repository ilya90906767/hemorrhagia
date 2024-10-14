from openai import OpenAI

# Set your API key
api_key = "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"

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Define the prompt
prompt = "Что такое википедия"

# Make the request to the API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
)

# Check and print the response
if response:
    result = response.choices[0].message.content
    print(result)
else:
    print("Error:", response.error)