class DialogueScene():
    def __init__(self, character_name):
        self.dialogue = dialogue # "Hey", for example
        self.character = character # The name of the character
        self.speech = speech # the name of some audio file
        self.base = base
        self.visemes = visemes # the name of the folder with the visemes (just use the audio file?)
        self.cycle = cycle # the name of the folder in the characters/{character}/visemes directory

class OptionsScene():
    def __init__(self, dialogue_options):
        self.dialogue_options = dialogue_options # These will be in the /scenes/
