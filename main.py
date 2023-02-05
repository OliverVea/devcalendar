import logging
import argparse

from devcalendar import App
from devcalendar.logic import CalendarService
from devcalendar.storage import JsonCalendarProvider
from devcalendar.storage.__static_calendar_provider import get_dummy_static_provider

def main():
    logging.basicConfig(filename='.log')
    calendar_provider = JsonCalendarProvider('.data/calendar.json')
    calendar_service = CalendarService(calendar_provider)

    app = App('web', 'index.html', calendar_service)
    app.run()


def main_debug():
    calendar_provider = get_dummy_static_provider()
    calendar_service = CalendarService(calendar_provider)

    app = App('web', 'index.html', calendar_service)
    app.run(mode='edge')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--debug', action='store_true', default=False, help="Starts the application in debug mode.")

    args = parser.parse_args()

    if args.debug:
        main_debug()
    else:
        main()
