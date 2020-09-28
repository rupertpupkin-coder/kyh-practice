palindrom = input("Skriv en palindrom:").replace(" ", "")
print(f"Längden på ordet: {len(palindrom)} tecken")


def isPalindrom(s):
    return s == s[::-1]


# s = ''.join([c for c in palindrom.lower() if c != ' '])                       List-comprehension
s = palindrom.lower()
ans = isPalindrom(s)

if ans:
    print(f"{s} är ett palindrom")
else:
    print("Detta är inte ett palindrom")

isPalindrom(s)
