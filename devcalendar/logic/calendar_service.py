import datetime
from typing import Optional

from devcalendar.models import CalendarEntry, CalendarTag
from devcalendar.abstractions import CalendarProvider


class CalendarService:
    def __init__(self, calendar_prodider: CalendarProvider):
        self.provider = calendar_prodider
        self.calendar = self.provider.get_calendar()

    def days(self) -> list[datetime.date]:
        delta = self.calendar.end - self.calendar.start
        return [self.calendar.start + datetime.timedelta(days=i) for i in range(delta.days + 1)]

    @staticmethod
    def __should_return_entry(
            entry: CalendarEntry,
            date: datetime.date,
            tags: list[CalendarTag]) -> bool:

        if not entry.conflicts_with_date(date):
            return False

        if tags and not all(tag in entry.tags for tag in tags):
            return False

        return True

    def get_entries_for_date(self,
            date: datetime.date,
            tags: Optional[list[CalendarTag]] = None) -> list[CalendarEntry]:

        tags = tags if tags is not None else []
        return [entry for entry in self.calendar.entries if self.__should_return_entry(entry, date, tags)]
