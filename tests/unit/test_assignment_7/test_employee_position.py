import pytest
from src.assignment_7.employee import Employee
from src.assignment_7.employee_position import Developer, Intern, Manager


@pytest.fixture(autouse=True)
def reset_employee_data():
    Employee.employee_data.clear()
    yield
    Employee.employee_data.clear()


# Manager Tests

# display_developers()


def test_manager_display_developers_multiple(capsys):
    Manager(1, "Alice", 80000)
    Developer(2, "Bob", 60000)
    Developer(3, "Charlie", 65000)

    Manager.display_developers()
    out = capsys.readouterr().out

    assert "Bob" in out
    assert "Charlie" in out


def test_manager_display_developers_none(capsys):
    Manager(1, "Alice", 80000)

    Manager.display_developers()
    out = capsys.readouterr().out.lower()

    assert "no developers" in out


# display_interns()
def test_manager_display_interns_multiple(capsys):
    Manager(1, "Alice", 80000)
    Intern(2, "Bob", 30000)
    Intern(3, "Charlie", 32000)

    Manager.display_interns()
    out = capsys.readouterr().out

    assert "Bob" in out
    assert "Charlie" in out


def test_manager_display_interns_none(capsys):
    Manager(1, "Alice", 80000)

    Manager.display_interns()
    out = capsys.readouterr().out.lower()

    assert "no interns" in out


# promote()
def test_manager_promote_success(capsys):
    dev = Developer(1, "Bob", 60000)

    Manager.promote(1, "Senior Developer", 10000)

    assert dev.position == "Senior Developer"
    assert dev.salary == 70000

    out = capsys.readouterr().out.lower()
    assert "promoted" in out


def test_manager_promote_invalid_employee(capsys):
    Manager.promote(99, "Senior Developer", 10000)

    out = capsys.readouterr().out.lower()
    assert "doesn't exist" in out


def test_manager_promote_negative_increment(capsys):
    dev = Developer(1, "Bob", 60000)

    Manager.promote(1, "Senior Developer", -5000)

    assert dev.salary == 55000


# Developer Tests
# map_mentee()
def test_developer_map_mentee_success():
    Intern(1, "Alice", 30000)
    developer = Developer(2, "Bob", 60000)

    developer.map_mentee(1)

    assert 1 in developer.mentees


def test_developer_map_mentee_invalid_intern():
    developer = Developer(2, "Bob", 60000)

    with pytest.raises(ValueError, match="Invalid intern id"):
        developer.map_mentee(99)


def test_developer_map_mentee_not_intern():
    Manager(1, "Alice", 80000)
    developer = Developer(2, "Bob", 60000)

    with pytest.raises(ValueError, match="Invalid intern id"):
        developer.map_mentee(1)


def test_developer_map_mentee_duplicate():
    Intern(1, "Alice", 30000)
    developer = Developer(2, "Bob", 60000)

    developer.map_mentee(1)

    with pytest.raises(ValueError, match="already"):
        developer.map_mentee(1)


# get_mentees()


def test_developer_get_mentees_multiple():
    Intern(1, "Alice", 30000)
    Intern(3, "Charlie", 32000)
    developer = Developer(2, "Bob", 60000)

    developer.map_mentee(1)
    developer.map_mentee(3)

    assert developer.get_mentees() == ["Alice", "Charlie"]


def test_developer_get_mentees_empty():
    developer = Developer(2, "Bob", 60000)

    assert developer.get_mentees() == []


# number_of_developer()
def test_number_of_developer(capsys):
    Developer(1, "Alice", 60000)
    Developer(2, "Bob", 65000)
    Intern(3, "Charlie", 30000)

    Developer.number_of_developer()
    out = capsys.readouterr().out

    assert "2" in out


# Intern Tests


# assign_mentor()
def test_intern_assign_mentor_success():
    intern = Intern(1, "Alice", 30000)
    developer = Developer(2, "Bob", 60000)

    intern.assign_mentor(2)

    assert intern.mentor_id == 2
    assert 1 in developer.mentees


def test_intern_assign_mentor_invalid_developer():
    intern = Intern(1, "Alice", 30000)

    with pytest.raises(ValueError, match="Invalid developer id"):
        intern.assign_mentor(99)


def test_intern_assign_mentor_not_developer():
    intern = Intern(1, "Alice", 30000)
    Manager(2, "Bob", 80000)

    with pytest.raises(ValueError, match="Invalid developer id"):
        intern.assign_mentor(2)


def test_intern_assign_mentor_already_has_mentor():
    intern = Intern(1, "Alice", 30000)
    Developer(2, "Bob", 60000)
    Developer(3, "Charlie", 65000)

    intern.assign_mentor(2)

    with pytest.raises(ValueError, match="already has"):
        intern.assign_mentor(3)


# get_mentor_name()
def test_intern_get_mentor_name_success():
    intern = Intern(1, "Alice", 30000)
    Developer(2, "Bob", 60000)

    intern.assign_mentor(2)

    assert intern.get_mentor_name() == "Bob"


def test_intern_get_mentor_name_none():
    intern = Intern(1, "Alice", 30000)

    assert intern.get_mentor_name() is None


# number_of_intern()


def test_number_of_intern(capsys):
    Intern(1, "Alice", 30000)
    Intern(2, "Bob", 32000)
    Developer(3, "Charlie", 60000)

    Intern.number_of_intern()
    out = capsys.readouterr().out

    assert "2" in out
