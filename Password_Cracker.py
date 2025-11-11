import hashlib

def crack_passwords(hash_file, wordlist_file):

  with open(hash_file, "r") as f:
        hashes = {line.strip().lower() for line in f}

    with open(wordlist_file, "r", errors="ignore") as f:
        for word in f:
            word = word.strip()
            if not word:
                continue

          hashed_word = hashlib.md5(word.encode()).hexdigest()

            if hashed_word in hashes:
                print(f"[+] Cracked: {hashed_word} --> {word}")
                hashes.remove(hashed_word)

    for h in hashes:
        print(f"[-] FAILED: {h}")


def main():
    hash_file = input("Enter path to hash file: ").strip()
    wordlist_file = input("Enter path to wordlist file: ").strip()

    print("\n--- CRACKING STARTED ---")
    crack_passwords(hash_file, wordlist_file)
    print("--- CRACKING FINISHED ---")


if __name__ == "__main__":
    main()

