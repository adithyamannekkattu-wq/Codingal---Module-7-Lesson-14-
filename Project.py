print("====================Notes Cleaner====================\n\n")


file=open("Unfiltered.txt", "w")
file.write("Important: Do Codingal Project\nImportant: Do Codingal Quiz\nJunk: Write engish note\nTo do: Scholex project\nJunk: Clean table\n")
file.close()


file=open("Unfiltered.txt", "r")
content=file.read()
print(content)
file.close()

skip=input("Skip lines starting with: ")
file=open("Unfiltered.txt", "r")
lines=file.readlines()

new_content=""

for line in lines:
    if line.startswith(skip):
        print(f"skip --> {line}")

    else:
        print(f"keep --> {line}")
        new_content=new_content+f"{line}\n"

file.close()

new=open("Filtered.txt", "w")
new.write(new_content)
new.close()
