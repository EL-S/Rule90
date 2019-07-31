import time
while True:
    s = [0,1,0]
    start = time.time()
    for i in range(10000):
        s.insert(0,0)
        s.extend((0,))
        s=list(map(lambda p,n: p^n,[0]+s,s[1:]+[0]))
    print(time.time() - start)
