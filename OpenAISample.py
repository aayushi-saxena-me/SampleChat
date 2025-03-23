from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
