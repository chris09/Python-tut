try:
    fhandle = open('myfile.txt', 'w')
    fhandle.write('This is some data to dump into the file')
    print('Wrote some data to the file')
except IOError as e:
    print('Exception caught: Unable to write to myfile', e)
except Exception as e:
    print('Another error occured', e)
else:
    print('File wirtten to successfully')
    fhandle.close()
