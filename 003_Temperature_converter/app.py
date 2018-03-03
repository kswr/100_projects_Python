def tempConverter(degrees, celcToFahr = True):
    if celcToFahr:
        return degrees*9/5 + 32
    else:
        return (degrees - 32) * 5/9


print(tempConverter(100))
print(tempConverter(212, False))
