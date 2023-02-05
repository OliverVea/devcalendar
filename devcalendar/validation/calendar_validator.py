from datetime import date

from devcalendar.models import Calendar, CalendarEntry

def validate_calendar(calendar: Calendar):
    __validate_span(calendar.start, calendar.end)
    __validate_entries(calendar.entries)

def __validate_span(start: date, end: date):
    assert isinstance(start, date), '`start` must be a date.'
    assert isinstance(end, date), '`end` must be a date.'
    assert (start <= end), f"`start` cannot be after `end`, got start={start} and end={end}."

def __validate_entries(entries: None | list[CalendarEntry]):
    if entries is None:
        return
    assert isinstance(entries, list), f'`entries` must be none or a list of {CalendarEntry}.'
    for entry in entries:
        assert isinstance(entry, CalendarEntry), f'`entries` must be {CalendarEntry}.'
