import requests

"""
I know it's spaghetti code but cut me some slack...
I'm now just learning OOP techniques
"""

error_message = "Sorry , try searching the web for that"

class Dictionary:
    def __init__(self):
        return

    """
    Enclose everything in a try-except block since it is good practice to plan to fail
    """

    # In case the word is a noun
    def noun(self, word):
        content = requests.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}").json()
        try:
            noun_def = content[0]["meaning"]["noun"][0]["definition"]
            if not noun_def:
                return error_message
        except Exception:
            print("Encountered some bloody error")
            pass
        return noun_def

    # In case the word is a verb
    def verb(self, word):
        content = requests.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}").json()
        try:
            verb_def = content[0]["meaning"]["verb"][0]["definition"]
            if not verb_def:
                return error_message
        except Exception:
            print("Encountered some bloody error")
            pass
        return verb_def

    # In case the word is an adjective
    def adjective(self, word):
        content = requests.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}").json()
        try:
            adj_def = content[0]["meaning"]["verb"][0]["definition"]
            if not adj_def:
                return error_message
        except Exception:
            print("Encountered some bloody error")
            pass
        return adj_def

    # In case the word is a transitive verb
    def trans_verb(self, word):
        content = requests.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}").json()
        try:
            trans_verb_def = content[0]["meaning"]["transitive verb"][0]["definition"]
            if not trans_verb_def:
                return error_message
        except Exception:
            print("Encountered some bloody error")
            pass
        return trans_verb_def

    # Getting the audio pronunciation
    def audio(self, word):
        content = requests.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}").json()
        try:
            audio = content[0]["phonetics"][0]["audio"]
            if not audio:
                message = "Can't seem to find the pronunciation, try searching the web"
                return message
        except Exception:
            print("Some bloody problem encountered")
        return audio

