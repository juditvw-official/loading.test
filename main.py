import time

def loading (speed):
  for i in range(20):
    print("-", flush=True, end="")
    time.sleep(speed)
  print()

def loading_1 (speed):
  for a in range(100):
    print("-", flush=True, end="")
    time.sleep(speed)
  print()

print("Loading 1")
loading(0.5)
print("sucseful")

print("Loading 2")
loading_1(0.1)
print("sucseful")

print("Loading 3")
loading(1)
print("sucseful")
