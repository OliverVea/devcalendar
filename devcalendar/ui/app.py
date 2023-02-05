import datetime
import json

import eel

from devcalendar.logic import CalendarService
from devcalendar.storage import DataclassEncoder

class App:
    def __init__(self,
            path: str,
            entry: str,
            calendar_service: CalendarService):

        self.path = path
        self.entry = entry
        self.service = calendar_service

    def register_endpoints(self):
        @eel.expose
        def get_dates() -> list[dict]:
            return [day.isoformat() for day in self.service.days()]

        @eel.expose
        def get_date_details(date_str: str) -> dict:
            date = datetime.date.fromisoformat(date_str)
            date_details = self.service.get_entries_for_date(date)
            return json.dumps(date_details, cls=DataclassEncoder)

        @eel.expose
        def get_tags() -> list[str]:
            raise NotImplementedError()


    def run(self, mode: str = 'chrome'):
        self.register_endpoints()
        eel.init(self.path)
        eel.start(self.entry, mode=mode)
