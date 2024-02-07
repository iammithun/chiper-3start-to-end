# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:55:30 2024

@author: iamrs
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(start_text, shift_amount, cipher_direction):
    end_text=''
    for letter in start_text:
        position=alphabet.index(letter)
        if cipher_direction == "decode":
            shift_amount*-1
        new_position=position+shift_amount
        end_text+=alphabet(new_position)
    print("The {cipher_text} text is{end_text}")
            

