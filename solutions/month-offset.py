def month_offset(month):
    """Return the month offset for a given month number."""
    offsets = {
        1: 1,
        2: 4,
        3: 4,
        4: 0,
        5: 2,
        6: 5,
        7: 0,
        8: 3,
        9: 6,
        10: 1,
        11: 4,
        12: 6
    }
    return offsets.get(month, -1)


if __name__ == "__main__":
    # Test the function with months 1-12 and an invalid month
    for m in range(1, 13):
        print(f"Offset for month {m}: {month_offset(m)}")
    print(f"Offset for month 43: {month_offset(43)}")