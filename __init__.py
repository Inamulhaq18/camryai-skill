from mycroft import MycroftSkill, intent_file_handler


class Camryai(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('camryai.intent')
    def handle_camryai(self, message):
        self.speak_dialog('camryai')


def create_skill():
    return Camryai()

