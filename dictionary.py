import requests


def dictionary(word):
    content = requests.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}").json()
    definition = []

    # Handle exceptions of different types of words
    try:
        noun_def = content[0]["meaning"]["noun"][0]["definition"]
        pronunciation = content[0]["phonetics"][0]["text"]
        example = content[0]["meaning"]["noun"][0]["example"]
        synonyms = content[0]["meaning"]["noun"][0]["synonyms"]
        syn = []
        for synonym in synonyms:
            syn.append(synonym)
        definition.append(noun_def)
    except Exception:
        pass

    try:
        verb_def = content[0]["meaning"]["verb"][0]["definition"]
        pronunciation = content[0]["phonetics"][0]["text"]
        example = content[0]["meaning"]["verb"][0]["example"]
        synonyms = content[0]["meaning"]["verb"][0]["synonyms"]
        syn = []
        for synonym in synonyms:
            syn.append(synonym)
    except Exception:
        pass

    try:
        adj_def = content[0]["meaning"]["adjective"][0]["definition"]
        pronunciation = content[0]["phonetics"][0]["text"]
        example = content[0]["meaning"]["adjective"][0]["example"]
        synonyms = content[0]["meaning"]["adjective"][0]["synonyms"]
        syn = []
        for synonym in synonyms:
            syn.append(synonym)
    except KeyError:
        pass

    try:
        trans_verb = content[0]["meaning"]["transitive verb"][0]["definition"]
        pronunciation = content[0]["phonetics"][0]["text"]
        example = content[0]["meaning"]["transitive verb"][0]["example"]
        synonyms = content[0]["meaning"]["transitive verb"][0]["synonyms"]
        syn = []
        for synonym in synonyms:
            syn.append(synonym)
    except Exception:
        pass

    try:
        audio = content[0]["phonetics"][0]["audio"]
    except Exception:
        print("Some bloody problem encountered.")

    return definition
