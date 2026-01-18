file_name="notes.txt"

def show_menu():
  print("\n----NOTE-TAKING APP Menu--")
  print("1.ADD A NEW NOTE:")
  print("2.VIEW ALL NOTES:")
  print("3.DELETE ALL NOTES:")
  print("4.EXIT:")


def add_note():
  note=input("enter ur note:")
  with open(file_name , "a") as file:
    file.write(note + "\n")
  print("note added!!")

def view_note():
  try:
    with open(file_name,"r") as file:
      content=file.read()
      if content:
        print("YOUR notes")
        print(content)
      else:
        print(" \n no notes")
  except FileNotFoundError:
    print("No notes")

def delete_notes():
  confirm =input("are you sure u want to delete (yes/n):")
  if confirm.lower()=="yes":
    with open(file_name, "w") as file:
      pass
    print("all nodes deleted")
  else:
    print("deletion cancelled")

while True:
  show_menu()
  choice = input("enter ur choice(1-4):")

  if choice == "1":
    add_note()
  elif choice == "2":
    view_note()
  elif choice == "3":
    delete_notes()
  elif choice == "4":
    print("bye")
    break

  else:
    print("wrong choice")  