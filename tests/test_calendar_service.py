from datetime import date, timedelta

from devcalendar.logic import CalendarService
from devcalendar.models import Calendar, CalendarEntry
from devcalendar.abstractions import CalendarProvider


class CalendarProviderMock(CalendarProvider):
    def __init__(self, calendar):
        self.calendar = calendar

    def internal_get_calendar(self):
        return self.calendar

    def internal_store_calendar(self, calendar):
        pass


def test_days__with_valid_range__returns_correct_dates(calendar: Calendar):
    provider = CalendarProviderMock(calendar)
    service = CalendarService(provider)
    days = service.days()

    assert len(days) is (calendar.end - calendar.start).days + 1
    assert days[0] == calendar.start
    assert days[-1] == calendar.end
    assert all((next - prev).days == 1 for prev, next in zip(days[:-1], days[1:]))


def test_get_entries_for_date__with_multiple_entries__correct_entries_are_returned():
    request_date = date(2022, 11, 17)
    entries = [
        CalendarEntry('a', request_date),
        CalendarEntry('b', request_date + timedelta(days=1)),
        CalendarEntry('c', request_date),
        CalendarEntry('d', request_date + timedelta(days=-1))
    ]

    start = request_date - timedelta(10)
    end = request_date + timedelta(10)

    calendar = Calendar(start, end, entries)
    provider = CalendarProviderMock(calendar)
    service = CalendarService(provider)

    date_entries = service.get_entries_for_date(request_date)

    assert len(date_entries) is 2
    assert date_entries[0] == entries[0]
    assert date_entries[1] == entries[2]

def test_get_entries_for_date__with_tagged_entries__correct_entries_are_returned():
    request_date = date(2022, 11, 17)

    tag = "correct_tag"
    other = "other_tag"

    entries = [
        CalendarEntry('a', request_date),
        CalendarEntry('b', request_date, tags=[tag]),
        CalendarEntry('c', request_date, tags=[other]),
        CalendarEntry('d', request_date, tags=[tag, other]),
    ]

    calendar = Calendar(request_date, request_date, entries)
    provider = CalendarProviderMock(calendar)
    service = CalendarService(provider)

    date_entries = service.get_entries_for_date(request_date, tags=[tag])

    assert len(date_entries) is 2
    assert date_entries[0] == entries[1]
    assert date_entries[1] == entries[3]
