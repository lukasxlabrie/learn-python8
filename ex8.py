#This line is a Var called "Formatter"
formattter = "{} {} {} {}"

#I think these prints commands are using the () to fill in the {} via the string .format as an indicator
print(formattter.format(1, 2, 3, 4))
print(formattter.format("one", "two", "three", "four"))
print(formattter.format(True, False, False, True))
# This prints 16 {} because the formatter is requested 4 times
print (formattter.format(formattter, formattter, formattter, formattter))
#I think the , is allowing the code to print on the same line
print(formattter.format(
    "It is quite difficult to",
    "work on this while",
    "an intense conversation ia happening behind me ",
    "and Lucy is watching is Toy Story"
))