"""Application-wide constants."""

# ----------- Log Messages -----------

INVALID_CHOICE_ERROR = "Invalid choice. Choice must be a number from 1 to 7."
EXIT_SUCCESS = "Exited successfully."
INVALID_ID_SALARY = "Invalid id or salary, ID and salary must be integer."
INVALID_DISPLAY_CHOICE = "Enter a valid choice."

TOTAL_EMPLOYEES = "Total number of employees: {}"

# ----------- Input Prompts -----------

ENTER_CHOICE = "Enter your choice between 0 and 9:"
ENTER_EMPLOYEE_ID_EDIT = "\nEnter the employee id to edit the salary: "
ENTER_NEW_SALARY = "Enter the new salary: "
ENTER_DISPLAY_CHOICE = "Enter your choice."
ENTER_DATE = "\nEnter the date in YYYY-MM-DD format to check weekday: "

CSV_INPUT_PROMPT = "Input: "

# ----------- Validation Messages -----------

NEGATIVE_ID_ERROR = "Id can not be a negative number."
NEGATIVE_SALARY_ERROR = "Salary can not be a negative number."

# ----------- Info Messages -----------

EMPLOYEE_CREATED = "Employee created successfully."

CSV_FORMAT_INFO = (
    "\nEnter the employee data as comma-separated values in the format:\n"
    "Employee id,Name,Position,salary"
)

DATE_WORKDAY_RESULT = "{} is a weekday: {}"


# ----------- create_employee_from_string -----------

INVALID_STRING_FORMAT = "The input does not match the format mentioned."
INVALID_EMPLOYEE_POSITION = "Invalid employee position: {}"

# ----------- create_employee / update_employee_salary -----------

EMPLOYEE_CREATED_SUCCESS = "Employee created successfully."
EMPLOYEE_ID_NOT_FOUND = "Employee id doesn't exist."
SALARY_UPDATED_SUCCESS = "Salary updated successfully."

# ----------- add_employee -----------

ENTER_EMPLOYEE_ID_CREATE = "\nEnter the employee id: "
ENTER_EMPLOYEE_NAME = "Enter the name of the employee: "
ENTER_EMPLOYEE_POSITION = "Enter the position of the employee: "
ENTER_EMPLOYEE_SALARY = "Enter the salary of the employee: "

ID_SHOULD_BE_POSITIVE = "Id should be positive."
EMPLOYEE_ALREADY_EXISTS = "Employee already exist."
EMPLOYEE_NAME_EMPTY = "Employee name can not be empty."
EMPLOYEE_POSITION_EMPTY = "Employee position cannot be empty."
SALARY_SHOULD_BE_POSITIVE = "Salary should be a positive number."

# ----------- Mentor / Mentee Input Prompts -----------

ENTER_INTERN_ID = "Enter intern id: "
ENTER_DEVELOPER_ID = "Enter developer id: "

# ----------- Mentor / Mentee Validation Messages -----------

INVALID_INTERN_ID = "Invalid intern id."
INVALID_DEVELOPER_ID = "Invalid developer id."
INVALID_GENERIC_INPUT = "Invalid input."
INVALID_EMPLOYEE_POSITION_INPUT = "Invalid position for the employee."

# ----------- Mentor / Mentee Info Messages -----------

MENTOR_ASSIGNED = "{} is now mentored by {}."
INTERN_NO_MENTOR = "{} has no mentor assigned."
INTERN_MENTOR_INFO = "{}'s mentor is {}."
DEVELOPER_NO_MENTEES = "{} has no mentees."
DEVELOPER_MENTEES_HEADER = "Mentees of {}:"


# ----------- Menus -----------

MAIN_MENU = """
Employee management system
    Menu
    1. Add an employee.
    2. Total number of employee.
    3. Modify salary of an employee.
    4. Display all employees.
    5. Check weekday.
    6. Create a instance using string data.
    7. Assign mentor
    8. Show intern mentor
    9. Show developer mentees
    0. Exit."""

DISPLAY_MENU = """Employee details.
    1. To display details of all employees.
    2. To display details of Developers.
    3. To display details of Interns."""
