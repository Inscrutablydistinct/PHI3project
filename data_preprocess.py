import re
from spellchecker import SpellChecker

contraction_mapping = {
    "don't": "do not",
    "won't": "will not",
    "can't": "cannot",
    "should've": "should have",
    "it's": "it is"
}

spell = SpellChecker()

def lowercase(text):
    lower_text = text.lower()
    return lower_text

def rem_num(text):
    cleaned_sentences = re.sub(r'[+-.−]','',re.sub(r'\d+', '', text))
    return cleaned_sentences

def expand(text):
    expanded_sentence = ""
    expanded_words = [contraction_mapping.get(word.lower(), word) for word in text.split()]
    expanded_sentence += " ".join(expanded_words)
    return expanded_sentence

def correct_spelling(sentence):
    corrected_sentence = []
    words = sentence.split()
    for word in words:
        corrected_word = spell.correction(word)
        if isinstance(corrected_word, str):
            corrected_sentence.append(corrected_word)      
    return " ".join(corrected_sentence)

def whitespace(text):
    return (re.sub(r'\s{2,}', ' ', re.sub(r'\s+', ' ', text))).strip()

def preprocess(text):
    return correct_spelling(expand(whitespace(lowercase(rem_num(text)))))

