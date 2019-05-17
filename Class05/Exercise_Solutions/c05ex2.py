import random 

e2f = {1:"un", 
    2:"deux",
    3:"trois",
    4:"quatre",
    5:"cinq",
    6:"six",
    7:"sept",
    8:"huit",
    9:"neuf"}

print("Welcome to the french numbers game.")

while True:
    num = random.randint(1,9)
    ans = input("What is the french word for " + str(num) + " (print exit to exit): ")
    if ans == e2f[num]:
        print("Congratulations")
    elif ans.lower() == "exit":
        break
    else:
        print("Sorry, the french word for", num, "is", e2f[num])
print("Thank you for playing!")