import subprocess
import sys
import argparse as ap
import datetime

args = sys.argv

parser = ap.ArgumentParser(description = "A&G Recorder")
parser.add_argument('-n', '--name', required = True, type = str, help = "Title")
parser.add_argument('-l', '--length', required = True ,type = int, help = "record length(min)")
parser.add_argument('-o', '--out', type = int, default = 1, help = "Save Format(1:flv /3:mp3 / 4:mp4)")
psargs = parser.parse_args()

title = psargs.name
address = "rtmp://fms-base1.mitene.ad.jp/agqr/aandg22"
d = datetime.date.today()
main_dir = "~/RadioRec/"
data3_dir = "~/RadioRec/data/audio/"
data4_dir = "~/RadioRec/data/video/"

rec_title = title + d.strftime("%Y%m%d")
rec_len = psargs.length *60
rec_mode = psargs.out
rec_cmd = "rtmpdump -vr " + address + " --live --stop " + str(rec_mode) + " -o " + data4_dir + rec_title + ".flv"

subprocess.call(rec_cmd, shell=True)

conv3_cmd = "avconv -i "+ data4_dir + rec_title +".flv" + " -c:a libmp3lame -b:a 192k " + data3_dir + rec_title + ".mp3"
conv4_cmd = "avconv -i " + data4_dir + rec_title+".flv" + " -codec copy " + data4_dir+rec_title+".mp4"

if(rec_mode == 3):
    subprocess.call(conv3_cmd,shell = True)

elif(rec_mode ==4):
    subprocess.call(conv4_cmd, shell = True)
    subprocess.call(conv3_cmd, shell = True)


subprocess.call("rm " + data4_dir + rec_title+".flv", shell =True)
