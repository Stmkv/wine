def get_format_year(year: int) -> str:
    last_num = int(str(year)[-1])
    if 11 <= year <= 2:
        return f"лет"
    elif last_num == 1:
        return f"год"
    elif 2 <= last_num <= 4:
        return f"года"
    else:
        return f"лет"
