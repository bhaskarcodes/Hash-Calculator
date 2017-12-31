# PasswordCrack

Simple md5 password cracking using Python

Make a file "passwords.txt" with a list of common passwords to try for brute forcing.

The python script calculates md5 hash value of all the passwords in "passwords.txt" file and stores in a file "hash.txt" in the  
following format:  

\<password\>:\<hashed value\>

which can be split using ":" for getting the original password.  

Assumption : passwords.txt is in the same directory as hash_calculator.py


