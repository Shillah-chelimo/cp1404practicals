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

    def __lt__(self, other):
        """Defines the less than comparison between two Guitar objects based on their years."""
        return self.year < other.year

def load_guitars(filename):
    """Reads guitar data from a file and returns a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print("File not found.")
    return guitars

def display_guitars(guitars):
    """Displays the guitars in the list."""
    print("Guitars:")
    for index, guitar in enumerate(guitars, start=1):
        print(f"{index}. {guitar}")

def main():
    """Main function."""
    guitars = load_guitars('guitars.csv')
    
    print("Guitars before sorting:")
    display_guitars(guitars)
    
    guitars.sort()
    
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

if __name__ == "__main__":
    main()

