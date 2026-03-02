# importing hashlib
import hashlib
def sha256_hash(text):
    '''
    This funtion takes in the text which is a string
    then will encode the text to bytes.
    then will pass it into a hash.
    then will call hexdigest to turn into readable format.
    Returns:
        result as readable hexstring
    '''
    byte_encode = text.encode()
    hashed = hashlib.sha256(byte_encode)

    return hashed.hexdigest()



def integrity_check(text1, text2):
    '''
    This function will perform an intergrity check by calling
    the sha256_hash function on two string texts given.
    then comparing if both are the same hash.
    Returns:
        boolean for if hashes are the same or not.
    '''
    text1_hashed = sha256_hash(text1)
    text2_hashed = sha256_hash(text2)
    return text1_hashed == text2_hashed

