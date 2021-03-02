f = open("tutorial.token", "r")
content = f.read()
content_list = content.split(" ")
newlist = []

for x in content_list:
  if x.count>=5 & x.islower():
    newlist.append(x)

print(newlist)
f.close()