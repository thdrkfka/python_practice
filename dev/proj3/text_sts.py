# semantix textual similarity _ 의미론적 유사도 확인

# Step 1
from sentence_transformers import SentenceTransformer

# Step 2
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 3
sentence1 = "The weather is lovely today"
sentence2 = "It's my birthday"

# 다문장
# sentences = [
#     "The weather is lovely today.",
#     "It's so sunny outside!",
#     "He drove to the stadium.",
# ]

# Step 4
embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)

print(embedding1.shape)
print(embedding2.shape)

# embeddings = model.encode(sentences)
# print(embeddings.shape)
# [3, 384]

# Step 5
similarities = model.similarity(embedding1, embedding2)
print(similarities)

# similarities = model.similarity(embeddings, embeddings)
# print(similarities)
# tensor([[1.0000, 0.6660, 0.1046],
#         [0.6660, 1.0000, 0.1411],
#         [0.1046, 0.1411, 1.0000]])