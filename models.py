from sqlalchemy import Column, Integer
from xds_server.core.database import Base
from xds_server.core.lib import get_custom_prefixer
from xds_server_apps.xds_notes import APP_NAME

prefixer = get_custom_prefixer(APP_NAME)


class NotesStream(Base):
    __tablename__ = prefixer('notes_streams')
    id = Column(Integer, primary_key=True)


class Note(Base):
    __tablename__ = prefixer('notes')
    id = Column(Integer, primary_key=True)


class NoteFile(Base):
    __tablename__ = prefixer('note_files')
    id = Column(Integer, primary_key=True)