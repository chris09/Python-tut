import urllib.request
import urllib.parse
import re


url = 'http://pythonprogramming.net'
values = {
    's': 'basics',
    'submit': 'search'
}

data = urllib.parse.urlencode(values)
print(data)
data = data.encode('utf-8')
print(data)
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# print(respData)

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for p in paragraphs:
    print(p)
