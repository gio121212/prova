import time
l=list(range(10000000))
v=list(range(1000000))
T1=time.perf_counter()
s=l+v
T2=time.perf_counter()
print(' + execution time: ' , T2-T1, 's')
T3=time.perf_counter()
l.extend(v)
T4=time.perf_counter()
print('extend execution time:', T4-T3 , 's')