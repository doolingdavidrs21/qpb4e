"""Custom exceptions for the text_processor package."""


class TextProcessingError(Exception):
    """Base exception for text processing errors."""
    pass


class InvalidInputError(TextProcessingError):
    """Raised when input is of an invalid type."""
    pass


class InvalidValueError(TextProcessingError):
    """Raised when a value is invalid (e.g., negative count)."""
    pass
