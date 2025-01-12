def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count_words(text)
    items_list = list(count_characters(text).items()) # Converts the dictionary into a list.

    sorted_items_list = sorted(items_list, key=lambda x: x[1], reverse=True) # Sorts the list by the count of characters.

    print(f"--- Book report of {book_path} ---")
    print()
    print(f"Word count: {word_count}.")
    print()
    print("Character count:")
    print()
    for item in sorted_items_list:
        if item[0].isalpha(): # Checks if the character is a letter.
            
            print(f"There are {item[1]} {item[0]}'s.")
    print()
    print("--- End of book report ---")
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    character_count_dict = {}
    lowered_text = text.lower()
    
    for character in lowered_text:
        if character in character_count_dict:
            character_count_dict[character] += 1
        else:
            character_count_dict[character] = 1
    return character_count_dict


        

main()