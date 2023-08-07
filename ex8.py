formattter = "{} {} {} {}"

print(formattter.format(1, 2, 3, 4))
print(formattter.format("one", "two", "three", "four"))
print(formattter.format(True, False, False, True))
print (formattter.format(formattter, formattter, formattter, formattter))
print(formattter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))