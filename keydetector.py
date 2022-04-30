import argparse
import cv2

def cvReadImage(input):
	return cv2.imread(str(input.name))

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
	return parser.parse_args()

def main():
	return None

if __name__ == '__main__':
	args = get_arg()
	image = cvReadImage(args.input)
	image_gray = cvCvtToGray(image)
	image_out = cvToEdgeImage(image_gray)
	cvShowImage(image_out)
	main()
