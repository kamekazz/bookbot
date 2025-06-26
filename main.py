from stats import get_num_of_words , count_characters, convert_dic_list
import sys

def get_book_text(_filepath):
    with open(f"{_filepath}") as f:
        file_contents = f.read()
        return file_contents




def main():
      # 1) Make sure we got exactly one argument (the book path)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {book_path}...")
    book_date = get_book_text(book_path)
    print('----------- Word Count ----------')
    word_counts = count_characters(book_date)
    print(f"Found {get_num_of_words(book_date)} total words")
    print('--------- Character Count -------')
    list_of_char = convert_dic_list(word_counts)
    for char in list_of_char:
        c =char['char']
        n =char['num']
        print(f'{c}: {n}')
    print("============= END ===============")
    
main()

