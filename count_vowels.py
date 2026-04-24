# count_vowels.py - Count vowels in a string

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test
print(f"Vowels in 'Hello': {count_vowels('Hello')}")
print(f"Vowels in 'Python Programming': {count_vowels('Python Programming')}")