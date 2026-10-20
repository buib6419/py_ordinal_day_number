from datetime import date

#: The epoch used by this library. 1970-01-01 maps to ordinal 1.
#: Chosen for human-recognisability over the proleptic-Gregorian
#: "day 0" used by datetime.toordinal (which dates back to year 1).
#: Ordinals here are 1-based, never zero or negative.
EPOCH = date(1970, 1, 1)


def date_to_ordinal(d):
    """Convert a date to a 1-based ordinal day number.

    1970-01-01 -> 1, 1970-01-02 -> 2, etc.

    Only dates on or after EPOCH (1970-01-01) are supported. Dates
    before the epoch raise ValueError; this keeps every returned
    ordinal a positive integer suitable for array indexing.
    """
    if not isinstance(d, date):
        raise TypeError("d must be a datetime.date")
    if d < EPOCH:
        raise ValueError("dates before 1970-01-01 are not supported")
    return d.toordinal() - EPOCH.toordinal() + 1


def ordinal_to_date(n):
    """Convert a 1-based ordinal day number to a date.

    1 -> 1970-01-01, 2 -> 1970-01-02, etc.

    Only positive integers are valid; this matches the 1-based
    scheme and guarantees the result is on or after EPOCH.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an int")
    if n < 1:
        raise ValueError("n must be >= 1")
    return date.fromordinal(n + EPOCH.toordinal() - 1)
