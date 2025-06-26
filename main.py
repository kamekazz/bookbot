from stats import get_num_of_words , count_characters

def get_book_text(_filepath):
    with open(f"books/{_filepath}") as f:
        file_contents = f.read()
        return file_contents




def main():
    book_date = get_book_text('frankenstein.txt')
    word_counts = count_characters(book_date)
    print( word_counts)
    #print(f"{get_num_of_words(book_date)} words found in the document")
    
main()