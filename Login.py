Username = ["Cassiem", "Gary", "Zaid", "Aaliyah", "Uthmaan"]
Password = ["666", "777", "999", "888", "333"]
Name = (input("Enter username: "))
Code = (input("Enter Password: "))
result = False

for x in range(len(Username)):
    if Name == Username[x] and Code == Password[x]:
        result = True
if result == True:
    print("Access granted")
else:
    print("Access denied")
