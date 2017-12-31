# Hash-Calculator

Simple md5 hash calculation using Python

Make a file "passwords.txt" with a list of common passwords to try for brute forcing.

The python script calculates md5 hash value of all the passwords in "passwords.txt" file and stores in a file "hash.txt" in the  
following format:  

\<password\>:\<hashed value\>

which can be split using ":" for getting the original password.  

Assumption : passwords.txt is in the same directory as hash_calculator.py

Steps:  
1) Go to terminal.  
2) Move to the directory where hash_calculator.py and passwords.txt file are present.  
3) Type the following:  
python hash_calculator.py  
The file with all the password:hash pairs i.e, hash.txt would be stored in the same directory.  


