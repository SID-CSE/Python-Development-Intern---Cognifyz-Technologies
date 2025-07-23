# Level 2 :Task 5
# Task : File Manipulation
'''
 Write a Python program that reads a text file and counts the occurrences of each word in the file.
 Display the results in alphabetical order along with their respective counts.

'''

def count_words(filename):
    w_counts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                clean_line = line.strip().lower()
                words = clean_line.split()
                for word in words:
                    clean_word = ''
                    for char in word:
                        if char.isalnum():
                            clean_word += char

                    if clean_word:
                        if clean_word in w_counts:
                            w_counts[clean_word] += 1
                        else:
                            w_counts[clean_word] = 1

        print("\nWord Frequencies (Alphabetical Order):\n")
        for word in sorted(w_counts):
            print(f"{word}: {w_counts[word]}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = input("Enter the filename: ")
count_words(file_name)