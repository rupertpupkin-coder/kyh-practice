def print_user(user):
    (name, age) = user   # Packar upp tuppeln
    print(f"Namn: {name}")
    print(f"Ålder: {age}")


print_user(("Jacob", 16))



def switchT(t):
    (a, b) = t
    (a, b) = (b, a)
    t = (a, b)
    return t


t = (5, 6)
(c, d) = switchT(t)
print(switchT(t))


def make_list(ls):
    return tuple(ls)

a = make_list([1, 2, 3])
print(make_list(a))

