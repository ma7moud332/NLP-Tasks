import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

def read_dataset(file_path):
    return pd.read_csv(file_path)

def tokenize_and_stem(text, stemmer):
    tokens = word_tokenize(str(text))  
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)  

# Main function
def main():
    dataset_path = "Dataset/Dataset_Python_Question_Answer.csv"  
    data_frame = read_dataset(dataset_path)
    porter_stemmer = PorterStemmer()
    snowball_stemmer = SnowballStemmer("english")

    data_frame["porter_stemmed_text"] = data_frame["Question"].apply(lambda x: tokenize_and_stem(x, porter_stemmer))
    data_frame["snowball_stemmed_text"] = data_frame["Question"].apply(lambda x: tokenize_and_stem(x, snowball_stemmer))
    print(data_frame[["porter_stemmed_text", "snowball_stemmed_text"]])

    output_file_path = "Output/Output.csv"
    data_frame.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    main()
