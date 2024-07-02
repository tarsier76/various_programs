def exponential_growth(n, factor, days):
    final_list = []
    if days == 0:
        final_list.append(n)
        return final_list
    for num in range(days + 1):
        final_list.append(n)
        n *= factor 
    return final_list

