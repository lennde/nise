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
        sec = 1
        while sec < 60*60:
            sec += randint(1, 5)
            if random() <= chance:
                sound = 1
                sec += 2
            else:
                sound = 2
                sec += 2
            sound_planning.append(data_model.SoundPlanning(sound=sound, studyparticipant_id=studyparticipant_id,
                                                           start_time=sec))
        self.session.bulk_save_objects(sound_planning)
        self.session.commit()
        return sound_planning

    def get_sound_planning(self, participant_id):
        planning = []
        sound_plannings = self.session.query(data_model.SoundPlanning)\
                                      .filter(data_model.SoundPlanning.studyparticipant_id == participant_id).all()
        for sound_planning in sound_plannings:
            planning.append({'start_time': sound_planning.start_time, 'sound': sound_planning.sound})
        return planning

    def setup(self):
        data_model.create_db()
