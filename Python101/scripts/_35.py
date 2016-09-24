import os
import time

curDir = os.getcwd()
print(curDir)

if os.path.isdir(os.path.join(os.getcwd(), 'newDir')):
    print('newDir is exists')
    time.sleep(2)
    os.rmdir('newDir')
else:
    os.mkdir('newDir')
    time.sleep(2)
    if os.path.isdir(os.path.join(os.getcwd(), 'newDir2')):
        print('newDir2 is exists')
        os.rmdir('newDir2')
    else:
        os.rename('newDir', 'newDir2')
        time.sleep(2)
        os.rmdir('newDir2')
