import pywhatkit as kit
import selected_verse_of_the_day


class SendMessage:

    def __init__(self):
        self.PHONE_NUMBER = "+2712345678"  # enter a number in between the ""
        self.message = selected_verse_of_the_day.random_verse
        self.TIME_IN_HOURS = 22  # enter a time in hours
        self.TIME_IN_MINUTES = 30 # enter a time in minutes

    def details_message(self):
        kit.sendwhatmsg(self.PHONE_NUMBER, self.message, self.TIME_IN_HOURS, self.TIME_IN_MINUTES)