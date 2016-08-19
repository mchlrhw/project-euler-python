import logging

from .lib import largest_prime_factor


log = logging.getLogger()
log.setLevel(logging.INFO)


def main():
    print(largest_prime_factor(600851475143))


if __name__ == '__main__':
    main()
