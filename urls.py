from core.routing import url
from xds_notes import views

urlpatterns = [
    url('/', view_func=views.index),
]
