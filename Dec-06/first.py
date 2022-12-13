def perform_task():
    with open("input") as f:
        lines = f.readlines()

    packet = lines[0].strip()
    required_symbols = 4
    marker = []

    for symbol_index in range(len(packet)):
        if len(marker) == required_symbols:
            marker.pop(0)
        marker.append(packet[symbol_index])
        if validate_marker(marker, required_symbols):
            print(symbol_index + 1)
            break


def validate_marker(marker, required_symbols):
    if len(marker) < required_symbols:
        return False

    unique_symbols = set()
    for symbol in marker:
        unique_symbols.add(symbol)

    if len(unique_symbols) == len(marker):
        return True
    else:
        return False


perform_task()
