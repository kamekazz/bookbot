
def get_book_text(_filepath):
    with open(f"books/{_filepath}") as f:
        file_contents = f.read()
        return file_contents


def get_num_of_words(_text):
    return len(_text.split())


def main():
    book_date = get_book_text('frankenstein.txt')
    print(f"{get_num_of_words(book_date)} words found in the document")
    
main()