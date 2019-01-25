# @Lennard de Graaf

from database import Session
import data_model as data_model
from random import randint, random

session = Session()


class Context:
    def __init__(self):
        self.session = Session()

    def create_participant(self, name):
        participant = data_model.StudyParticipant(name=name)
        self.session.add(participant)
        self.session.commit()
        return participant

    def generate_sounds(self, studyparticipant_id, chance=0.50):
        sound_planning = []
        s = 1
        while s < 60*60:
            s += randint(1, 5)
            if random() <= chance:
                sound = 1
                s += 2
            else:
                sound = 2
                s += 2
            sound_planning.append(data_model.SoundPlanning(sound=sound, studyparticipant_id=studyparticipant_id,
                                                           start_time=s))
        self.session.bulk_save_objects(sound_planning)
        self.session.commit()
        return sound_planning

    def setup(self):
        data_model.create_db()
