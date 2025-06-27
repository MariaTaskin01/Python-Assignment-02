# 1. Start with a variable `x = 0` and apply `+=`, `-=`, `*=`, `/=`, `%=`, step by step.

print("1. Start with a variable `x = 0` and apply `+=`, `-=`, `*=`, `/=`, `%=`, step by step.")

x = 0
print("Initial value of x:", x)

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x /= 4
print("x /= 4:", x)

x %= 3
print("x %= 3:", x)

# 2. Create a counter that increases by 2 on each step, using `+=`.

print("2. Create a counter that increases by 2 on each step, using `+=`.")

y = 0

while y <= 20 :
    print("Counter",y)
    y += 2

# 3. Create a simple savings balance calculator: add interest using `*=`.

print("3. Create a simple savings balance calculator: add interest using `*=`.")

saving = 1000
interest = 0.75

print("Saving", saving)
print("Interest", interest)

print("Saving * Interest = ", saving * interest )

# 4. Simulate a countdown where each step decreases by  using `-=`.

print("4. Simulate a countdown where each step decreases by  using `-=`.")

a = 10

while a >= 1 :
    print("Countdown",a)
    a -= 1