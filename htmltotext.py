'''
Phishing Website HTML Classification.
Dataset: https://www.kaggle.com/datasets/huntingdata11/phishing-website-html-classification
'''
import os
from bs4 import BeautifulSoup
import text2emotion
from spellchecker import SpellChecker
import textstat

spell = SpellChecker()

with open("data_phishing.csv", "w", encoding='utf-8') as f:
    f.write("Happy,Angry,Surprise,Sad,Fear,no_words,no_misspelled,readability,unique_words,class\n")

    for filename in os.listdir('training/Phish'):
        print(filename)
        with open(
            'training/Phish/' + filename,  # "training/NotPhish/0_biblehub_com.html",
            "r",
                encoding='utf-8') as html_page:
            # opening file_name.html so as to read it

            soup = BeautifulSoup(html_page, "html.parser")

            text = soup.get_text()
            # text = ''.join(html_text)
            # print(text)
            # print(type(text))
            emotions = text2emotion.get_emotion(text)
            print(f"{emotions=}")
            print(f"{len(text.split())=}")
            no_words = len(text.split())
            misspelled = spell.unknown(text)
            no_misspelled = 0 if no_words == 0 else len(misspelled) / no_words

            misspelled = spell.unknown(text)
            print(f"{len(misspelled)=}")
            readability = textstat.flesch_reading_ease(text)
            unique = len(set(text.split(' ')))

            # Creating html_text.txt File
            f.write(
                f"{emotions['Happy']},{emotions['Angry']},{emotions['Surprise']},{emotions['Sad']},{emotions['Fear']},{no_words},{no_misspelled},{readability},{unique},1\n")

    # {'Happy': 0.14, 'Angry': 0.12, 'Surprise': 0.29, 'Sad': 0.25, 'Fear': 0.2}
