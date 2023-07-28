import time

print(f"=> Countdown to the fireworks!")
for c in range(10, 0, -1):
    print(f"{c}")
    time.sleep(1)

print(f"=> BOOM!")