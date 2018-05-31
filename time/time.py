import time
def displayTime():
    epoch=time.time()
    print('The epoch is {}'.format(epoch))
    cur=time.ctime(epoch)
    print('The time is {}'.format(cur))
    print('The days since epoch is {}'.format(epoch//(24*60*60)))
if __name__=='__main__':
    displayTime()
