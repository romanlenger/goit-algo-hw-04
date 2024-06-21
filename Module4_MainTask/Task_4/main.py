from handlers import *

from variables import DATA_FILE


def parse_input(user_input: str):
    input = user_input.strip().split()
    command = input[0].lower()
    args = input[1:]
    return command, args


def main():
    # додано Json файл для зберігання даних
    data = load_contacts(DATA_FILE)

    command_handlers = {
        "hello": lambda _: "Hello, enter your command please(add, change, phone, all, exit):",
        "add": lambda args: add_contact(args[0], args[1], data, DATA_FILE) if len(args) == 2 else "Invalid input. Use: add [name] [phone]",
        "change": lambda args: change_contact(args[0], args[1], data, DATA_FILE) if len(args) == 2 else "Invalid input. Use: change [name] [phone]",
        "phone": lambda args: show_phone(args[0], data) if len(args) == 1 else "Invalid input. Use: phone [name]",
        "all": lambda _: show_all(data),
        "close": lambda _: exit_bot(),
        "exit": lambda _: exit_bot(),
    }
    

    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)
        handler = command_handlers.get(command)

        if handler:
            response = handler(args)
            print(response)

            if command in ["close", "exit"]:
                break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()