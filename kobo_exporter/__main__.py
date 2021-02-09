import docx
from kobo_exporter.model.model import read_bookmarks, format_bookamrk


doc = docx.Document()

bookmarks = read_bookmarks()
for bookmark in bookmarks:
    doc.add_paragraph(format_bookamrk(bookmark))
    doc.add_paragraph('')

doc.save('note.docx')
