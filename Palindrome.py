import argparse

def isPalindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    msg = "Please pass a string to check either it is palindrome or not"
    parser = argparse.ArgumentParser(description = msg)

    # Adding optional argument
    parser.add_argument("string", type = str, help='The input string to check for palindrome')
    
    # Read arguments from command line
    args = parser.parse_args()
    ans = isPalindrome(args.string)
    if ans:
        print("Yes")
    else:
        print("No")
