import http.client


h = http.client.HTTPConnection('www.infiniteskills.com')
h.request('GET', '/')
data = h.getresponse()
print(data.code)
print(data.headers)
text = data.readlines()
for t in text:
    print(t.decode('utf-8'))