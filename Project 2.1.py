# # Get user input for a word if want input, or just call function at the end
# word = input('Enter a word: ')

# Define a function as a palindrome checker 
def paliChecker(word):
    '''
    Args:
    word (str): Takes in the word itself
    newList (list): Breaks the word up into a list 
    '''
    # #Convert the word into a list of characters, toggle the print function if only using this function 
    newList = list(word.lower())
    # print(newList)
    # Check if the word is a palindromeS
    while True: 
        if newList[0:1] == newList[-1:]:
            del newList[0:1]
            del newList[-1:]
            if len(newList) <= 1:
                # If the word is a palindrome, print a success message and break out of the loop
                # When needed, toggle the comment around the print function
                # print("This is a palindrome")
                return True
                break
        else:
            # If the word isn't a palindrome, print a failure message and break out of the loop
            # When needed, toggle the comment around the print function
            # print("This is not a palindrome")
            return False
            break
# paliChecker('rAcecAR')
# paliChecker('MothEr')
# paliChecker('saippuakivikauppias')
# paliChecker('haPPEN')
# paliChecker('rAceaCaR')
# paliChecker('PalInDrome')
# paliChecker('madam')
# paliChecker('redder')


# Open the file word.txt
fin = open("words.txt")
# Set the palindrome count to 0
count = 0
#Define the paliCount function 
def paliCount():
    ''' Uses the paliChecker() function
    and uses fin (file): just has the entire words.txt file to that variable 
    '''
    for line in fin:
        word = line.strip()
        # Use global count to make sure the count variable can be edited and used anywhere
        global count
        # If the paliChecker() function is True, add 1 to the count
        if paliChecker(word) is True:
            count += 1
        # If the paliChecker() function is False, don't add anything to the count
        if paliChecker(word) is False:
            count += 0
    print(f'There are {count} palindromes.')
# Call the function
paliCount()

