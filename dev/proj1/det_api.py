from fastapi import FastAPI, File, UploadFile

# STEP 1: Import the necessary modules. # 
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: Create an ObjectDetector object. # detecter 추론기 만들기.
base_options = python.BaseOptions(model_asset_path='models\\efficientdet_lite0.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,score_threshold=0.5)
                                        # 모델 정보
detector = vision.ObjectDetector.create_from_options(options)


app = FastAPI()

import io
import PIL

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    
    byte_file = await file.read()

    # STEP 3: Load the input image. # 추론할 데이터 가져오기(이미지)
    # image = mp.Image.create_from_file(IMAGE_FILE)

    image_bin = io.BytesIO(byte_file)
    pil_img = PIL.Image.open(image_bin)
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_img))


    # STEP 4: Detect objects in the input image. # 추론
    detection_result = detector.detect(image)
    print(detection_result)

    # DetectionResult(detections=[Detection(bounding_box=BoundingBox(origin_x=72, origin_y=162, width=252, height=191), 
    #                                       categories=[Category(index=None, score=0.7798683643341064, display_name=None, category_name='cat')], 
    #                                       keypoints=[]),
    #                              Detection(bounding_box=BoundingBox(origin_x=303, origin_y=27, width=248, height=344), 
    #                                        categories=[Category(index=None, score=0.7624295949935913, display_name=None, category_name='dog')],
    #                                          keypoints=[])])

    # STEP 5: Process the classification result. In this case, visualize it. # 추론한 결과 보여주는 후처리단 # 프로젝트 진행한다면, json으로 변경해서 보여주기
    # top_category = classification_result.classifications[0].categories[0]

    results = []
    for detection in detection_result.detections:
        print("detection list 뽑기")
        print(f"detection list : {detection}")

        # detection list 뽑기
        # Detection(bounding_box=BoundingBox(origin_x=72, origin_y=162, width=252, height=191),
        #            categories=[Category(index=None, score=0.7798683643341064, display_name=None, category_name='cat')],
        #              keypoints=[])
        # detection list 뽑기
        # Detection(bounding_box=BoundingBox(origin_x=303, origin_y=27, width=248, height=344),
        #            categories=[Category(index=None, score=0.7624295949935913, display_name=None, category_name='dog')],
        #              keypoints=[])

        results.append(detection.categories[0].category_name)
    return{"result": results}
