import random
import string
import logging as logger


def generate_random_new_user(prefix=None):

    if not prefix:
        prefix = 'testuser_'

    random_string_length = 8
    random_username = ''.join(random.choices(string.ascii_letters, k=random_string_length))

    random_username = prefix + random_username

    logger.info(f'Generated random username: {random_username}')

    # we can generate random password, but not this time
    random_password = '1234Abc'
    random_info = {"username": random_username, "password": random_password}

    # write random_info to the file config.ini to track names

    return random_info


def get_random_product_from_list(items):

    random_number = random.randint(1, len(items) - 1)
    item = {'page': str(random_number), 'name': items[random_number - 1]}

    return item
