str_x = "Emma is good developer, Emma is a writer"
count = 0
for index in range(len(str_x)):
    if str_x[index:index+4] == "Emma":
        count += 1
print("Emma appeared", count, "times")