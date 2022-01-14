import requests

def IPAndLoc():
    locationAPI = "https://api.iplocation.net/?ip="
    IPurl = "https://whatismyipaddress.com/"
    IPRes = requests.get(IPurl)
    IP = str(IPRes.content)
    IP = IP[IP.find("Your IP address: ") + 17:IP.find("</li>",IP.find("Your IP address: "))]
    LocRes = str(requests.get(locationAPI + IP).content)
    start = LocRes.find("{}country_name{}:{}".format(chr(34),chr(34),chr(34))) + 16
    end = int(LocRes.find(",",start))
    COUNTRY = LocRes[start:end - 1]
    iploc = IP + " , " + COUNTRY
    return iploc
print(IPAndLoc())
