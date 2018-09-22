from django.urls import path
from . import views

app_name = 'im'
urlpatterns = [
    path('', views.index, name='index'),
    path('consume/', views.consume, name='consume'),
    path('shoppinglist/', views.shoppinglist, name='shoppinglist'),
    # TODO: add exiperes before X date?
    # TODO: add categories
    # TODO: add pantry item selection
    path('expirations/', views.Expirations.as_view(), name='expirations'),
    #TODO: later: add edit views instead of admin edits
    path('item/<int:pk>/', views.DetailView.as_view(), name='pantryitemlinedetail'),
]
