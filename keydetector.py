import argparse
import cv2

def cvReadImage(input):
	return cv2.imread(str(input.name))

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
	cvShowImage(image)
	main()
