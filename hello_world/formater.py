PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON]


def get_formatted(msg, imie, format):
    if format == PLAIN:
        return plain_text(msg, imie)
    elif format == PLAIN_UP:
        return plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        return plain_text_lower_case(msg, imie)
    elif format == JSON:
        return format_to_json(msg, imie)


def format_to_json(msg, imie):
    return f'{{"imie":"{imie}", "msg":"{msg}"}}'


def plain_text(msg, imie):
    return imie + ' ' + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())