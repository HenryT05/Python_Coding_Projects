import hashlib

# Dictonary Containing 3 different users and their stored password
# that is byte encoded and hashed as sha-256.
USER_DB = {
    "user1": hashlib.sha256("RandomPassword1".encode()).hexdigest(),
    "user2": hashlib.sha256("pythonrules".encode()).hexdigest(),
    "user3": hashlib.sha256("letmein".encode()).hexdigest()
}

def login(username, password):
    '''
    Checks if the username exits in USER_DB
    if yes then will hash the attempted password
    and then compare to USER_DB[username]
    Returns:
        Boolean
    '''
    if username in USER_DB:
        hashed_input = hashlib.sha256(password.encode()).hexdigest()
        if hashed_input == USER_DB[username]:
            return True
    return False

# Quick test
if __name__ == "__main__":
    print(login("user1", "RandomPassword1"))  # Should print True
    print(login("user1", "wrongpassword"))    # Should print False
    print(login("fakeuser", "anything"))      # Should print False

    '''
    Here we can see that in this login returning a false
    this means that an attacker trying to attack a login will not
    know if either the username or password is false. Meaning
    they cant use this info to keep trying until they find a 
    username that will work.
    '''