def export_to_txt(email_content, filename="generated_email.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(email_content)
    return filename
