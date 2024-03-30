from project_management import Project, load_projects, save_projects, display_projects, filter_projects_by_date, add_new_project, update_project


def main():
    print("Welcome to Pythonic Project Management")
    filename = "projects.txt"  # Default data file
    projects = load_projects(filename)
    
    while True:
        print_menu()
        choice = input(">>> ").lower()
        
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}.")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filtered_projects = filter_projects_by_date(projects, date)
            display_projects(filtered_projects)
        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_option = input("Would you like to save to projects.txt? ").lower()
            if save_option == 'yes' or save_option == 'y':
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    """Prints the menu options."""
    print("\nMenu:")
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

if __name__ == "__main__":
    main()
