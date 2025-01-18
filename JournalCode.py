import os
import datetime

FILE_NAME = "journal_entries.txt"

def add_entry():
    """
    Add a new journal entry.
    """
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\nWrite your journal entry (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    entry = f"\n[Date: {date}]\n{' '.join(lines)}\n"
    
    with open(FILE_NAME, "a") as file:
        file.write(entry)
    print("\nEntry added successfully!")

def view_entries():
    """
    View all journal entries.
    """
    if not os.path.exists(FILE_NAME):
        print("\nNo journal entries found.")
        return
    
    print("\nYour Journal Entries:")
    with open(FILE_NAME, "r") as file:
        entries = file.read()
        print(entries if entries else "No entries to display.")

def search_entries():
    """
    Search journal entries by keyword.
    """
    if not os.path.exists(FILE_NAME):
        print("\nNo journal entries found.")
        return

    keyword = input("\nEnter a keyword to search for: ").strip()
    found = False

    with open(FILE_NAME, "r") as file:
        entries = file.readlines()
        print("\nSearch Results:")
        for line in entries:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

    if not found:
        print("No entries matched your search.")

def delete_entries():
    """
    Delete all journal entries.
    """
    if not os.path.exists(FILE_NAME):
        print("\nNo journal entries found.")
        return

    confirm = input("\nAre you sure you want to delete all journal entries? (yes/no): ").strip().lower()
    if confirm == "yes":
        os.remove(FILE_NAME)
        print("\nAll journal entries deleted.")
    else:
        print("\nDeletion canceled.")

def main():
    """
    Main menu for the journal app.
    """
    while True:
        print("\n=== Personal Journal App ===")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search Entries")
        print("4. Delete All Entries")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            delete_entries()
        elif choice == "5":
            print("\nExiting Journal App. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
