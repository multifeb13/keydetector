import argparse
import cv2

def cvReadImage(input):
	return cv2.imread(str(input.name))

def cvCvtToGray(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
	image_out = cvCvtToGray(image)
	cvShowImage(image_out)
	main()
