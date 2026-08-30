import pandas
source_csv=pandas.read_csv("nato_phonetic_alphabet.csv")
dict={r.letter:r.code for (i,r) in source_csv.iterrows()}
word=input("Enter a word: ").upper()
letter_list=[dict[letter] for letter in word]
print(letter_list)
