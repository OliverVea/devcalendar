import logging
import argparse

from devcalendar import App
from devcalendar.logic import CalendarService
from devcalendar.storage import JsonCalendarProvider
from devcalendar.storage.__static_calendar_provider import get_dummy_static_provider

def main(debug: bool = False):
    if not debug:
        logging.basicConfig(filename='.log')

    calendar_provider = get_dummy_static_provider() if debug else JsonCalendarProvider('.data/calendar.json')
    calendar_service = CalendarService(calendar_provider)

    app = App('web', 'index.html', calendar_service)

    mode = 'edge' if debug else 'chrome'
    app.run(mode = mode)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--debug', action='store_true', help="Starts the application in debug mode.")

    args = parser.parse_args()

    main(args.debug)
