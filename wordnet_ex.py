from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("positive"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print('Synonyms:')
print(set(synonyms))
print('\n')
print('Antonyms:')
print(set(antonyms))
