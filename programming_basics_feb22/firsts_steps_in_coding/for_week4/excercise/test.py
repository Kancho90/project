text = "Честита Баба Марта на всички !"
text_new = ""
n = len(text)
for i in range(0,n):
  text_new += text[i]
  if i == 6:
    break
  print(text_new)
print(text)
