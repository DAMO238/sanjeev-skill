from mycroft import MycroftSkill, intent_file_handler


class Sanjeev(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sanjeev.intent')
    def handle_sanjeev(self, message):
        self.speak_dialog('sanjeev')


def create_skill():
    return Sanjeev()

