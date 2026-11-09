import itertools
import string
import time

def brute_force_cracker(target_password):
    # Character set to use for generating guesses (lowercase letters + numbers)
    chars = string.ascii_lowercase + string.digits
    
    attempts = 0
    start_time = time.time()
    
    print(f"\n[*] Starting brute-force loop...")
    print(f"[*] Trying combinations against the target password...\n")
    
    # Try increasing lengths from 1 up to 6 characters
    for length in range(1, 7):
        # Generate all combinations of the current length
        for guess_tuple in itertools.product(chars, repeat=length):
            attempts += 1
            guess = "".join(guess_tuple)
            
            # Optional: Print progress update every 50,000 tries
            if attempts % 50000 == 0:
                print(f"[-] Tried {attempts:,} combinations... Current try: {guess}")
                
            # Check if our guess matches the target password
            if guess == target_password:
                end_time = time.time()
                elapsed_time = end_time - start_time
                return guess, attempts, elapsed_time
                
    return None, attempts, 0

def main():
    print("========================================")
    print("   Python Brute-Force Password Demo     ")
    print("========================================")
    
    # Option to enter the target password
    target = input("Enter a short password to crack (e.g., 'cat', 'ab12'): ").strip().lower()
    
    if not target:
        print("[!] Password cannot be empty.")
        return
        
    print(f"\n[+] Password recorded. Initiating attack simulation...")
    
    # Run the cracking function
    cracked_pass, total_attempts, duration = brute_force_cracker(target)
    
    if cracked_pass:
        print("\n" + "="*40)
        print(" 🎉 PASSWORD CRACKED SUCCESSFULLY! 🎉")
        print("="*40)
        print(f"  Target Password : {cracked_pass}")
        print(f"  Total Attempts  : {total_attempts:,}")
        print(f"  Time Taken      : {duration:.4f} seconds")
        print("="*40)
    else:
        print("\n[-] Failed to crack the password within the length limit.")

if __name__ == "__main__":
    main()