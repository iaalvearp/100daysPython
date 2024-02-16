import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode": # Angela's solution for the bug
        shift_amount *= -1
    for char in start_text:
        if not char in alphabet:
            end_text += char
        else:
            shift_amount%= 26
            position = alphabet.index(char)
            new_position = position + shift_amount        
            end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is: {end_text}")

# Angela's solution
should_end = False

while not should_end:
    print(art.logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))




    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

''' My solution for the bug
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            new_position = position - shift_amount
        elif cipher_direction == "encode":
            new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is: {end_text}")
'''

''' My solution to the complete challenge
want_to_continue = "yes"

while want_to_continue == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    index_list = []
    cipher_text = []

    def get_index_list(word, list):
        for char in word:
            if char == " ":
                list.append(" ")
            else:
                list.append(alphabet.index(char))

    def encrypt(indexs, shifted):
        for index in indexs:
            if index == " ":
                shifted.append(" ")
            elif direction == "encode":
                shifted.append(alphabet[index + shift])
            else:
                shifted.append(alphabet[index - shift])

    if direction == "encode":
        get_index_list(text, index_list)
        encrypt(index_list, cipher_text)
        print(f"Here's the encoded result: {''.join(cipher_text)}")
    elif direction == "decode":
        get_index_list(text, index_list)
        encrypt(index_list, cipher_text)
        print(f"Here's the decoded result: {''.join(cipher_text)}")
    else:
        print(f"Yoy write {direction} and that's a wrong choice!")
    
    want_to_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")'''


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
