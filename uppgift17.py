from pathlib import Path

p = Path("TODO.txt")


homepage = """
1. Lista TODO
2. Lägg till uppgift
3. Ta bort uppgift
4. Avbryt programmet"""

print(homepage)

todo_list = []


def user_input():
    user_answer = input("Vad vill du göra? ")
    while True:
        if user_answer == "1":
            print(p.read_text())

        elif user_answer == "2":
            print(p.read_text())
            user_input2 = input("Vad vill du lägga till? ")
            todo_list.append(user_input2)
            p.write_text(user_input2)

        elif user_answer == "3":
            print(p.read_text())
            user_input3 = input("Vad vill du ta bort? ")
        elif user_answer == "4":
            quit()






user_input()