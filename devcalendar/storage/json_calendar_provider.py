import json

from dataclasses import asdict
from os import PathLike

from devcalendar.models import Calendar
from devcalendar.abstractions import CalendarProvider
from devcalendar.storage.dataclass_encoder import DataclassEncoder
from devcalendar.storage.calendar_decoder import CalendarDecoder

class JsonCalendarProvider(CalendarProvider):
    def __init__(self, path: PathLike):
        self.path = path

    def internal_get_calendar(self) -> Calendar:
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return CalendarDecoder.decode(data)


    def internal_store_calendar(self, calendar: Calendar):
        data = asdict(calendar)

        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, cls=DataclassEncoder)
