"""
In this code I am asuming that the text file svenskt_text.txt is in the same directory as the python file.
If you need to change the path of the file you can do that in the "input_file" variable
"""

# We need to import io so that we can read and write in utf-8
import io
import os

class fileInfo:
    def __init__(self, input_File_Name = "", output_File_Name = "output.txt", consonants = "bcdfghjklmnpqrstvzx", translated_Text = "", original_Text = any):
        self._input_File_Name = input_File_Name
        self._output_File_Name = output_File_Name
        self._consonants = consonants
        self._translated_Text = translated_Text
        self._original_Text = original_Text
    
    def get_input_File_Name(self):
        return self._input_File_Name
    
    def set_input_File_Name(self, x):
        self._input_File_Name = x

    def get_output_File_Name(self):
        return self._output_File_Name
    
    def set_output_File_Name(self, x):
        self._output_File_Name = x
    
    def get_consonants(self):
        return self._consonants
    
    def set_consonants(self, x):
        self._consonants = x

    def get_translated_Text(self):
        return self._translated_Text
    
    def add_translated_Text(self, x):
        self._translated_Text += x

    def get_original_Text(self):
        return self._original_Text
    
    def set_original_Text(self, x):
        self._original_Text = x

# This will be our way to change and get the information in the class
file_info = fileInfo()

# This function will handle the actual translation of the text
def translate():
    # This for loop will check every char individually from the text file
    for char in file_info.get_original_Text():
        # If we find that the char exists in the consonant variable then we can change it to rövarspråk
        if char.lower() in file_info.get_consonants():
            file_info.add_translated_Text(char + "o" + char)
        # Else we will just add the char to the translated string as nothing needs to be done to it
        else:
            file_info.add_translated_Text(char)
    
    # No need to return the translated text as it's saved in the class

# This function handles the input and output file with read and write
def translate_file():
    # We are using try except if the file does not exsist and will print the OSError is that is the case
    try:
        if os.path.isfile(file_info.get_input_File_Name()) and os.path.getsize(file_info.get_input_File_Name()) > 0:

            # Here we initiate the file with the io import so we can read åäö in the file
            with io.open(file_info.get_input_File_Name(), mode="r", encoding="utf-8") as file:

                # Send the file content to the other function so it can be translated
                file_info.set_original_Text(file.read())

                # We tell it to start translating the text
                translate()
            
            # We also need to use io here to write using utf-8 so that we can write åäö to the files
            with io.open(file_info.get_output_File_Name(), mode="w", encoding="utf-8") as file:
                file.write(file_info.get_translated_Text())
                print(f'This is the tanslated text:\n{file_info.get_translated_Text()}')

        # If we find that there is no file or the file is empty we will say that it's empty
        else:
            print('There is nothing to translate')

    # catch the OSError is the file does not exsist
    except OSError as error:
        print(error)


if __name__ == "__main__":
    # Add the file to the class so that we can access it anywhere
    file_info.set_input_File_Name("svenskt_text.txt")

    # Start cheking and initializing the file given
    translate_file()