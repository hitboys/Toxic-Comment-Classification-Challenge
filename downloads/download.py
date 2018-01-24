import os
import argparse

parser = argparse.ArgumentParser(description="** download datasets **")
parser.add_argument('-glove', type=str, default=None, help="download glove pre-train vectors, parameter: [840b, ]")
args = parser.parse_args()

def download_glove(name):
	if name == "840b":
		filename = "glove.840B.300d.zip"
	elif name == "42b":
		filename = "glove.42B.300d.zip"
	elif name == "6b":
		filename = "glove.6B.zip"
	elif name == "twitter":
		filename = "glove.twitter.27B.zip"
	else:
		return
	
	os.system("wget http://nlp.stanford.edu/data/%s" % filename)
	os.system("unzip %s" % filename)
	os.system("rm %s" % filename)

if __name__ == '__main__':
	if args.glove is not None:
		download_glove(args.glove)
