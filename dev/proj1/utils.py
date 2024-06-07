import urllib.request

IMAGE_FILENAMES = ['burger.jpg', 'cat.jpg']

for name in IMAGE_FILENAMES:
  url = f'https://storage.googleapis.com/mediapipe-tasks/image_classifier/{name}'
  urllib.request.urlretrieve(url, name)

  # 파이썬으로 이미지 파일 다운로드
  # 경로를 바꾸면 임의의 파일 새롭게 다운 받을 수도 있음. 없으면 에러남.
  # 모델 가져왔고 테스트할 이미지 가져옴.