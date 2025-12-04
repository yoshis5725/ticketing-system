import uuid


def create_random_ticket_number() -> str:
    """
    Create a random ticket number.
    :return: ticket number (str)
    """
    ticket_number = uuid.uuid4().hex[:8].upper()
    return f'TKT-{ticket_number}'