import matplotlib.pyplot as plt
# import urllib2
import time
import urllib.request


stocksToPull = ['AAPL', 'GOOG', 'MSFT', 'CMG', 'EBAY', 'AMZN', 'TSLA']

def pullData(stock):
    try:
        fileLine = stock + '.txt'
        uriToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1y/csv'
        # sourceCode = urllib2.urlopen(uriToVisit).read()
        sourceCode = urllib.request.urlopen(uriToVisit).read()
        sourceCode = sourceCode.decode('utf-8')
        splitSource = sourceCode.split('\n')
        for eachLine in splitSource:
            splitLine = eachLine.split(',')

            if len(splitLine) == 6:
                if 'values' not in eachLine:
                    saveFile = open(fileLine, 'a')
                    lineToWrite = eachLine + '\n'
                    saveFile.write(lineToWrite)

        print('pulled', stock)
        print('sleeping')
        time.sleep(5)

    except Exception as e:
        print('main loop', e)

for eachStock in stocksToPull:
    pullData(eachStock)

# plt.plot([1,2,3],[5,7,4])
# plt.show()
