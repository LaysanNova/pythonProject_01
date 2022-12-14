import random
import string
import logging as logger


def generate_random_new_user(prefix=None):

    if not prefix:
        prefix = 'testuser'

    random_string_length = 8
    random_username = ''.join(random.choices(string.ascii_letters, k=random_string_length))

    logger.info(f'Generated random username: {random_username}')

    # we can generate random password
    random_password = '1234Abc'
    random_info = {"username": random_username, "password": random_password}

    # write random_info to the file to track names

    return random_info


