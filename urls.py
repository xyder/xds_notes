from xds_notes import views
from tools.routing import url

urlpatterns = [
    url('/', view_func=views.index),
]
