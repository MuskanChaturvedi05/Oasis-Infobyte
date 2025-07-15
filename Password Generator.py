#My python program of Password Generator
import random
import string
print("THIS IS MY PASSWORD GENERATOR")
def main():
    
    length = int(input("Enter The Lengh Of Your Password: "))
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    symbolsD = string.punctuation
    combine = lowerD+upperD+digitD+symbolsD
    x = random.sample(combine,length)
    password ="".join(x)
    print("Your Password Is:", password) 
    main()
main()    
