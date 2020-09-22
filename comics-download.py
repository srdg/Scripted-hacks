from bs4 import BeautifulSoup as bs
import requests
from fpdf import FPDF
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-s", help="Comic Name")
parser.add_argument("-o", help="Offset (e.g. ....online-free-0284.jpg will have this argument as 284 (page number in URL for first page of comic)", type=int)
parser.add_argument("-n", help="Number of pages in comic book", type=int)
parser.add_argument("-f", help="Number of digits in a page number (e.g. ....online-free-0284.jpg will have this argument as 4 (digits)", type=int)
args = parser.parse_args()


def downloadPages():
	parent = "https://www.omgbeaupeep.com/comics/mangas/Avatar The Last Airbender/"+args.s+"/read-avatar-the-last-airbender-comics-online-free-"
	page_list = []
	for i in range(1,args.n+1):
		img_data = requests.get(parent+str(i+(args.o-1)).zfill(args.f)+'.jpg').content
		root_dir='Book/'
		Path(root_dir).mkdir(parents=True, exist_ok=True) 
		with open(root_dir+str(i).zfill(3)+'.jpg', 'wb') as handler:
			page_list.append(root_dir+str(i).zfill(3)+'.jpg')
			handler.write(img_data)
		print('Wrote page '+str(i))
	return page_list

def createFile(page_list):
	print("Creating pdf file...",end="")
	pdf = FPDF()
	for page in page_list:
		pdf.add_page()
		pdf.image(page, 0,0,210,297)
	name = args.s[args.s.find("The"):args.s.rfind("(")]
	pdf.output(name+".pdf", "F")
	print("done.")
	
	

def main():
	page_list = downloadPages()
	createFile(page_list)

if __name__=="__main__":
	main()
