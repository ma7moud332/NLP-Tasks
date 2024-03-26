import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_words(text):
    return word_tokenize(text)

def tokenize_sentences(text):
    return sent_tokenize(text)

def tokenize_with_split(text):
    words = text.split()
    sentences = text.split('.')
    return words, sentences

def main():
    text = input("Please Enter The Text: ")
    print("\nChoose an option: \n1 - Tokenized words \n2 - Tokenized sentences \n3 - Output using split function.")

    choice = int(input("\nPlease Enter Your Choice: "))
    while choice < 1 or choice > 3:
        print("\nChoose a valid option.")
        choice = int(input("Enter Your Choice: "))

    if choice == 1:
        words = tokenize_words(text)
        print(words)
    elif choice == 2:
        sentences = tokenize_sentences(text)
        print(sentences)
    else:
        words, sentences = tokenize_with_split(text)
        print(f"Words: {words}")
        print(f"Sentences: {sentences}")

if __name__ == "__main__":
    nltk.download('punkt')  
    main()
