import datetime

class Project:
    """Represents a project."""

    def __init__(self, name, start_date, priority, estimate, completion):
        """Initializes a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        """Returns a string representation of the Project instance."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.estimate}, completion: {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority

def load_projects(filename):
    """Loads projects from a file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip header
            for line in file:
                data = line.strip().split('\t')
                name, start_date, priority, estimate, completion = data
                start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                priority = int(priority)
                estimate = float(estimate)
                completion = int(completion)
                project = Project(name, start_date, priority, estimate, completion)
                projects.append(project)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return projects

def save_projects(filename, projects):
    """Saves projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}\t{project.completion}\n")

def display_projects(projects):
    """Displays all projects."""
    for project in projects:
        print(project)

def filter_projects_by_date(projects, date):
    """Filters projects by start date."""
    filtered_projects = [project for project in projects if project.start_date > date]
    return filtered_projects

def add_new_project():
    """Adds a new project."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, estimate, completion)

def update_project(projects):
    """Updates an existing project."""
    print("Current projects:")
    display_projects(projects)
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    if new_completion:
        project.completion = int(new_completion)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)

