import os


class DialogueScene():
    def __init__(self, world_name, scene_id):
        '''
        Use the world name and the scene id to locate all of the relevant content
        '''
        scene_file_location = os.path.join("worlds", world_name, "scenes", scene_id) + ".txt"
        print(scene_file_location)
        with open(scene_file_location) as f:
            scene_file_text = f.read()
        print(scene_file_text)
        character_directory = os.path.join("worlds", world_name, "characters")
        # self.dialogue = dialogue # "Hey", for example
        # self.character = character # The name of the character
        # self.speech = speech # the name of some audio file
        # self.base = base
        # self.visemes = visemes # the name of the folder with the visemes (just use the audio file?)
        # self.cycle = cycle # the name of the folder in the characters/{character}/visemes directory

class OptionsScene():
    def __init__(self, world_name, scene_id):
        scene_file_location = os.path.join("worlds", world_name, "scenes", scene_id) + ".txt"
        print(scene_file_location)
        with open(scene_file_location) as f:
            scene_file_text = f.read()
        character_directory = os.path.join("worlds", world_name, "characters")
        scene_options = scene_file_text.split("\n\n")
        # TODO: split the scene options into dialogue and gotos
        print(scene_options[0])

def scene(world, scene_id):
    pass

some_scene = OptionsScene("bincos default world", "0000001")