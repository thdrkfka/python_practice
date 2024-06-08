# hugginface/transformers => 자연어 # model을 알아서 다운받아줌. -> user/.chache/huggingface

# huggingface 에서의 Step5
# Step 1. import modules # 모듈 import
from transformers import pipeline
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
                                        # sequence 단위의 데이터를 분류

# Step 2. create inference isinstance # 추론기 생성
classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model") # 긍/부정 분류
            #  pipeline (task 이름, model 이름)

# Step 3. prepare input data # 입력값 준비
text = "bad request."

# Step 4. infrence # 추론
result = classifier(text)

# Step 5. visualize # 후처리
print(result)



# pipeline 없거나 쓰지 않을 때
# Step 2.
# tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_model")
# model = AutoModelForSequenceClassification.from_pretrained("stevhliu/my_awesome_model")

# # Step 4. 
# inputs = tokenizer(text, return_tensors="pt")
# with torch.no_grad():
#     logits = model(**inputs).logits

# 4-1. preprocessing(data -> tensor(blob)) # 사람이 읽을 수 있는 데이터를 모델이 읽을 수 있는 데이터로 변경
# 4-2. inference(tensor(blog) -> logit) # 추론
# 4-3. postprocessing(logit -> data) # 사람이 읽을 수 있는 데이터로 변경



# pytorch 설치 후, 아래와 같은 에러 발생 시 => conda install chardet 설치
# ImportError: cannot import name 'get_full_repo_name' from 'huggingface_hub' (C:\Users\user\miniconda3\envs\proj3\Lib\site-packages\huggingface_hub\__init__.py)
