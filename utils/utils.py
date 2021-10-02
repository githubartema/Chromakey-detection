import numpy as np
import cv2  

def get_bounds(regions):
    masks = sorted(regions, key=cv2.contourArea, reverse=True)[:2]
    if max(masks[0][:, :, 0]) > max(masks[1][:, :, 0]):
      target_mask = masks[0]
    else:
      target_mask = masks[1]

    perimeter = cv2.arcLength(target_mask, True)
    bounds = cv2.approxPolyDP(target_mask, 0.1 * perimeter, True)

    return bounds

def get_result_frame(bounds, frame, mask):
  x = cv2.fillConvexPoly(np.zeros((1080, 1920), np.uint8), bounds, color=(255, 255, 255))
  x = cv2.bitwise_not(x)
  x = cv2.bitwise_and(frame, frame, mask = x)
  x = cv2.bitwise_or(x, mask)

  return x

def sort_coordinates(coordinates):
  temp = sorted(coordinates, key=lambda x: x[0][0], reverse=True)
  temp_1, temp_2 = temp[:2], temp[2:]
  temp_1, temp_2 = sorted(temp_1, key=lambda x: x[0][1]), sorted(temp_2, key=lambda x: x[0][1], reverse=True)

  return temp_1 + temp_2