import sys

def caesar(plaintext,n):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # checking for space 
        if ch==" ":
            ans+=" "
        # if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

if __name__ == "__main__":

    print("Please enter the text you want to be encrypted")
    plaintext = sys.stdin.readline()
    if 'q' == plaintext.rstrip():
            print('Exit')
    else:
        print("Please enter the number of shifts")
        n = int(sys.stdin.readline())
        ciphertext = caesar(plaintext,n)
        sys.stdout.write("Cipher Text: " + ciphertext)





