#This line is a Var called "Formatter"
formattter = "{} {} {} {}"

#I think these prints commands are using the () to fill in the {} via the string .format as an indicator
print(formattter.format(1, 2, 3, 4))
print(formattter.format("one", "two", "three", "four"))
print(formattter.format(True, False, False, True))
print (formattter.format(formattter, formattter, formattter, formattter))
#I think the , is allowing the code to print on the same line
print(formattter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))