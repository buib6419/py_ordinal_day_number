# py_ordinal_day_number

Converts calendar dates to and from sequential day numbers for indexing.

```python
from datetime import date
from py_ordinal_day_number import date_to_ordinal, ordinal_to_date

n = date_to_ordinal(date(2024, 3, 15))   # 19765
print(n)
print(ordinal_to_date(n))               # 2024-03-15
```

## Why

When dates need to be stored in a compact, comparable form or used as
1-based indices into an array, converting to an integer is the simplest
approach. Python's `datetime.date` already has `toordinal()`/`fromordinal()`,
but that scheme counts from the proleptic Gregorian year 1 and returns a
large, unwieldy number (e.g. 738920 for 2024-03-15).

This library re-anchors ordinals to 1970-01-01, so that day maps to 1,
the next day to 2, and so on. The trade-off is that dates before 1970 are
rejected entirely — the returned ordinals are always positive integers,
which is what makes them safe for array indexing.

## Edge case

Any date before 1970-01-01 raises `ValueError`. Booleans are rejected for
ordinal input even though `bool` is a subclass of `int`, to prevent
silent bugs.
