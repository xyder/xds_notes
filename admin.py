from core.lib import create_admin_view
from xds_notes import models

create_admin_view(models.Note)
create_admin_view(models.NotesStream)
create_admin_view(models.NoteFile)
