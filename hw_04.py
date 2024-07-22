
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            print('There is no such name in contacts. Try another name')
        except IndexError:
            pass
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args





@input_error
def add_contact(args, contacts):
        name, phone = args
        if name not in contacts.keys():
            contacts[name] = phone
            return "Contact added."
        else:
            print('Contact with this name already exists. Please try "change" command')


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact updated.'


@input_error
def show_contact(args, contacts):
        name = args[0]
        return contacts[name]


@input_error
def all_contacts(args, contacts):
    return contacts

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(all_contacts(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()


