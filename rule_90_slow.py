import time
s = "010"

start = time.time()
for i in range(10000):
    s = "0" + "".join(list(map(lambda p,n:str(int(p)^int(n)), "0" + s, s[1:] + "0"))) + "0"
print(time.time() - start)
