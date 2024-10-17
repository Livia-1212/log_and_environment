import logging
from app.commands.commands import Command
from icecream import ic


class GreetCommand(Command):
    def execute(self):
        from app.app import App
        logging.info("Hello, This is a calculator!")

        logging.debug(ic(App))

        print("Hello, This is a calculator!")