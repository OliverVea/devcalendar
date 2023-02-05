import logging

from datetime import date, timedelta

from devcalendar.models import Calendar, CalendarEntry
from devcalendar.abstractions import CalendarProvider

class StaticCalendarProdider(CalendarProvider):
    def __init__(self, calendar: Calendar):
        self.calendar = calendar

    def internal_get_calendar(self) -> Calendar:
        return self.calendar

    def internal_store_calendar(self, calendar: Calendar):
        self.calendar = calendar

def get_dummy_static_provider() -> StaticCalendarProdider:
    logging.warning('Using dummy `CalendarProvider` meant for debugging.')

    start = date(2022, 11, 17)
    end = date(2022, 12, 3)
    entries = [
        CalendarEntry('entry 1', start, []),
        CalendarEntry('entry 2', end, ['tag A']),
        CalendarEntry('entry 3', start, ['tag B'], end),
        CalendarEntry('entry 4', start + timedelta(days=1),
                      ['tag A', 'tag B']),
    ]

    calendar = Calendar(start, end, entries)

    return StaticCalendarProdider(calendar)
