#Phone Directory: add one or more numbers each entry. Print in sorted order and provide ability to search.

phone_book = {}

name = input("Please enter Name ('end' to stop): ")

while name != "end":
    number = input("Please enter number: ")
    if number.isdigit() and len(number) == 10:
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]

    else:
        print("Invalid phone number. Try again.")

    name = input("Please enter Name ('end' to stop): ")

else:
    print("Phone book saved successfully...")

print("-" * 50)
print("Phone Book - List of Contacts")
print("-" * 50)
for k,v in sorted(phone_book.items()):
    print(k,v)


print("-" * 50)
print("Phone Book - Search Contacts")
print("-" * 50)
name_for_search = input("Please enter name you would like to search: ")

while name_for_search != 'stop':
    try:
        numbers_for_name = phone_book[name_for_search]
        print(name_for_search, numbers_for_name)
        print("-" * 50)
    except KeyError:
        print("No contact found with name: ",name_for_search)
    finally:
        name_for_search = input("Please enter name you would like to search: ")