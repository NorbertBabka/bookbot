def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(f,file_contents)
        return file_contents

def character_counter(book):
    char_count={}
    character_list=list(book.lower())
    character_set=set(character_list)
    for character in character_set:
        char_count[character]=character_list.count(character)
    return char_count

def word_counter(book):
    words = book.split()
    print(words)
    return len(words)   

print(
    character_counter(main())
    )   


