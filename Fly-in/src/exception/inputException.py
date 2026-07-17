class InputError(Exception):
    def __init__(self, message: str) -> None:
        show_message = f"Input file error: {message}"
        super().__init__(show_message)
