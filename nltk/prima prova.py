import nltk
from nltk.tokenize import word_tokenize

def translate_to_logical(sentence):
    # Tokenizzazione della frase
    tokens = word_tokenize(sentence.lower(), language='italian')

    # Mappatura parole chiave a variabili proposizionali
    keyword_mapping = {
        "e": "∧",
        "o": "∨",
        "non": "¬",
        "non si dà il caso che" : "¬",
        "se": "→",
        "allora": "",  # Non necessaria per la traduzione
        "solamente": "",  # Non necessaria per la traduzione
        "se": "",    # Non necessaria per la traduzione
        "se e solo se": "↔",
        "è": "",    # Non necessaria per la traduzione
        "un": "",     # Non necessaria per la traduzione
        "per": "",   # Non necessaria per la traduzione
        "ma": "",   # Non necessaria per la traduzione
        "così": "",    # Non necessaria per la traduzione
        "ancora": ""    # Non necessaria per la traduzione
    }

    # Costruzione dell'espressione logica
    logical_expression = ""
    for token in tokens:
        if token not in keyword_mapping:
            logical_expression += token + " "
        else:
            logical_expression += keyword_mapping[token] + " "
    
    return logical_expression.strip()

# Test
sentence = input("Inserisci la frase: ")
logical_expression = translate_to_logical(sentence)
print("La traduzione in linguaggio logico è:", logical_expression)