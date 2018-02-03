import threading as T

def add(na,nb):
    s=na+nb
    print(s)
def mult(na,nb):
    m=na*nb
    print(m)

if __name__=='__main__':
    t1=T.Thread(target=add,args=(10,20))
    t2=T.Thread(target=mult,args=(10,20))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('EOD')
