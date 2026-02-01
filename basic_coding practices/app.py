import tiktoken

# Choose encoding (for OpenAI models)
encoding = tiktoken.get_encoding("gpt-4o-mini")

text = "Hello, how are you?"

tokens = encoding.encode(text)
decoded = encoding.decode(tokens)

print("Original text:", text)
print("Tokens:", tokens)
print("Number of tokens:", len(tokens))
print("Decoded text:", decoded)


