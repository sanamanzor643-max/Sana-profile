import re

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944",
    "",
    "یہ ایک مثال ہے"
]
for text in samples:
 ws = text.split()
 words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
 print("\nOriginal:", repr(text))
print("Whitespace:", ws, "Count:", len(ws))
print("Word-like:", words, "Count:", len(words))
# Model tokenizer 
try:
from sentence_transformers import SentenceTransformer
model = SentenceTransformer(
 "sentence-transformers/all-MiniLM-L6-v2",
   device="cpu"
    )
for text in samples[:2]:
    print("\nModel tokens:", model.tokenizer.tokenize(text))
except ImportError:
    print("\nSentence Transformers is not installed.")