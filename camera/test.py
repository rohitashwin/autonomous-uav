from calibrate_camera import undistort_image
from object_detection import detect_all_targets, prepare_target_images
from cv_utilities import draw_image_objects
from utils import time_elapsed
from transformations import get_img_center
import numpy as np
import cv2

PIPELINE_TARGET_N_PATH = "targets/target_n.jpg"
PIPELINE_TARGET_R_PATH = "targets/target_r.jpg"
PIPELINE_TARGET_HELI_PATH = "targets/helipad.jpg"

# UNDISTORT TEST

# img = cv2.imread('test.jpg')
# print(img.shape)
# img = undistort_image(img)
# cv2.imwrite('und.jpg', img)



# OBJECT DETECTION full pipeline TEST
paths = [
    # "test/phone/easy1.png",
    # "test/phone/easy2.png",
    # "test/phone/easy3.png",
    "test/phone/easy4.png",
    "test/phone/med1.png",
    # "test/phone/med2.png",
    "test/phone/med3.png",
    # "test/phone/hard1.png",
    # "test/phone/weird1.png",
]

# paths_white = [
#     "test/white/white1.png",
#     "test/white/white2.png",
#     "test/white/white3.png",
#     "test/white/white4.png",
#     "test/white/white5.png",
#     "test/white/white6.png",
#     "test/white/white7.png",
#     "test/white/white8.png",
# ]

target_images = [
      {
          "name": "target_n",
          "path": PIPELINE_TARGET_N_PATH,
      },
      {
          "name": "target_r",
          "path": PIPELINE_TARGET_R_PATH,
      },
    #   {
    #       "name": "target_heli",
    #       "path": PIPELINE_TARGET_HELI_PATH,
    #   }
    ]

for path in paths:
    time_elapsed("Start", False)
    target_images = prepare_target_images(target_images)
    time_elapsed("Target images ready")
    results = detect_all_targets(path, target_images)
    exit(0)
    # draw_image_objects(path, results)



# OBJECT LOCALIZATION TEST
# path = "test/phone/med3.png"
# results = detect_all(path)
# for r in results:
#     if r["found"]:
#         print("location of", r["path"], "is:", get_img_center(r["corners"], (np.diag([1,1,1]), [1, 2, 3])))
