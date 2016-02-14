from core.lib import create_admin_view
from xds_notes import models

create_admin_view(models.TaskProject)
create_admin_view(models.TaskList)
create_admin_view(models.Task)
