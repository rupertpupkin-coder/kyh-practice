name = input("Vad heter du i förnamn? ")
efternamn = input("Vad heter du i efternamn? ")
age = int(input("Hur gammal är du? "))

a = "Hejsan %s du heter %s i efternamn. Du är %d år gammal" % (name, efternamn, age)
#print(a)


o = "Hejsan {} ditt namn är {}. Du är {} år gammal".format(name, efternamn, age)
print(o)