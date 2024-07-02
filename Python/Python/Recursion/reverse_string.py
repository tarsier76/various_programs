def reverse_string(s):
    if len(s) == 0:
        return ''
    else:
        reversed_string = reverse_string(s[1:]) 
        reversed_string += s[0]
        return reversed_string 

