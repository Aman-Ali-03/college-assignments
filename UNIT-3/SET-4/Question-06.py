# Write a Python program to check whether a given key exists in a dictionary.
# Example: Input Key: Name Output: Key Found
# Otherwise display: Key Not Found

student = {
    "name": "Aman",
    "age": 20,
    "branch": "CSE",
    "college": "RDEC",
    "semester": 3,
    "cgpa": 8.64
}

key = input("Enter your key :")

if key in student:
    print("Key found.")
else :
    print("Key not found")