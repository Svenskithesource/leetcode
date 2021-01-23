words = ["gin", "zen", "gig", "msg"]
dict_morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
                 'D': '-..', 'E': '.', 'F': '..-.',
                 'G': '--.', 'H': '....', 'I': '..',
                 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---',
                 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                 'S': '...', 'T': '-', 'U': '..-',
                 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..'}

l = []
for word in words:
    y = ""
    for i in range(0, len(word)):
        y += dict_morse[word[i].upper()]
    words[words.index(word)] = y

print(len(list(dict.fromkeys(words))))
