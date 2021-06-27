class StateChoices:
    EXELENT = 0
    VERY_GOOD = 1
    GOOD = 2
    TO_REPAIR = 3

    CHOICES = (
        (EXELENT, 'Exelente'),
        (VERY_GOOD, 'Muy bueno'),
        (GOOD, 'Bueno'),
        (TO_REPAIR, 'A reparar'),
    )


class HomeType:
    HOUSE = 0
    APARTMENT = 1
    PH = 2
    DUPLEX = 3

    CHOICES = (
        (HOUSE, 'Casa'),
        (APARTMENT, 'departamento'),
        (PH, 'PH'),
        (DUPLEX, 'Duplex'),
    )
