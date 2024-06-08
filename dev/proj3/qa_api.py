from fastapi import FastAPI, Form

# step1 import module
from transformers import pipeline

# step2 create inference isinstance
question_answerer = pipeline("question-answering", model="stevhliu/my_awesome_qa_model")

app = FastAPI()


@app.post("/qa/")
async def qa(q: str = Form(), a: str = Form()):

  # step3 prepare input data
  # question = "How many programming languages does BLOOM support?"
  # context = "BLOOM has 176 billion parameters and can generate text in 46 languages natural languages and 13 programming languages."

  # step4 inference
  result = question_answerer(question=q, context=a)

  # step5 visualizes
  # print(result)

  return {"result": result}