# bank-transactions

def add(list, item):
  list.append(item)


def remove(list, index):
  list.pop(index)


def clear(list):
  list.clear(item)


def print_list(list):
  print(list)

def reverse(list):
  list.reverse()

def index(list, item):
  print(list.index(item))

list = ["Georgijs Vasiļjevs", "Anastasija Krupiza"]
print("List is empty now, what you want to do?")
while True:
  choice = int(input("1. Add\n2. Remove\n3. Clear\n4. Print list\n5. Reverse\n6. Index\n"))
  if choice == 1:
    item = input("What you want to add?\n")
    add(list, item)
    print_list(list)
  elif choice == 2:
    index = int(input("What you want to remove?\n"))
    remove(list, index)
    print_list(list)
  elif choice == 3:
    clear(list)
    print_list(list)
  elif choice == 4:
    print_list(list)
  elif choice == 5:
    reverse(list)
    print_list(list)
  elif choice == 6:
    item = input("What you want to index?\n")
    index(list, item)
    print_list(list)
  else:
    print("Invalid input")