ans = 0
for i in range(3):
    line = input()
    if line == "Fizz" or line == "Buzz" or line == "FizzBuzz":
        continue
    ans = int(line) + 3 - i
if ans % 3 == 0 and ans % 5 == 0:
    print("FizzBuzz")
elif ans % 3 == 0:
    print("Fizz")
elif ans % 5 == 0:
    print("Buzz")
else:
    print(ans)
