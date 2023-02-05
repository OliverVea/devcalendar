import datetime

from dataclasses import dataclass

from devcalendar.models.calendar_entry import CalendarEntry


@dataclass
class Calendar:
    start: datetime.date
    end: datetime.date
    entries: list[CalendarEntry] = None

    def __post_init__(self):
        if self.entries is None:
            self.entries = []
