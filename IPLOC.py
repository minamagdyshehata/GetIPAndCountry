import requests

def IPAndLoc():
    locationAPI = "https://api.iplocation.net/?ip="
    IPurl = "https://api.ipify.org/"
    IPRes = requests.get(IPurl)
    IP = str(IPRes.content)
    IP = IP[IP.find("b'") + 2:-1]
    LocRes = str(requests.get(locationAPI + IP).content)
    start = LocRes.find("{}country_name{}:{}".format(chr(34),chr(34),chr(34))) + 16
    end = int(LocRes.find(",",start))
    COUNTRY = LocRes[start:end - 1]
    iploc = IP + " , " + COUNTRY
    return iploc
print(IPAndLoc())

