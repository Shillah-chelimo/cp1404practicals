class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initializes a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True if the programming language is dynamically typed, False otherwise."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Returns a string representation of the ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
