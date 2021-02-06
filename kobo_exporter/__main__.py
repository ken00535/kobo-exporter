from kobo_exporter.model.model import read_bookmarks


bookmarks = read_bookmarks()
for bookmark in bookmarks:
    print(bookmark.format_bookamrk())
