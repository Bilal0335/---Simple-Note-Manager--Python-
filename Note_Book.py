'''
Simple Note Manager (Python)
'''

import os

print("="*40)
print("📒 Simple Note Manager (Python)")
print("="*40)

def create_note(file_path):
    content = input("Write your note: ")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✅ Note saved successfully in '{file_path}'!")

def read_note(file_path):
    try:
        with open(file_path, 'r') as f:
            print("\n📖 Your Note:\n" + f.read())
    except FileNotFoundError:
        print("❌ File not found!")

def append_note(file_path):
    content = input("Write your note: ")
    with open(file_path, 'a') as f:
        f.write(f"\n{content}")
    print("✅ Note appended successfully!")

def edit_note(file_path):
    try:
        with open(file_path, 'r') as f:
            print("\n📖 Current Note:\n", f.read())
        new_content = input("Enter new content: ")
        with open(file_path, 'w') as f:
            f.write(new_content)
        print("✅ Note updated successfully!")
    except FileNotFoundError:
        print("❌ File not found!")

# 📌 Main Function
def main():
    
    folder_name = input("Enter folder name: ")  
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)  
    
    filename = input("Enter note filename: ") + ".txt"
    file_path = os.path.join(folder_name, filename)  

    while True:
        print("\n📌 Menu:")
        print("1️⃣ Create Note")
        print("2️⃣ Read Note")
        print("3️⃣ Append Note")
        print("4️⃣ Edit Note")
        print("5️⃣ Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create_note(file_path)
            elif choice == 2:
                read_note(file_path)
            elif choice == 3:
                append_note(file_path)
            elif choice == 4:
                edit_note(file_path)
            elif choice == 5:
                print("🔴 Exiting...")
                break
            else:
                print("❌ Invalid choice. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number!")

# Run the program
main()
