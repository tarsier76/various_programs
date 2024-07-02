doc_type_pdf = "pdf"
doc_type_txt = "txt"
doc_type_docx = "docx"
doc_type_md = "md"
doc_type_html = "html"


def conversion_type(doc_type):
    if doc_type == "pdf":
        return doc_type_html
    elif doc_type == "txt":
        return doc_type_pdf
    elif doc_type == "docx":
        return doc_type_md
    elif doc_type == "md":
        return doc_type_pdf
    elif doc_type == "html":
        return doc_type_txt
    else:
        raise Exception("Unknown document type")