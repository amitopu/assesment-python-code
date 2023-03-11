# To check anagram python dictionary is used to store the number of occurance of 
# each charecters in the strings and then compared the number of occurance for both
# the strings. If each individual characters present exactly same number of times
# in both the strings then the strings are anagram of each other.

def anagram_checker(phrase1, phrase2):
    """
        This program checks if two strings are anagram or not. 
        if two strings are anagram then True is returned and False otherwise.
        time complexity is O(n) where n is the length of the largest phrase
        and space complexity is O(n). There is a container called counter() in python.
        counter() counts the number of occurance of each characters in a string. Comparing
        two counters for both the strings we can check if they are anagram of each other 
        or not. counter() doesnot use any auxiliary space like dictionaries. so it will
        be O(1) in space complexity.
    """
    # preprocess the pharases removing spaces and make them all lower case
    str1 = ''.join(phrase1.lower().split(' '))
    str2 = ''.join(phrase2.lower().split(' '))

    # if the length of the strings are not equal they are not anagram.
    if len(str1) == len(str2):

        # store the number of occurance of each characters in both the strings
        # to two different dictionaries
        dict1 = {}
        for char in str1:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char]  = 1
        dict2 = {}
        for char in str2:
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char]  = 1

        # check if number of occurance of each characters in both the strings
        # are equal or not.
        for key in dict1:
            if dict1[key] != dict2[key]:
                return False
        return True

    else:
        return False
    
if __name__ == "__main__":
    print(anagram_checker('hello I am Mike', 'Hii Mello make'))
    print(anagram_checker('myster ious', 'myst esious'))
    print(anagram_checker('digitalzoom', 'mooztaldigi'))
        