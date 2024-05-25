def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        args_list = []
        kwargs_dictionary = {}

        for arg in args:
            args_list.append(convert_md_to_txt(arg))

        for kwarg in kwargs:
            kwargs_dictionary[kwarg] = convert_md_to_txt(kwargs[kwarg])

        return func(*args_list, **kwargs_dictionary)
    return wrapper

def convert_md_to_txt(doc):
    separated_lines = doc.split("\n")
    for line in separated_lines:
        separated_lines[separated_lines.index(line)] = line.lstrip('# ')
    return "\n".join(separated_lines)

@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""First: {first_doc}
Second: {second_doc}
"""

@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""Title: {title}
Body: {body}
Conclusion: {conclusion}
"""