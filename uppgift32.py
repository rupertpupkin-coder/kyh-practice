palindrom = input("Skriv en palindrom:").replace(" ", "")
print(f"Längden på ordet: {len(palindrom)}")


def isPalindrom(s):
    return s == s[::-1]



s = palindrom.lower()
ans = isPalindrom(s)

if ans:
    print("Detta är en palindrom")
else:
    print("Detta är inte en palindrom")