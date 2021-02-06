import yaml
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Bookmark(Base):
    __tablename__ = "Bookmark"

    id = Column('BookmarkID', Text, primary_key=True)
    text = Column('Text', Text)
    annotation = Column('Annotation', Text)

    def format_bookamrk(self) -> str:
        '''format bookmark to note'''
        if self.annotation is None:
            self.annotation = ""
        note = '「{:s}」\n{:s}\n'.format(self.text, self.annotation)
        return note


def read_bookmarks() -> Bookmark:
    '''read bookmarks'''
    bookmarks = db_session.query(Bookmark).all()
    return bookmarks

with open("config/config.yaml", "r") as stream:
    data = yaml.load(stream)
    db_path = data['koboPath']
db_string = 'sqlite:///{:s}'.format(db_path)

db = create_engine(db_string)
Base.metadata.create_all(db)
db_session = sessionmaker(db)()
