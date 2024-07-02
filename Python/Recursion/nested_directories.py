def list_files(current_node, current_path=""):
    file_paths = []
    for node, content in current_node.items():
        new_path = f"{current_path}/{node}"
        if content is None:
            file_paths.append(new_path)
        else:
            file_paths.extend(list_files(content, new_path))
    return file_paths
