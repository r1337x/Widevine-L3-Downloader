import os
import time
import shutil

print("\nWEBDL Script")
print("Required files : yt-dlp.exe, mkvmerge.exe, mp4decrypt.exe\n")

count = 0

mpdurl = input("Enter MPD URL : ")

os.system(f'yt-dlp --allow-unplayable-formats "{mpdurl}" -P "~/ytdown" -o "video.%(ext)s"')

while not (os.path.exists("~/ytdown/video.mp4") and os.path.exists("~/ytdown/video.m4a")):
  time.sleep(1)
  count += 1
  if count>=120:
     print("Script exiting cuz file doesn't exist")
     quit()

print("\nPress 2")
delete_choice = int(input("Enter your Delete Choice : "))


vkey = input("Enter Video Key : ")
vkid = input("Enter Video KID : ")

count = 0

os.system(f'mp4decrypt --key {vkid}:{vkey} "~/ytdown/video.mp4" "~/ytdown/video_decrypted.mp4"')

while not os.path.exists("~/ytdown/video_decrypted.mp4"):
  time.sleep(1)
  count += 1
  if count>=120:
     print("Script exiting cuz file doesn't exist")
     quit()

akey = input("Enter Audio Key : ")
akid = input("Enter Audio KID : ")

count = 0

os.sytem(f'mp4decrypt --key {akid}:{akey} "~/ytdown/video.m4a" "~/ytdown/audio_decrypted.m4a"')

while not os.path.exists("~/ytdown/audio_decrypted.m4a"):
  time.sleep(1)
  count += 1
  if count>=120:
     print("Script exiting cuz file doesn't exist")
     quit()

os.system("mkvmerge -o Final.mp4 -A '~/ytdown/video_decrypted.mp4' '~/ytdown/audio_decrypted.m4a'")

if delete_choice == 1:
  shutil.rmtree("~/ytdown")
else:
  quit()