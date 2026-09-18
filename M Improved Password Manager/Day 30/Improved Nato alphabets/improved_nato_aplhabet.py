import pandas
source_csv=pandas.read_csv("nato_phonetic_alphabet.csv")
aplha_dict={r.letter:r.code for (i, r) in source_csv.iterrows()}
def nato():
    word=input("Enter a word: ").upper()
    try:
        letter_list=[aplha_dict[letter] for letter in word]
        print(letter_list)
    except:
        print("Please enter a word containing only letters and nothing else.")
        nato()
nato()
