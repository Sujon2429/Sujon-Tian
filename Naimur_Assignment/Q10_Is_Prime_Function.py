def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

start = int(input("starting value: "))
end = int(input("ending value: "))

for i in range(start, end+1):
    if is_prime(i) == True:
        print(i)
