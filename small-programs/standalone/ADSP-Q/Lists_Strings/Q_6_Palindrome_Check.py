# Write a function that tests whether a string is a palindrome.

def test_palindrome(usr_input: str) -> bool:
    if usr_input == usr_input[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    usr_input = input("Enter a string: ").lower()
    if test_palindrome(usr_input):
        print("The string is palindrome!")
    else:
        print("The string isn't palindrome :( ")
