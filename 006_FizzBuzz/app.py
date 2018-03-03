def fizzBuzz(countTo = 100):
    """This function prints fizz buzz for 100 elements by default"""
    fb = ''
    for i in range(1, countTo + 1):
        if (i % 3 == 0) & (i % 5 == 0):
            fb += 'Fizz Buzz, '
        elif i % 3 == 0:
            fb += 'Fizz, '
        elif i % 5 == 0:
            fb += 'Buzz, '
        else:
            fb += str(i) + ', '
    return fb

print(fizzBuzz())

print(fizzBuzz(50))
