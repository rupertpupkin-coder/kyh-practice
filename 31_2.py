indata = input("Ange tal med komma emellan:")
ls = indata.split(",")


ls2 = []
for elem in ls:
    ls2.append(int(elem))
# ls2 = [int(elem) for elem in ls.split(",")]

backwards = ', '.join(list(reversed(ls)))
# backwards = ', '.join(ls[::-1]) alternativ väg att köra baklänges

print(f"Första talet: {ls[0]}")
print(f"Sista talet: {ls[-1]}")
print(f"Summan av av talen är: {sum(ls2)}")
print(f"Baklänges: {backwards}")



#ls2 = [int(elem) for elem in ls.split(",")]

