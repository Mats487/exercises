import pytest
from tasks import *
from calendars import *
from datetime import date, timedelta


@pytest.fixture
def today():
    return date(2000, 1, 1)


@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)


@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)


@pytest.fixture
def calendar(today):
    return CalendarStub(today)


@pytest.fixture
def sut(calendar):
    return TaskList(calendar)


def test_creation(sut):
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_future(sut, tomorrow):
    # Arrange
    task = Task('Mowing the grass', tomorrow)

    # Act
    sut.add_task(task)

    # Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past(sut, yesterday):
    # Arrange
    task = Task('Mowing the grass', yesterday)

    # Act
    with pytest.raises(RuntimeError) as error:
        sut.add_task(task)

    # Assert
    assert error, f'Due date can not be in the past'
    assert 0 == len(sut)


def test_task_becomes_overdue(sut, calendar, today, tomorrow):
    # Arrange
    next_week = today + timedelta(weeks=1)
    task = Task('description', tomorrow)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks


def test_task_becomes_finished(sut, tomorrow):
    # Arrange
    task = Task('Mowing the grass', tomorrow)
    sut.add_task(task)

    # Act
    task.finished = True

    # Assert
    assert 1 == len(sut.finished_tasks)
    assert not [task] == sut.due_tasks
