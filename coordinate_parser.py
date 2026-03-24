def parse_single_coordinate(part, width, height):
    """Parse a single coordinate token like 'a1' into a (row, col) tuple.

    Returns None if the token is invalid or refers to a cell outside the
    board dimensions supplied by width and height.
    """
    if not isinstance(part, str):
        return None
    part = part.strip().lower()
    if len(part) < 2:
        return None
    col_char = part[0]
    if col_char < 'a' or col_char > 'z':
        return None
    try:
        row_num = int(part[1:])
    except ValueError:
        return None
    col = ord(col_char) - ord('a')
    row = row_num - 1
    if 0 <= col < width and 0 <= row < height:
        return (row, col)
    return None
