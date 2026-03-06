# Import login fuction from mock_login
from mock_login import login

# imports the logger to print 
from logger import setup_logger
logger = setup_logger()

def load_wordlist(filepath):
    '''
    opens a wordlist that contains password guesses.
    then strips whitespace and newline symbols.
    then stores each line in a list.
    Returns:
        a list containg each line in file.
    '''
    word_list = []
    
    try: # Try this file
        with open(filepath) as word_file:
            for line in word_file:
                word_list.append(line.strip())
    
    except FileNotFoundError: # if that fails do this instead.
        logger.error(f"Error file {filepath} not found")
        return []
    return word_list

def dictionary_attack(username, wordlist_path):
    '''
    calls load_wordlist(filepath) to get the password list.
    imports and calls login() from mock_login.py (the other program i created)
    then loops through every password from the list and tries
    login(username, password)

    Returns:
        Str saying success or failed if login works or not.
    '''

    max_attempts = 5 # added max attempt variable to mimick
    attempt_count = 0 # real life systems 

    passwords = load_wordlist(wordlist_path)
    for password in passwords:
        attempt_count += 1
        logger.info(f"[Attempt] Trying: {password}")
        if login(username, password):
            logger.warning(f"[SUCCESS] Password found: {password}")
            break
        if attempt_count >= max_attempts:
            logger.warning(f"[LOCKOUT] Too many attempts. Account Locked.")
            break
    else:
        logger.info(f"[FAILED] Password not Found in wordlist.")
            


if __name__ == "__main__":
    print(load_wordlist("wordlist.txt"))  # Should print your password list
    print(load_wordlist("fake.txt"))      # Should print the error + []
    dictionary_attack("user3", "wordlist.txt") # Calls the attack and finds the password
                                               # from the list for user3.

