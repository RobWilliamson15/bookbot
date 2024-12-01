#with open("books/frankenstein.txt") as f:
#    file_contents = f.read()
    
#print(file_contents)

def number_of_words(book):
    words = book.split()
    return len(words)

#words = number_of_words(file_contents)
#print(len(words))

def number_of_each_character(text):
    count = {}
    lowered_string = text.lower()
    for c in lowered_string:
        count[c] = count.setdefault(c,0)+1
    return count

#count = number_of_each_character(file_contents)
#print(count)

def generate_report(file_path):
    
    with open(file_path, 'r') as file:
        text = file.read()

    word_count = number_of_words(text)

    character_count = number_of_each_character(text)

    sorted_characters = sorted(character_count.items(), key=lambda x: x[1], reverse=True)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    print("--- End of report ---")


file_path = "books/frankenstein.txt"
generate_report(file_path)

