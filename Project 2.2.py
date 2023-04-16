# Define the find function and assign arguments
def find(word, part):
    ''' 
    Args:
    word (str): The entire string sentence 
    part (str): The couple of letters we want to find within the string sentence
    '''
    # Set our fist index at 0
    index = 0 
    # And our 2nd index as the length of the part we are trying to find
    indexPart = len(part)
    # Make them .lower() so it gets rid of case sensitivity 
    word = word.lower()
    part = part.lower()
    # While loop as long as the index - the indexPart is less than the length of the word
    while index-indexPart <= len(word):
        #If the words first letter and the index + indexPart are equal to the part, return the index and break from loop
        if word[index:index + indexPart] == part: 
            return index
            break
        # If not, add 1 to the index until it gets to where is needed
        else: 
            index += 1
    # If the length of the part is more than the word, return Invalid 
    if len(part) > len(word):
        return "Invalid"
    # If the part isn't even in the word, it will print None because it just doesn't exist
# print(find('this is a sEntence', 'Sen'))
# print(find("Ms Yang Assigned this a While ago", "ign"))
# print(find("Why do we need test cases Ms Yang", "yang"))
# print(find("This is my last test case for this example and for the day goodbye", "dby"))
# print(find('Hello there', "dby"))
# print(find("Hello There", "Hello There Family"))