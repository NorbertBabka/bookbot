def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
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
    return len(words)   

alphabet = "abcdefghijklmnopqrstuvwxyz"

print(
   f"--- Begin report of books/frankenstein.txt ---\n{word_counter(main())} words found in the document\n"
)
character_report=character_counter(main())
for character in character_report:
    if (character in alphabet) == True:
        print(
            f"The '{character}' character was found {character_report[character]} times"
        )
print("--- End of report ---")
