import argparse

def get_arg():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--input', required=True, type=argparse.FileType('rb'))
	return parser.parse_args()

def main():
	return None

if __name__ == '__main__':
	args = get_arg()
	print(args.input)
	main()
