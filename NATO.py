import pandas as pd
df = pd.read_csv('nato_phonetic_alphabet.csv')

alphabet_dic = {row["letter"]:row["code"] for (index, row) in df.iterrows()}

user_text = input("please enter name:").upper()
phonetic_list =[alphabet_dic[letter] for letter in user_text]

print(phonetic_list)