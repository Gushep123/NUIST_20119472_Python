studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
for name in studentNames:
    print(f"{name} Evans")
new_name = input("\nadd a name to list：")
studentNames.append(new_name)
for name in studentNames:
    print(f"{name} Evans")
