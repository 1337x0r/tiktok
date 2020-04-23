import re
import pyfiglet
from src import *
import os

def main():
    print(pyfiglet.figlet_format("Tiktok Download", font='slant'), end = '')
    print ("Script Created By: Will Pratama", end = '')
    print ("\nThanks To: Pamungkas\n")
    links = str(input("Input Link TikTok: "))
    if "TikTok" in links:
        deleteSpace = re.sub(r"\s+", "", links, flags=re.UNICODE)
        links = re.findall(r"TikTok\>(.*)", str(deleteSpace))[0]
    else:
        links = links

    s = TikTok()
    parse = s.parseTikTok(links)
    if "true" in parse[0]:
        aweme_id = parse[1]
        userId = parse[2]
        username = parse[3]

        get = s.getUrlVidio(userId, aweme_id)
        if "true" in get[0]:
            urlVidio = get[1]
            namaFile = "@" + username + " - " + aweme_id + ".mp4"
            s.download_vidio(urlVidio, namaFile)
        else:
            pass    
    else:
        print (parse[1])

        
if __name__ == "__main__":
    main()  