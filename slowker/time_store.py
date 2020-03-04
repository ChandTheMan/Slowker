import time

tick = time.perf_counter()
print(tick)
tock = time.perf_counter()
print(tock-tick)
