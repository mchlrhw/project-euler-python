from collections import deque


DIGITS = {
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE',
}

SUBPOWERS = {
    1: 'TY',
    2: 'HUNDRED',
}

POWERS = {
    3: 'THOUSAND',
    6: 'MILLION',
    9: 'BILLION',
    12: 'TRILLION',
    15: 'QUADRILLION',
    18: 'QUINTILLION',
    21: 'SEXTILLION',
    24: 'SEPTILLION',
    27: 'OCTILLION',
    30: 'NONILLION',
    33: 'DECILLION',
    36: 'UNDECILLION',
    39: 'DUODECILLION',
    42: 'TREDECILLION',
    45: 'QUATTUORDECILLION',
    48: 'QUINDECILLION',
    51: 'SEXDECILLION',
    54: 'SEPTENDECILLION',
    57: 'OCTODECILLION',
    60: 'NOVEMDECILLION',
}


class HugeNumber(Exception): pass


def digit_groups(number):
    short = len(number) % 3
    if short:
        pad_len = 3 - short
        number = ('0'*pad_len) + number

    args = [iter(number)] * 3
    groups = zip(*args)
    return (str(int(''.join(group))) for group in groups)


def get_power_name(power):
    try:
        power_name = POWERS[power]
    except KeyError:
        raise HugeNumber('This module does not support such huge ints')
    return power_name


def clean_tys(name):
    name = name.replace(' TY', 'TY')
    name = name.replace('ONETY', 'TEN')
    name = name.replace('TWOTY', 'TWENTY')
    name = name.replace('THREETY', 'THIRTY')
    name = name.replace('FOURTY', 'FORTY')
    name = name.replace('FIVETY', 'FIFTY')
    name = name.replace('EIGHTTY', 'EIGHTY')
    return name


def clean_teens(name):
    name = name.replace('TEN ONE', 'ELEVEN')
    name = name.replace('TEN TWO', 'TWELVE')
    name = name.replace('TEN THREE', 'THIRTEEN')
    name = name.replace('TEN FOUR', 'FORTEEN')
    name = name.replace('TEN FIVE', 'FIFTEEN')
    name = name.replace('TEN SIX', 'SIXTEEN')
    name = name.replace('TEN SEVEN', 'SEVENTEEN')
    name = name.replace('TEN EIGHT', 'EIGHTEEN')
    name = name.replace('TEN NINE', 'NINETEEN')
    return name


def squash_hyphens(name):
    name = name.replace(' - ', '-')
    return name


def int_to_english(integer):
    if not isinstance(integer, int):
        raise RuntimeError('Argument must be an int')

    if integer == 0:
        return 'ZERO'

    prefix = ''
    if integer < 0:
        prefix = 'MINUS'

    digits = str(abs(integer))

    name = deque()
    groups = list(digit_groups(digits))
    for g_pos, group in enumerate(reversed(groups)):
        if not int(group):
            continue

        power = g_pos * 3
        if power:
            power_name = get_power_name(power)
            name.appendleft(power_name)

        group_val = int(group)
        for subpower, digit in enumerate(reversed(group)):
            if subpower == 1 and (group_val % 100) > 20 and group_val % 10:
                ten_sep = '-'
            else:
                ten_sep = ''

            if subpower == 2 and group_val % 100:
                hundred_sep = 'AND'
            else:
                hundred_sep = ''

            subpower_name = SUBPOWERS.get(subpower)

            digit_name = DIGITS.get(int(digit))
            if not digit_name:
                continue

            if ten_sep:
                name.appendleft(ten_sep)
            if hundred_sep:
                name.appendleft(hundred_sep)
            if subpower_name:
                name.appendleft(subpower_name)

            name.appendleft(digit_name)

    name.appendleft(prefix)

    name = ' '.join(name)
    name = clean_tys(name)
    name = clean_teens(name)
    name = squash_hyphens(name)
    name = name.strip()

    return name
