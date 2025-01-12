def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count_words(text)
    print("--------------------")
    print("")
    print(f"Word count: {word_count}.")
    print("")
    print(f"{count_characters(text)}")

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