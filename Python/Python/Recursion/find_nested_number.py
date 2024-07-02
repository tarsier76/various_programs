def count_nested_levels(nested_documents, target_document_id, level=1):
    if not nested_documents:
        return -1

    if target_document_id in nested_documents:
        return level  

    for document_id, nested_docs in nested_documents.items():
        nested_level = count_nested_levels(nested_docs, target_document_id, level + 1)
        if nested_level != -1:
            return nested_level

    return -1