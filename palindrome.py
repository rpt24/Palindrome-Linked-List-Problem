
# function to check if it's a palindrome
def isPalindrome(items) -> bool:
    # check the list against its reverse order to see if equal
    return items == items[::-1]

# main function to drive program
def main():
    # list of lists of data to iterate through and check
    data_items = [['1','2','1'],
                 ['1','0']]
    # iterate through the data items
    for data in data_items:
        # if palindrome is found print that data item
        if isPalindrome(data):
            print('Palindrome found!')
            print(data)
    
    
if __name__ == "__main__":
    main()