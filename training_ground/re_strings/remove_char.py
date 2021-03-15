def remove_char(text: str, pos: int) -> str:
    return text[:pos]+text[pos + 1:]


if __name__ == "__main__":
    print(remove_char('google.com', 4))
