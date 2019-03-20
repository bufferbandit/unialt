#!/usr/bin/python3

def aa(starthex):
    alternate_alphabet = []
    starthex = hex(int(starthex, 16) - 1)
    for i in range(0, 26):
        i = int(starthex, 16)  ; i +=1
        uni_num = hex(i)[2:]
        starthex = hex(i)
        alternate_letter = chr(i)
        alternate_alphabet.append(alternate_letter)
    return alternate_alphabet


fonts = {

    "NORMAL_ALPHABET"                    : aa("0x00061"),
    "MONOSPACE_CAPITAL"                  : aa("0x1D670"),
    "MONOSPACE_MINISCULS"                : aa("0x1D68A"),

    "BOLD_CAPITAL"                       : aa("0x1D400"),
    "BOLD_MINISCULS"                     : aa("0x1D41A"),

    "ITALIC_CAPITAL"                     : aa("0x1D434"),
    "ITALIC_MINISCULS"                   : aa("0x1D44E"),

    "ITALIC_BOLD_CAPITAL"                : aa("0x1D468"),
    "ITALIC_BOLD_MINISULS"               : aa("0x1D482"),

    "SANS-SERIF_CAPITAL"                 : aa("0x1D5A0"),
    "SANS-SERIF_MINISCULS"               : aa("0x1D5BA"),

    "SANS-SERIF_BOLD_CAPITAL"            : aa("0x1D5D4"),
    "SANS-SERIF_BOLD_MINISCULS"          : aa("0x1D5EE"),

    "SANS-SERIF_ITALIC_CAPITAL"          : aa("0x1D608"),
    "SANS-SERIF_ITALIC_MINISCULS"        : aa("0x1D622"),

    "SANS-SERIF_BOLD_ITALIC_CAPITAL"     : aa("0x1D63C"),
    "SANS-SERIF_BOLD_ITALIC_MINISCULS"   : aa("0x1D656"),

    "sans-small": aa("0x1D400"),


        }


font = "SANS-SERIF_MINISCULS"
real = "NORMAL_ALPHABET"

real_alphabet      =  fonts[real]
alternate_alphabet =  fonts[font]

unicode_dictionary = dict(zip(real_alphabet, alternate_alphabet))

def unialt(real_sentence):
    alternative_sentence = ""
    for real_char in real_sentence:
        try:
            alt_char = unicode_dictionary[real_char]
            alternative_sentence += alt_char
        except KeyError:
            alternative_sentence += real_char
    return alternative_sentence
