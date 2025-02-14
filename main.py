def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(f,file_contents)
        return file_contents

def character_counter(book):
    char_count={}
    characters=list(book)
    lower_chars=book.lower()
    for char in lower_chars:
        char_count[char]=lower_chars.count(char)
    return char_count

def word_counter(book):
    words = book.split()
    print(words)
    return len(words)   

print(
    character_counter(main())
    )   


