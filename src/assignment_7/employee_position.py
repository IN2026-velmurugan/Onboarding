"""Class for different employee category."""

from src.assignment_7.employee import Employee


class Manager(Employee):
    """Represent a manager employee."""

    def __init__(self, manager_id: int, name: str, salary: int) -> None:
        """Initialize a Manager instance.

        Args:
            manager_id: Unique identifier for the manager.
            name: Full name of the manager.
            salary: Salary of the manager.

        Returns:
            None.
        """
        super().__init__(manager_id, name, "Manager", salary)

    @classmethod
    def display_developers(cls) -> None:
        """Display all developers in the employee registry."""
        developer_list: list[Developer] = [
            dev for _dev_id, dev in cls.employee_data.items() if isinstance(dev, Developer)
        ]

        if not developer_list:
            print("There are no developers in employee data.")
            return

        print("Developer list:")
        for dev in developer_list:
            print(dev.name)

    @classmethod
    def display_interns(cls) -> None:
        """Display all interns in the employee registry."""
        intern_list: list[Intern] = [
            intern for _intern_id, intern in cls.employee_data.items() if isinstance(intern, Intern)
        ]

        if not intern_list:
            print("There are no interns in employee data.")
            return

        print("Intern list:")
        for intern in intern_list:
            print(intern.name)

    @classmethod
    def promote(cls, employee_id: int, new_role: str, increment_amount: int) -> None:
        """Promote an employee to a new role.

        Update the employee position and increase the salary
        by the specified increment amount.

        Args:
            employee_id: Identifier of the employee to promote.
            new_role: New role or position title.
            increment_amount: Salary increment amount.

        Returns:
            None.
        """
        if employee_id not in cls.employee_data:
            print("Employee id doesn't exist.")
            return

        cls.employee_data[employee_id].position = new_role
        cls.employee_data[employee_id].salary += increment_amount
        print(f"{cls.employee_data[employee_id].name} is promoted to {new_role}.")


class Developer(Employee):
    """Represent a developer employee."""

    def __init__(self, developer_id: int, name: str, salary: int) -> None:
        """Initialize a Developer instance.

        Args:
            developer_id: Unique identifier for the developer.
            name: Full name of the developer.
            salary: Salary of the developer.

        Returns:
            None.
        """
        super().__init__(developer_id, name, "Developer", salary)
        self.mentees: list[int] = []

    def map_mentee(self, intern_id: int) -> None:
        """Assign an intern as a mentee.

        Args:
            intern_id: Intern to be added as mentee.
        """
        intern = self.employee_data.get(intern_id)

        if not intern or not isinstance(intern, Intern):
            raise ValueError("Invalid intern id.")

        if intern_id in self.mentees:
            raise ValueError("Intern already assigned as mentee.")

        self.mentees.append(intern_id)

        print(f"{self.name} is now mentoring {intern.name}.")

    def get_mentees(self) -> list[str]:
        """List all mentees of this developer.

        Returns:
            List of mentees mapped to the developer.
        """
        return [self.employee_data[intern_id].name for intern_id in self.mentees]

    @classmethod
    def number_of_developer(cls) -> None:
        """Count and display the number of developers."""
        dev_count = 0
        for employee in cls.employee_data.values():
            if isinstance(employee, Developer):
                dev_count += 1
        print("The count of developers:", dev_count)


class Intern(Employee):
    """Represent an intern employee."""

    def __init__(self, intern_id: int, name: str, salary: int) -> None:
        """Initialize an Intern instance.

        Args:
            intern_id: Unique identifier for the intern.
            name: Full name of the intern.
            salary: Salary of the intern.

        Returns:
            None.
        """
        super().__init__(intern_id, name, "Intern", salary)
        self.mentor_id: int | None = None

    def assign_mentor(self, developer_id: int) -> None:
        """Request mentorship from a developer.

        Args:
            developer_id: Mentor ID from the developer list.

        Raises:
            ValueError: If the developer ID is invalid or if the mentee is already mapped.
        """
        developer = self.employee_data.get(developer_id)

        if not developer or not isinstance(developer, Developer):
            raise ValueError("Invalid developer id.")

        if self.mentor_id is not None:
            raise ValueError("Intern already has a mentor.")

        developer.map_mentee(self.employee_id)
        self.mentor_id = developer_id

    def get_mentor_name(self) -> str | None:
        """Display mentor details.

        Returns:
            Mentor mapped to the Intern.
        """
        if self.mentor_id is None:
            return None
        return self.employee_data[self.mentor_id].name

    @classmethod
    def number_of_intern(cls) -> None:
        """Count and display the number of interns."""
        intern_count = 0
        for employee in cls.employee_data.values():
            if isinstance(employee, Intern):
                intern_count += 1
        print("The count of interns:", intern_count)
