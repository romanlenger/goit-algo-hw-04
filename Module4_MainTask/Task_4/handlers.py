from data import *


def add_contact(name: str, phone: str, contacts: dict, jsonpath: str) -> str:
    contacts[name] = phone
    save_contacts(jsonpath, contacts)
    return "Contact added."


def change_contact(name: str, phone: str, contacts: dict, jsonpath: str) -> str:
    if name in contacts:
        contacts[name] = phone
        save_contacts(jsonpath, contacts)
        return "Contact updated."
    return "Contact not found."


def show_phone(name: str, contacts: dict) -> str:
    return contacts.get(name, "Contact not found.")


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def exit_bot():
    return "Good bye!"

