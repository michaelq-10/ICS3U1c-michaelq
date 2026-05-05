def month_name(month_number: int) -> str:
    """Return the name of a month given its number (1-12), or 'error' for invalid input."""
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months.get(month_number, "error")


def main():
    for i in range(1, 13):
        print(f"Month {i}: {month_name(i)}")
    print(f"Month 43: {month_name(43)}")


if __name__ == "__main__":
    main()