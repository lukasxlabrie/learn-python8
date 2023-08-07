#This line is a Var called "Formatter"
formattter = "{} {} {} {} {}" #{} must = # of print requests in .format

#I think these prints commands are using the () to fill in the {} via the string .format as an indicator
print(formattter.format(1, 2, 3, 4, 5))
print(formattter.format("one", "two", "three", "four", "five"))
print(formattter.format(True, False, False, True, True))
print(formattter.format("Green", "Yellow", "Blue","Orange", "Black"))
# This prints 16 {} because the formatter is requested 4 times
print (formattter.format(formattter, formattter, formattter, formattter, formattter))
#I think the , is allowing the code to print on the same line
print(formattter.format(
    "It is quite difficult to",
    "work on this while",
    "an intense conversation is happening behind me",
    "and Lucy is watching is Toy Story",
    "but i am still making progress!"
))

#the majority of ways to break this code can be redcued to syntax. Outisde of this the other possibilities are defined in my notes