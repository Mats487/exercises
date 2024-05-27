import pytest
from tasks import *
from calendars import *
from datetime import date, timedelta


def test_creation():
    # Arrange
    today = date(2000, 1, 1)
    calendar = CalendarStub(today)

    # Act
    sut = TaskList(calendar)

    # Assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_future():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    task = Task('Mowing the grass', tomorrow)

    # Act
    sut.add_task(task)

    # Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past():
    # Arrange
    today = date(2000, 1, 1)
    due = date(1999, 12, 30)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    task = Task('Mowing the grass', due)

    # Act
    with pytest.raises(RuntimeError) as error:
        sut.add_task(task)

    # Assert
    assert error, f'Due date can not be in the past'
    assert 0 == len(sut)

def test_task_becomes_finished():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    task = Task('Mowing the grass', tomorrow)
    sut.add_task(task)

    # Act
    task.finished = True
    
    # Assert
    assert 1 == len(sut.finished_tasks)
    assert not [task] == sut.due_tasks