import yaml
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Bookmark(Base):
    __tablename__ = "Bookmark"

    id = Column('BookmarkID', Text, primary_key=True)
    book_id = Column('VolumeID', Text)
    text = Column('Text', Text)
    annotation = Column('Annotation', Text)


class Content(Base):
    __tablename__ = "content"

    id = Column('ContentID', Text, primary_key=True)
    book_id = Column('BookID', Text)
    book_title = Column('BookTitle', Text)


class Handler():
    def read_bookmarks(self, book_title=None) -> Bookmark:
        '''read bookmarks'''
        bookmarks = session.query(Bookmark, Content.book_title).\
            join(Content, Bookmark.book_id == Content.book_id).\
            filter(Content.book_title.like('%' + book_condition + '%')).\
            all()
        return bookmarks

    def format_bookamrk(self, bookmark) -> str:
        '''format bookmark to note'''
        if bookmark.Bookmark.annotation is None:
            bookmark.Bookmark.annotation = ""
        bookmark.Bookmark.text = bookmark.Bookmark.text.replace('\n', '')
        bookmark.Bookmark.text = bookmark.Bookmark.text.replace('\r', '')
        bookmark.Bookmark.text = bookmark.Bookmark.text.replace(' ', '')
        if bookmark.Bookmark.annotation != '':
            note = '「{:s}」《{:s}》\n'.\
                format(
                    bookmark.Bookmark.text,
                    bookmark.book_title
                )
        else:
            note = '「{:s}」《{:s}》'.\
                format(
                    bookmark.Bookmark.text,
                    bookmark.book_title
                )
        return note

    def format_annotation(self, bookmark) -> str:
        '''format annotation to note'''
        if bookmark.Bookmark.annotation is None:
            return ''
        if bookmark.Bookmark.annotation != '':
            note = '{:s}'.\
                format(
                    bookmark.Bookmark.annotation
                )
            return note
        return ''


with open("config/config.yaml", "r", encoding='utf-8') as stream:
    data = yaml.safe_load(stream)
    db_path = data['koboPath']
    book_condition = data['bookTitle']
db_url = 'sqlite:///{:s}'.format(db_path)
engine = create_engine(db_url)
Base.metadata.create_all(engine)
session_maker = sessionmaker(engine)
session = session_maker()
