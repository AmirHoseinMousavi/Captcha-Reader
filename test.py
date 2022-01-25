from Captcha_Reader import getWords
from shutil import copy
import os

IMAGES = 'Captchas/'

OUTPUT = 'OUTPUT/'

if not os.path.exists(OUTPUT):
	os.mkdir(OUTPUT)

for index, captcha in enumerate(os.listdir(IMAGES)):
	print(index + 1)
	dirName = OUTPUT + str(index) + '_'
	# if not os.path.exists(dirName):
	# 	os.mkdir(dirName)
	copy(IMAGES + captcha, dirName + 'mainCaptcha.gif')
	getWords(IMAGES + captcha, dirName)
