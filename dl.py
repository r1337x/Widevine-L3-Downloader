import os
from typing import DefaultDict

print("\nWEBDL Script")
print("Required files : yt-dlp.exe, mkvmerge.exe, mp4decrypt.exe, aria2c.exe\n")

filename = input("Enter the output file name (no spaces) : ")
mpdurl = input("Enter MPD URL : ")

os.system(f'yt-dlp --allow-unplayable-formats "{mpdurl}"')

os.system("ren *.mp4 video.mp4")
os.system("ren *.m4a audio.m4a")

tKID = input("\nEnter the 3rd decryption key KID")
tKID.strip()
tKEY = input("\nEnter the 3rd decryption key")
tKEY.strip()

os.system(f'mp4decrypt --key {tKID}:{tKEY} video.mp4 video_decrypted.mp4')

fKID = input("\nEnter the 1st decryption key KID")
fKID.strip()
fKEY = input("\nEnter the 1st decryption key")
fKEY.strip()

os.system(f'mp4decrypt --key {fKID}:{fKEY} audio.m4a audio_decrypted.m4a')
os.system(f'mkvmerge -o {filename}.mp4 -A video_decrypted.mp4 audio_decrypted.m4a en.srt')




print("\nPress 2")
delete_choice = int(input("Enter Response : "))

if delete_choice == 1:
    os.remove("encrypted.m4a")
    os.remove("encrypted.mp4")
    os.remove("decrypted.m4a")
    os.remove("decrypted.mp4")
else:
    quit()
