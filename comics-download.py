from bs4 import BeautifulSoup as bs
import requests
from fpdf import FPDF


def downloadPages():
	parent = "https://www.omgbeaupeep.com/comics/mangas/Avatar The Last Airbender/011 - Avatar The Last Airbender - Smoke and Shadow Part 2 (2015)/read-avatar-the-last-airbender-comics-online-free-"
	page_list = []
	for i in range(1,81):
		img_data = requests.get(parent+str(i).zfill(3)+'.jpg').content
		root_dir='Book 7/'
		
		with open(root_dir+str(i).zfill(3)+'.jpg', 'wb') as handler:
			page_list.append(root_dir+str(i).zfill(3)+'.jpg')
			handler.write(img_data)
		print('Wrote page '+str(i))
	return page_list

def createFile(page_list):
	print("Creating pdf file...")
	pdf = FPDF()
	for page in page_list:
		pdf.add_page()
		pdf.image(page, 0,0,210,297)
	pdf.output("Book 14 - Smoke and Shadow-II.pdf", "F")
	
	

def main():
	page_list = downloadPages()
	createFile(page_list)
	
if __name__=="__main__":
	main()
