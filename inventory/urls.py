from django.urls import path
from . import views

app_name = 'im'
urlpatterns = [
    path('', views.index, name='index'),
    path('consume/', views.consume, name='consume'),
    path('shoppinglist/', views.Shoppinglist.as_view(), name='shoppinglist'),
    # TODO: add exiperes before X date?
    # TODO: add categories
    # TODO: add pantry item selection
    path('expirations/', views.Expirations.as_view(), name='expirations'),
    path('item/<int:pk>/', views.DetailView.as_view(), name='pantryitemlinedetail'),
]
