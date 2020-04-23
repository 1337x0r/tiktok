# Script Created By: Will Pratama - https://www.facebook.com/yaelahhwil
# Thanks To: Pamungkas - https://www.facebook.com/yudha.t.pamungkas.3

class Config():
    TIKTOK_HEADERS = { 
        'Host': 'api21-h2.tiktokv.com', 
        'User-Agent': 'okhttp/1323.111.32.3232', 
        'Cookie': 'odin_tt=04c751dda5a2396d73220905817a72b888cbf3b7734718d14dcd998ac781db657889f603cea1dfe593dcd5378c26b9e24eb1cca2b6720835ef3c2926a983116e; d_ticket=ed8e7e66043805b099a1390215efa23e1f576; sid_guard=d3da0690959f0a1b524a818fa74ec99c%7C1587014271%7C5184000%7CMon%2C+15-Jun-2020+05%3A17%3A51+GMT; uid_tt=0db1561b9e7059e6c0a93731385d11071ef97c70e30e011d46fe0e521dcce5aa; sid_tt=d3da0690959f0a1b524a818fa74ec99c; sessionid=d3da0690959f0a1b524a818fa74ec99c; store-idc=alisg; store-country-code=id; install_id=6816169706295576321; ttreq=1$c6963e7f549cb855044458bcaecb2af3be50df0e'
    }

    TIKTOK_HOST_DOMAIN = 'https://api21-h2.tiktokv.com'
    TIKTOK_END = '&count=100&retry_type=no_retry&app_language=en&language=en&region=US&sys_region=US&carrier_region=ID&&iid=0&device_id=0&channel=googleplay&aid=1180&app_name=trill&version_code=155&version_name=1.5.5&device_platform=android&device_type=G011A&os_version=5.1.1'

    def __init__(self):
        self.host = self.TIKTOK_HOST_DOMAIN
        self.end = self.TIKTOK_END
        self.headers = self.TIKTOK_HEADERS