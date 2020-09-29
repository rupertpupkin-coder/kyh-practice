# 40.1
def reverse(a):
    text = []
    for c in a:
        text.append(c)
    length = len(text)
    s = length
    new_list = [None] * length
    for i in text:
        s = s - 1
        new_list[s] = i
    return new_list


o = "".join(reverse("123456"))
print(o)


# 40.2

def text(text):
    count = 0
    for l in text:
        if l == l.upper():
            count += 1
    return count


#name = input("Skriv något:")
#a = text(name)
#print(a)


# 40.3

def minmax(value, min, max):
    if min < value < max:
        return True
    else:
        return False


a = minmax(44, 10, 56)
print(a)
