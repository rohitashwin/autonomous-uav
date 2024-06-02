import cv2
import time_utils
import time
import autopilot as ap
# from os.path import join
import os
import json
import file_utils

class SensorReader():
    def __init__(self, save_dir):
        self.save_dir = save_dir
        self.init_sensors() 

    def init_sensors(self):
        self.camera_resolution = (1920, 1080)
        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        camera.set(cv2.CAP_PROP_FPS, 30)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.camera_resolution[0])
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.camera_resolution[1])
        self.camera = camera
        self.latest_image = None

        self.apm = ap.Autopilot(ap.SERIAL_PORT, ap.DEFAULT_BAUD_RATE)
        self.latest_sensors = None

    def read_sensors(self):
        timestamp = time_utils.get_timestamp(millis=True)
        ret, image = self.camera.read() 
        if not ret:
            image = None
        ap_data = self.apm.get_data() 

        image_path = os.path.join(self.save_dir, f"{timestamp}_cam.jpg")
        self.latest_image = image
        cv2.imwrite(image_path, image)

        sensor_data_path = os.path.join(self.save_dir, f"{timestamp}_sensors.json")
        sensor_data = {
            "image_path": image_path,
            "gps": ap_data["gps"],
            "imu": ap_data["imu"],
            "attitude": ap_data["attitude"]
        }
        self.latest_sensors = sensor_data
        with open(sensor_data_path, "w") as f:
            json.dump(sensor_data, f, indent=4)

        sensor_data["image"] = image
        return sensor_data

    def get_latest(self):
        return self.latest_sensors, self.latest_image

    def read_fixed(self, n, interval):
        for i in range(n):
            self.read_sensors()
            
def test_image_load():
    start = time.time()
    path = "temp/240531_011844_493_cam.jpg"
    img = cv2.imread(path)
    end = time.time()
    print(end-start)
    print(img.shape)

if __name__ == "__main__":
    save_dir = file_utils.new_save_dir()
    reader = SensorReader(save_dir)

    # n = 60
    # interval = .05

    # n = 30
    # interval = .1

    n = 15 
    interval = .2

    # n = 6 
    # interval = .5

    # n = 3
    # interval = 1

    reader.read_fixed(n, interval)

# if __name__ == "__main__":
#     test_image_load()