import os

keys = [
    "ANTHROPIC_API_KEY",
    "OPENAI_API_KEY",
    "HUGGINGFACE_API_KEY",
]

for key in keys:
    value = os.getenv(key)
    if value:
        print(f"{key}: set, length={len(value)}")
    else:
        print(f"{key}: not set")
        