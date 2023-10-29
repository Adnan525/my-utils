def stringify(s : str, sep : str):
    temp = s.split(sep)
    temp = [item.strip() for item in temp]
    return temp