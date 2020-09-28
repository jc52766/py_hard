from sys import argv
script, filename = argv

txt = open(filename)
print(txt.read())

newTxt = input("Input a file name (I'll print its contents):")
txt_newTxt = open(newTxt)
print(txt_newTxt.read())
