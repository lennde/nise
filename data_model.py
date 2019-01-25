# @Lennard de Graaf

from sqlalchemy import Column, Integer, String, ForeignKey
from nise.database import Base, engine


class StudyParticipant(Base):
    __tablename__ = "studyparticipants"
    studyparticipant_id = Column(Integer, primary_key=True)
    name = Column(String)


class SoundPlanning(Base):
    __tablename__ = "soundplannings"
    soundplanning_id = Column(Integer, primary_key=True)
    studyparticipant_id = Column(Integer, ForeignKey('studyparticipants.studyparticipant_id'))
    start_time = Column(Integer)
    sound = Column(Integer)


def create_db():
    Base.metadata.create_all(engine)
