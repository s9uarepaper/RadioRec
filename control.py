import subprocess
import sys
import os.path
import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

d = datetime.date.today()
filename = "ani" + d.strftime("%Y%m%d")+".mp3"
main_dir = "~/RadioRec/"
data3_dir = "./data/audio/"
filepath = data3_dir + filename
subprocess.call("python "+main_dir+"aandg.py -n ani -l 1 -o 4", shell=True)


#google driveアップロード部分（テスト実装）
if os.path.isfile(filepath):
	gauth = GoogleAuth()
	gauth.CommandLineAuth()
	drive = GoogleDrive(gauth)

	f = drive.CreateFile({'title': filename, 'mimeType': 'audio/mpeg'})
	f.SetContentFile(filepath)
	f.Upload()
else :
	print('file upload error.')
