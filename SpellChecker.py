# First install spellcheker
from spellchecker import SpellChecker
spell = SpellChecker()
misspelled = spell.unknown(['parayss', 'paralese', 'parallyslis', 'paralys'])
for word in misspelled:
    print(spell.correction(word))
    print(spell.candidates(word))
