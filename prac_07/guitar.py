class Guitar:
    """Represents a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initializes a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Returns the age of the guitar."""
        return 2024 - self.year

    def is_vintage(self):
        """Returns True if the guitar is vintage (50 or more years old), False otherwise."""
        return self.get_age() >= 50

    def __str__(self):
        """Returns a string representation of the Guitar instance."""
        cost_str = "${:,.2f}".format(self.cost)
        return f"{self.name} ({self.year}) : {cost_str}"
