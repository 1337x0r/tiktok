# Script Created By: Will Pratama - https://www.facebook.com/yaelahhwil
# Thanks To: Pamungkas - https://www.facebook.com/yudha.t.pamungkas.3

import re
import requests
import sys
from .config import Config

class TikTok:
    def __init__(self):
        self.con = Config()
        self.host = self.con.TIKTOK_HOST_DOMAIN
        self.end = self.con.TIKTOK_END
        self.headers = self.con.TIKTOK_HEADERS

    def getdata_vidio(self, links):
        VERSION = sys.version_info[0]
        UA_CHROME = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
        r1 = None
        class Junk:
            def __init__(self):
                self.data = None

        if VERSION==2:
            import urllib2
            req = urllib2.Request(links, headers={ 'User-Agent': UA_CHROME })
            # faked to return a similar setup as Python3
            r1 = Junk()
            r1.data = urllib2.urlopen(req).read()
            return r1
        else:
            import urllib3
            http = urllib3.PoolManager(10, headers={ 'User-Agent': UA_CHROME })
            r1 = http.urlopen('GET', links)
            return r1

    def parseTikTok(self, url):  
        abc = requests.get(url = url, allow_redirects=False, headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36" })
        if "301" in str(abc.status_code):
            send = requests.get(url = str(abc.headers["Location"]), allow_redirects=False, headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36" })
            if "302" in str(send.status_code):
                try:
                    send = requests.get(url = str(send.headers["Location"]), allow_redirects=False, headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36" })
                    aweme_id = re.findall(r"\/\/aweme\/detail\/(.*?)\?", str(send.content))[1]
                    userId = re.findall(r"\"userId\":\"(.*?)\"", str(send.content))[0]
                    username = re.findall(r"\"alternateName\":\"(.*?)\"", str(send.content))[0]
                    if len(aweme_id) > 1 or len(userId) > 1 or len(username) > 1:
                        print("\nfound good video link...", end ='')
                        return ["true", aweme_id, userId, username]
                    else:
                        print("\ndid not find a video link :(", end ='')
                        return ["false", ""]
                except:
                    print("\ndid not find a video link :(", end ='')
                    return ["false", ""]        
            else:
                aweme_id = re.findall(r"\/\/aweme\/detail\/(.*?)\?", str(send.content))[1]
                userId = re.findall(r"\"userId\":\"(.*?)\"", str(send.content))[0]
                username = re.findall(r"\"alternateName\":\"(.*?)\"", str(send.content))[0]
                if len(aweme_id) > 1 or len(userId) > 1 or len(username) > 1:
                    print("\nfound good video link...", end ='')
                    return ["true", aweme_id, userId, username]
                else:
                    print("\ndid not find a video link :(", end ='')
                    return ["false", ""]    
        if "302" in str(abc.status_code):
            try:
                send = requests.get(url = str(abc.headers["Location"]), headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36" }).content
                aweme_id = re.findall(r"\/\/aweme\/detail\/(.*?)\?", str(send))[1]
                userId = re.findall(r"\"userId\":\"(.*?)\"", str(send))[0]
                username = re.findall(r"\"alternateName\":\"(.*?)\"", str(send))[0]
                if len(aweme_id) > 1 or len(userId) > 1 or len(username) > 1:
                    print("\nfound good video link...", end ='')
                    return ["true", aweme_id, userId, username]
                else:
                    print("\ndid not find a video link :(", end ='')
                    return ["false", ""]
            except:
                print("\ndid not find a video link :(", end ='')
                return ["false", ""]        
        else:
            try:
                aweme_id = re.findall(r"\/\/aweme\/detail\/(.*?)\?", str(abc.content))[1]
                userId = re.findall(r"\"userId\":\"(.*?)\"", str(abc.content))[0]
                username = re.findall(r"\"alternateName\":\"(.*?)\"", str(abc.content))[0]
                if len(aweme_id) > 1 or len(userId) > 1 or len(username) > 1:
                    print("\nfound good video link...", end ='')
                    return ["true", aweme_id, userId, username]
                else:
                    print("\ndid not find a video link :(", end ='')
                    return ["false", ""]
            except:
                print("\ndid not find a video link :(", end ='')
                return ["false", ""]        

    def download_vidio(self, url, namaFile):
        datavidio = self.getdata_vidio(url)
        outf = open("Output-Tiktok/"+namaFile,"wb")
        outf.write(datavidio.data)
        outf.close()
        print("\nvidio success saved " + namaFile, end = '')

    def getUserId(self, keywords):
        get = requests.get(url = self.host+'/aweme/v1/discover/search/?cursor=0&keyword='+str(keywords).strip()+self.end, headers = self.headers).json()    
        userid = get["user_list"][0]["user_info"]["uid"]
        return userid

    def getUrlVidio(self, userId, awemeid):
        print ("\nscanning data vidio, please wait..", end ='')
        get = requests.get(url = self.host+'/aweme/v1/aweme/post/?max_cursor=0&user_id='+str(userId)+self.end, headers = self.headers).json()
        max_cursor = get["max_cursor"]
       
        for a in range(20):
            try:
                aweme_id = get["aweme_list"][int(a)]["aweme_id"]
                if str(awemeid) in str(aweme_id):
                    print ("\nfound this data vidio..!", end = '')
                    urlVidio = get["aweme_list"][int(a)]["video"]["bit_rate"][0]["play_addr"]["url_list"][0]
                    return ["true", urlVidio]
                else:
                    pass    
            except:
                continue
                
        for x in range(50):
            get_again = requests.get(url = self.host+'/aweme/v1/aweme/post/?max_cursor='+str(max_cursor)+'&user_id='+str(userId)+self.end, headers = self.headers)
            if "No more videos" in str(get_again.content):
                return ["false", "not found this data..:("]
            else:
                max_cursor = get_again.json()["max_cursor"]
                for a in range(20):
                    try:
                        aweme_id = get_again.json()["aweme_list"][int(a)]["aweme_id"]
                        if str(awemeid) in str(aweme_id):
                            print ("\nfound this data vidio..!", end = '')
                            vidio = get_again.json()["aweme_list"][int(a)]["video"]["bit_rate"][0]["play_addr"]["url_list"][0]
                            return ["true", vidio]
                        else:    
                            pass
                    except:
                        pass           