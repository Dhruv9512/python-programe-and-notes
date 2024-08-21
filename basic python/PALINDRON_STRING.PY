str = input("Enter a sentence:- ").lower().split(' ')
new_str=''.join([n for n in str if not n==''])
if new_str==new_str[::-1]:
    print("The sentence",' '.join([n for n in str if not n=='']),"you enter is a palindrome.")
else:
     print("The sentence ",' '.join([n for n in str if not n=='']),"you enter is not a palindrome.")


print(new_str)


