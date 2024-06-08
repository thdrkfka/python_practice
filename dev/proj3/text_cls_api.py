from fastapi import FastAPI, Form

# Step 1. import modules # 모듈 import
from transformers import pipeline

# Step 2. create inference isinstance # 추론기 생성
classifier = pipeline("sentiment-analysis", model="snunlp/KR-FinBert-SC") # 긍/부정 분류

app = FastAPI()


@app.post("/text/")
async def text(text: str = Form()):
    
  # Step 3. prepare input data # 입력값 준비
  # text = "[오늘의 주목주] '최태원 TSMC와 회담'에 SK 10%대 상승, 에스티팜 15% 뛰어"

  # Step 4. infrence # 추론
  result = classifier(text)

  # Step 5. visualize # 후처리
  # print(result)

  return {"result": result}