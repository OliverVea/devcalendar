import datetime

from dataclasses import dataclass

from devcalendar.models.calendar_tag import CalendarTag


@dataclass
class CalendarEntry:
    name: str
    start: datetime.date
    tags: list[CalendarTag] = None
    end: datetime.date = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []

        if self.end is None:
            self.end = self.start

    def conflicts_with_date(self, date: datetime.date) -> bool:
        return self.start <= date <= self.end
