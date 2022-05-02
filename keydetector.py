import argparse
import numpy as np
import cv2

ORIENTATION_HORIZONTAL=1
ORIENTATION_VERTICAL=2

def cvReadImage(input):
	return cv2.imread(str(input.name))

def cvWriteImage(filename, input):
	cv2.imwrite(filename, input)

def cvCvtToGray(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def cvToEdgeImage(image_gray):
	return cv2.Canny(image_gray, 150, 300, L2gradient=True)

def cvShowImage(image):
	cv2.imshow('image', image)
	cv2.waitKey(0)

def get_arg():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--input', required=True, type=argparse.FileType('rb'))
	parser.add_argument('-v', '--view', action='store_true')
	return parser.parse_args()

def detectOrientation(image):
	height, width = image.shape[:3]

	# count horizontal stream
	h_cnt = 0
	for y in range(height - 1):
		for x in range(width - 1):
			if image[y,x+0] and image[y,x+1]:
				h_cnt+=1

	# count vertical stream
	v_cnt = 0
	for x in range(width - 1):
		for y in range(height - 1):
			if image[y+0,x] and image[y+1,x]:
				v_cnt+=1

	if h_cnt > v_cnt:
		return ORIENTATION_HORIZONTAL
	else:
		return ORIENTATION_VERTICAL

def main():
	return None

if __name__ == '__main__':
	args = get_arg()
	image = cvReadImage(args.input)
	image_gray = cvCvtToGray(image)
	image_out = cvToEdgeImage(image_gray)
	ori = detectOrientation(image_out)
	if ori == ORIENTATION_HORIZONTAL:
		print("Horizontal")
	else:
		print("Vertical")

	if args.view:
		cvShowImage(image_out)
	main()
