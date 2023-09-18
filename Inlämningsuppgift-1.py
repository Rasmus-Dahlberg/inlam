"""
In this code I am asuming that the text file svenskt_text.txt is in the same directory as the python file.
If you need to change the path of the file you can do that in the "input_file" variable
"""

# We need to import io so that we can read and write in utf-8
import io

# This function will handle the actual translation of the text
def translate(text_file):
    consonants = "bcdfghjklmnpqrstvzx"
    translated_text = ""

    # This for loop will check every char individually from the text file
    for char in text_file:
        # If we find that the char exists in the consonant variable then we can change it to rövarspråk
        if char.lower() in consonants:
            translated_text += char + "o" + char
        # Else we will just add the char to the translated string as nothing needs to be done to it
        else:
            translated_text += char
    
    # We will send the translated text back so that we can create a new file with the translated text
    return translated_text

# This function handles the input and output file with read and write
def translate_file(input_file, output_file):
    # Here we initiate the file with the io import so we can read åäö in the file
    with io.open(input_file, mode="r", encoding="utf-8") as file:
        # Send the file content to the other function so it can be translated
        translated_text = translate(file.read())
    
    # We also need to use io here to write using utf-8 so that we can write åäö
    with io.open(output_file, mode="w", encoding="utf-8") as file:
        file.write(translated_text)
        print(f'This is the tanslated text:\n{translated_text}')


if __name__ == "__main__":
    # Variables are initiated here for an easier change later on
    input_file = "svenskt_text.txt"
    output_file = "svenskt_text_output.txt"

    # Send the files to the first function to inition the files and send text to the translate function
    translate_file(input_file, output_file)