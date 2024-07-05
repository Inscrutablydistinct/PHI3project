import re
from spellchecker import SpellChecker
from nltk.tokenize import sent_tokenize

# contraction_mapping = {
#     "don't": "do not",
#     "won't": "will not",
#     "can't": "cannot",
#     "should've": "should have",
#     "it's": "it is"
# }

# spell = SpellChecker()

# def lowercase(text):
#     lower_text = text.lower()
#     return lower_text

# def rem_num(text):
#     cleaned_sentences = re.sub(r'[+-.−]','',re.sub(r'\d+', '', text))
#     return cleaned_sentences

# def expand(text):
#     expanded_sentence = ""
#     expanded_words = [contraction_mapping.get(word.lower(), word) for word in text.split()]
#     expanded_sentence += " ".join(expanded_words)
#     return expanded_sentence

# def correct_spelling(sentence):
#     corrected_sentence = []
#     words = sentence.split()
#     for word in words:
#         corrected_word = spell.correction(word)
#         if isinstance(corrected_word, str):
#             corrected_sentence.append(corrected_word)      
#     return " ".join(corrected_sentence)

# def whitespace(text):
#     return (re.sub(r'\s{2,}', ' ', re.sub(r'\s+', ' ', text))).strip()

# def preprocess(text):
#     return correct_spelling(expand(whitespace(lowercase(rem_num(text)))))



# def extract_key_sentences(context):
#     keywords = [
#         "suggested that", "propose", "conjecture", "principle",
#         "claim", "represent", "model"
#     ]
#     sentences = sent_tokenize(context)
#     key_sentences = [
#         sentence for sentence in sentences
#         if any(keyword in sentence for keyword in keywords)
#     ]
#     return key_sentences

# def remove_references_and_emails(context):
#     context = re.sub(r'\S+@\S+', '', context)
#     context = re.sub(r'\[\d+\]', '', context)
#     context = re.sub(r'\(\d+\)', '', context)
#     context = re.sub(r'http\S+', '', context)
    
#     return context

# def preprocess(context):
#     context = remove_references_and_emails(context)
#     key_sentences = extract_key_sentences(context)
#     print(key_sentences)
#     refined_context = ' '.join(key_sentences)
#     return refined_context


def extract_key_sentences(context):

    keywords = [
    "measurement", "experiment", "theory", "values", "interaction", "proposal", 
    "verification", "quantum", "nonclassical", "weak values", "weak measurements", 
    "projector", "predictions", "dynamics", "eigenvalue", "imaginary part", 
    "real part", "inaccuracy", "entanglement", "counterfactual", 
    "observations", "data", "experimental", "realization", "implementation", 
    "analysis", "study", "research", "method", "technique", "procedure", 
    "findings", "results", "conclusion", "implications", "significance", 
    "accuracy", "precision", "instrumentation", "setup", "validation", 
    "hypothesis", "model", "simulation", "framework", "context", "overview", 
    "summary", "goal", "objective", "focus", "details", "elements", 
    "factors", "variables", "parameters", "conditions", "criteria", 
    "principles", "guidelines", "process", "system", "application", 
    "execution", "performance", "operation", "behavior", "function", 
    "task", "activity", "efficiency", "effectiveness", "skill", "expertise"
]

    sentences = sent_tokenize(context)
    
    key_sentences = [
        sentence for sentence in sentences
        if any(keyword in sentence for keyword in keywords)
    ]
    
    return key_sentences

def remove_references_and_emails(context):

    context = re.sub(r'\S+@\S+', '', context)

    context = re.sub(r'\[\d+\]', '', context)
    context = re.sub(r'\(\d+\)', '', context)

    context = re.sub(r'http\S+', '', context)
    
    return context

def format_references(context):
    references = re.sub(r'(\w+\. \w+\., "[^"]+", \w+\. \w+, vol\. \d+, pp\. \d+–\d+.)','', context)
    return references

def preprocess(context):
    context = remove_references_and_emails(context)
    # key_sentences = extract_key_sentences(context)
    # refined_context = ' '.join(key_sentences)
    references = format_references(context)
    return references


