import numpy as np
import cv2  
from utils.utils import *

person = cv2.imread('./person/person.jpeg')

pts1 = [
        [np.shape(person)[0], 0],
        [np.shape(person)[0], np.shape(person)[1]],
        [0., np.shape(person)[1]],
        [0., 0]
]

green = {
    'lower' : np.array([25, 150, 72]),
    'upper' : np.array([102, 255, 255])
}

video = cv2.VideoCapture('./video/green.mp4')

video_info = {  
    'fps':    int(video.get(5)),
    'width':  1920,
    'height': 1080,
    'fourcc': video.get(cv2.CAP_PROP_FOURCC),
    'num_of_frames': int(video.get(7))
}

output = cv2.VideoWriter('./result/vidos.avi',  cv2.VideoWriter_fourcc(*'DIVX'), video_info['fps'], (video_info['width'],video_info['height']))

for i in range(video_info['num_of_frames']):
  _, frame = video.read()

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  blurred_hsv = cv2.GaussianBlur(hsv, (5, 5), 0)

  mask = cv2.inRange(blurred_hsv, green['lower'], green['upper'])
  green_contours = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_NONE)[-2] 

  coordinates = [_.tolist() for _ in sort_coordinates(get_bounds(green_contours))]
  coordinates = np.array(coordinates, dtype='float32')

  H, _ = cv2.findHomography(np.float32(pts1), coordinates, cv2.RANSAC, 5.0)
  mask = cv2.warpPerspective(person, H, (1920, 1080))
  img = get_result_frame(np.int32(coordinates), frame, mask)

  output.write(img)

print('Saving video to ./result folder...')

output.release()