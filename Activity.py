print("====================Notes Cleaner====================\n\n")


file=open("Unfiltered.txt", "w")
file.write("Maths: Learn equations today\nCoding: Variables and loops\nScience: Photosynthesis\nCoding: If Statements\nEnglish: Essay Writing\nCoding: Functions and recursion\nHistory: World War II")
file.close()


char=int(input("How many characters to preview?: "))
file=open("Unfiltered.txt", "r")
characters=file.read(char)
print(characters)
print("")
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
