# Step 1. import modules
from transformers import pipeline

# Step 2. create inference isinstance
summarizer = pipeline("summarization", model="stevhliu/my_awesome_billsum_model")

# Step 3. prepare input data
text = "[파이낸셜뉴스] 당분간 시민들의 주유비 부담이 완화될 것으로 예상된다.\n 경유는 이번주 평균 가격이 1400원대로 넉 달 만에 최저 수준을 기록했으며 휘발유 가격도 5주 연속 하락했다. \n 8일 한국석유공사 유가정보시스템에 따르면 지난 2~6일 전국 주유소 휘발유 평균 판매가는 전주 대비 리터(L)당 11.5원 내린 1666.9원을 기록했다. \n 지난 달부터 5주 연속 하락한 것이다.\n 전국에서 가장 가격이 높은 서울이 13.8원 하락한 1729.4원, 가장 가격이 낮은 대구는 11원 하락한 1630.5원으로 집계됐다.\n 이번주 경유 평균 판매가격은 1497.5원으로 일주일 새 14.4원 하락했다. \n 6주 연속 하락으로, 주간 단위 1400원대에 진입한 건 지난 1월 다섯째주 이후 약 4개월 만이다. \n 국제유가 하락으로 당분간 국내 기름값도 낮아질 것으로 예상된다. \n 국제유가는 통상 2~3주 시차를 두고 국내 주유소 가격에 반영된다.\n 이번주 국제유가는 주요 산유국의 점진적 감산 완화, 미국의 경기 부진 우려 등으로 하락했다. \n두바이유는 전주 대비 4.9달러 내린 79.3달러, 국제 휘발유 가격은 3달러 내린 84.9달러를 기록했다."
#국제유가 #기름값 #주유비"

# Step 4. inference
result = summarizer(text)

# Step 5. visualize
print(result)