'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from text import tamil

PAD        = '_'
EOS        = '~'

# Export all symbols:
en_symbols = PAD+EOS+'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'(),-.:;? '

_arpabet = ['@' + s for s in tamil.tamil_letters]

symbols = [PAD, EOS]+ _arpabet