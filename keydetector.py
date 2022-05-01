import argparse
import numpy as np
import cv2

def cvReadImage(input):
	return cv2.imread(str(input.name))

def cvCvtToGray(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def cvToEdgeImage(image_gray):
	return cv2.Canny(image_gray, 150, 300, L2gradient=True)

def cvHoughLines(image_edge):
	lines = cv2.HoughLines(image_edge, 1, np.pi / 180, 100)
	if lines is None:
		print("None")
	else:
		print(len(lines))
	return lines

def cvShowImage(image):
	cv2.imshow('image', image)
	cv2.waitKey(0)

def get_arg():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--input', required=True, type=argparse.FileType('rb'))
	parser.add_argument('-v', '--view', action='store_true')
	return parser.parse_args()

def main():
	return None

if __name__ == '__main__':
	args = get_arg()
	image = cvReadImage(args.input)
	image_gray = cvCvtToGray(image)
	image_out = cvToEdgeImage(image_gray)
	houghLines = cvHoughLines(image_out)
	if args.view:
		cvShowImage(image_out)
	main()
