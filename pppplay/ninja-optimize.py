import string

cs = set()
for c in string.ascii_letters + string.digits + r"+,-./\_$":
    cs.add(ord(c))
for i in range(256):
    print('%d,' % (i in cs))
