import requests as rq
# import urllib2 as urli
# from xml.etree import ElementTree as ET
import untangle as unt
from pprint import pprint

req = rq.get("https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=5000")

res = req.text #string

doc = unt.parse(res)
child_element = doc.ann

# the1stTag = 'ann'
# the2ndTag = 'anime id="5000" gid="2056435461" type="movie" name="Sora no Momotaro" precision="movie" generated-on="2020-03-14T09:28:45Z"'
# the3rdTag = 'staff'
# the4thTag = 'task'

print(child_element)

# print(child_element)


