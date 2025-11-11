# Password Cracker

Description:
A simple Python-based password cracking tool that uses a dictionary to go against MD5 password hashes.
It reads a list of stolen hashes and attempts to find the original passwords by comparing MD5 hashes of words from a wordlist.

Problem it solves: 
Helps learners understand how password hashing works, why strong passwords are important, and how dictionary attacks operate in cybersecurity.

## Requirements

Python 3.6+

Files required:

Password_Cracker.py, hashes.txt, wordlist.txt

## Installation

Clone or download the repository:

git clone <your-repo-url>
cd jane-the-ripper-ken-a-c

python3 jane-the=ripper-ken-a-c

## Usage Examples

Run the password cracker:

python Password_Cracker.py

Example input when prompted:

Enter path to hash file: hashes.txt
Enter path to wordlist file: wordlist.txt

Sample output:

--- CRACKING STARTED ---
[+] Cracked: 5f4dcc3b5aa765d61d8327deb882cf99 --> password
[+] Cracked: e10adc3949ba59abbe56e057f20f883e --> 123456
[-] FAILED: d41d8cd98f00b204e9800998ecf8427e
--- CRACKING FINISHED ---

## Testing

None
