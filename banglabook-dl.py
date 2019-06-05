from selenium import webdriver
import os
import sys
import time
import pathlib
from multiprocessing import Pool
from selenium.webdriver.chrome.options import Options
from PIL import Image,ImageOps
import argparse
from tqdm import tqdm
pathlib.Path('data').mkdir(parents=True, exist_ok=True) 
options = Options()
options.headless=True
driver = webdriver.Chrome('./chromedriver',chrome_options=options)
driver.set_window_size(1366, 728)
for i in tqdm(range(373)):
	driver.get("https://view.publitas.com/bdfuel/tbl-2019-banglabook-org/page/"+str(i))
	time.sleep(2)
	driver.save_screenshot('data/'+str(i)+'.png')
	img=Image.open('data/'+str(i)+'.png')
	img=ImageOps.crop(img,(490,20,450,30))
	img.save('data/'+str(i)+'.png')
