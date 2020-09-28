# hej = ','.join(["ab", "cd"])
#       # ',' = self, ab cd = string
#
#
# print(hej)

#exempel:

# POCO "Plain old class object"
class School:
    def __init__(self, name):
        self.name = name

    def get_name(self, trimmed):
        if trimmed:
            return self.name.strip()
        return self.name

skola = School("KYH")

#print(skola.name)
#print(type(skola))
print(skola.get_name(False))