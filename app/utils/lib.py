def file_name_to_title(file: str) -> str:
    file_name = file.split(".")[0]
    name = file_name.replace("_", " ")
    return name.title()
