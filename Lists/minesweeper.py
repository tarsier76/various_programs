def check_mines(board):
    list_of_lines = board.splitlines()
    separated_values = [list(i) for i in list_of_lines]

    def check_adjacent_mines(x, y):
        count = 0
        for i in range(max(0, x - 1), min(x + 2, len(separated_values))):
            for j in range(max(0, y - 1), min(y + 2, len(separated_values[0]))):
                if separated_values[i][j] == '*':
                    count += 1
        return count

    for i in range(len(separated_values)):
        for j in range(len(separated_values[i])):
            if separated_values[i][j] == '·':
                count = check_adjacent_mines(i, j)
                if count > 0:
                    separated_values[i][j] = str(count)

    return '\n'.join([''.join(row) for row in separated_values])

print(check_mines('''·*·*·
··*··
··*··
·····'''))
