import logging

def setup_logger():
    '''
    Creates a logger that writes to both the terminal and 
    a file called attack_log.txt

    Returns:
        logger object so attacker.py can use it.

    '''
    logger = logging.getLogger("AttackLogger") # Create logger object
    logger.setLevel(logging.DEBUG) # capture all levels

    # format how each line looks
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler("attack_log.txt") # Writes to attack_log.txt
    stream_handler = logging.StreamHandler() # Prints to terminal

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
