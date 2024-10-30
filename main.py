def main():
    path = "books/frankenstein.txt"
    text = open_file(path)
    count = count_words(text)
    print(f"{count}")

def open_file(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    list = text.split()
    return len(list)

main()