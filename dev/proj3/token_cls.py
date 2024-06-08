# step1
from transformers import pipeline

# step2
classifier = pipeline("ner", model="stevhliu/my_awesome_wnut_model")

# step3
text = "The Golden State Warriors are an American professional basketball team based in San Francisco."

# step4
result = classifier(text)

# step5
print(result)