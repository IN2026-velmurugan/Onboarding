"""Application-wide constants."""

CSV_FORMAT_INFO = (
    "\nEnter the employee data as comma-separated values in the format:\n"
    "Employee ID,Name,Position,salary"
)

DATE_WORKDAY_RESULT = "{} is a weekday: {}"

DEVELOPER_MENTEES_HEADER = "Mentees of {}:"
DEVELOPER_NO_MENTEES = "{} has no mentees."

DISPLAY_MENU = """Employee details.
    1. To display details of all employees.
    2. To display details of Developers.
    3. To display details of Interns."""

EMPLOYEE_ALREADY_EXISTS = "Employee already exist."
EMPLOYEE_CREATED = "Employee created successfully."
EMPLOYEE_CREATED_SUCCESS = "Employee created successfully."
EMPLOYEE_ID_NOT_FOUND = "Employee ID doesn't exist."
EMPLOYEE_NAME_EMPTY = "Employee name can not be empty."
EMPLOYEE_POSITION_EMPTY = "Employee position cannot be empty."

ENTER_CHOICE = "Enter your choice between 0 and 9:"
ENTER_DATE = "\nEnter the date in YYYY-MM-DD format to check weekday: "
ENTER_DEVELOPER_ID = "Enter developer ID: "
ENTER_DISPLAY_CHOICE = "Enter your choice."
ENTER_EMPLOYEE_ID_CREATE = "\nEnter the employee ID: "
ENTER_EMPLOYEE_ID_EDIT = "\nEnter the employee ID to edit the salary: "
ENTER_EMPLOYEE_NAME = "Enter the name of the employee: "
ENTER_EMPLOYEE_POSITION = "Enter the position of the employee: "
ENTER_EMPLOYEE_SALARY = "Enter the salary of the employee: "
ENTER_INTERN_ID = "Enter intern ID: "
ENTER_NEW_SALARY = "Enter the new salary: "

ERROR_ATTEMPT_EXCEEDED = "Attempt exceeded. Please try again."
ERROR_INVALID_OPERATION = "Invalid operation : {}"
ERROR_UNEXPECTED = "Unexpected application error"

EXIT_SUCCESS = "Exited successfully."

ID_SHOULD_BE_POSITIVE = "ID should be positive."

INFO_INTERRUPTED = "Application interrupted by user."

INVALID_CHOICE_ERROR = "Invalid choice. Choice must be a number from 1 to 7."
INVALID_DEVELOPER_ID = "Invalid developer ID."
INVALID_DISPLAY_CHOICE = "Enter a valid choice."
INVALID_EMPLOYEE_POSITION = "Invalid employee position: {}"
INVALID_EMPLOYEE_POSITION_INPUT = "Invalid position for the employee."
INVALID_GENERIC_INPUT = "Invalid input. {}"
INVALID_ID_SALARY = "Invalid ID or salary, ID and salary must be integer."
INVALID_INTERN_ID = "Invalid intern ID."
INVALID_STRING_FORMAT = "The input does not match the format mentioned."

INTERN_MENTOR_INFO = "{}'s mentor is {}."
INTERN_NO_MENTOR = "{} has no mentor assigned."

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

MENTOR_ASSIGNED = "{} is now mentored by {}."

NEGATIVE_ID_ERROR = "ID can not be a negative number."
NEGATIVE_SALARY_ERROR = "Salary can not be a negative number."

SALARY_SHOULD_BE_POSITIVE = "Salary should be a positive number."
SALARY_UPDATED_SUCCESS = "Salary updated successfully."

TOTAL_EMPLOYEES = "Total number of employees: {}"
