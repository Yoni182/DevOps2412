# 1. Write the following code: a = 1/0;
# This line will cause a ZeroDivisionError

# 2. Build a corresponding try-except block to avoid exception
try:
    a = 1 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# 3. Check if the following code is legal
try:
    x = 1
finally:
    print("finally")
# Yes, this code is legal.

# 4 & 5. What exception types can be caught by the following handler and what is wrong with using it?
# except:
# This will catch all exceptions, which is not recommended as it can hide bugs.

# 6. What exceptions can be caught by the following handlers?
# except IOError:
# This will catch input/output related exceptions.

# except ZeroDivisionError:
# This will catch division by zero exceptions.

# 7. Create a text file named “words.txt” programmatically
with open("words.txt", "w") as file:
    pass

# 8. Write your name into the file
with open("words.txt", "w") as file1:
    file1.write("Yoni Chesla")

# 9. Read your file content and print it
with open("words.txt", "r") as file2:
    content = file2.read()
    print(content)

# 10. Write Hebrew content into your text file and print its content programmatically
with open("words.txt", "w", encoding="utf-8") as file3:
    file3.write("שלום עולם")  # Hebrew for 'Hello World'

with open("words.txt", "r", encoding="utf-8") as file4:
    content = file4.read()
    print(content)

from PIL import Image

# Create an image with RGB mode
width, height = 200, 200
image = Image.new('RGB', (width, height), color='crimson')

# Save the image
image.save('example1.png')
