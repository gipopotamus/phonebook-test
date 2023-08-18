from phonebook_manager import Phonebook
from phonebook_entry import PhonebookEntry


def main():
    phonebook = Phonebook('phonebook.txt')
    """
        Запуск интерфейса управления телефонным справочником.
    """
    while True:
        print("Phonebook Menu:")
        print("1. Display Entries")
        print("2. Add New Entry")
        print("3. Edit Entry")
        print("4. Search Entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            phonebook.display_entries()
        elif choice == '2':
            last_name = input("Last Name: ")
            first_name = input("First Name: ")
            middle_name = input("Middle Name: ")
            organization = input("Organization: ")
            work_phone = input("Work Phone: ")
            personal_phone = input("Personal Phone: ")
            new_entry = PhonebookEntry(last_name, first_name, middle_name, organization, work_phone, personal_phone)
            phonebook.add_entry(new_entry)
            print("Entry added successfully!")
        elif choice == '3':
            index = int(input("Enter the index of the entry to edit: ")) - 1
            if 0 <= index < len(phonebook.entries):
                last_name = input("Last Name: ")
                first_name = input("First Name: ")
                middle_name = input("Middle Name: ")
                organization = input("Organization: ")
                work_phone = input("Work Phone: ")
                personal_phone = input("Personal Phone: ")
                new_entry = PhonebookEntry(last_name, first_name, middle_name, organization, work_phone, personal_phone)
                phonebook.edit_entry(index, new_entry)
                print("Entry edited successfully!")
            else:
                print("Invalid index.")
        elif choice == '4':
            query = input("Enter search query: ")
            results = phonebook.search_entries(query)
            if results:
                print("Search Results:")
                for idx, entry in enumerate(results, start=1):
                    print(f"{idx}. {entry.last_name} {entry.first_name} {entry.middle_name} ({entry.organization})")
                    print(f"   Work Phone: {entry.work_phone}")
                    print(f"   Personal Phone: {entry.personal_phone}")
                    print()
            else:
                print("No results found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
