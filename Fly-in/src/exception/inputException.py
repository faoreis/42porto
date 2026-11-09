class InputError(Exception):
    def __init__(self, message: str, line_number: int = None) -> None:
        if line_number is not None:
            show_message = f"Input file error at line {line_number}: {message}"
        else:
            show_message = f"Input file error: {message}"
        super().__init__(show_message)
        self.line_number = line_number
