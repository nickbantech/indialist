from django.urls import path
from .views import (
	BizListView,
	BizDetailView,
	BizCreateView,
	BizUpdateView,
	BizDeleteView
	)
from . import views

urlpatterns = [
    path('', BizListView.as_view(), name='biz-home'),
    path('list/<int:pk>/', BizDetailView.as_view(), name='list-detail'),
    path('list/new/', BizCreateView.as_view(), name='list-create'),
    path('list/<int:pk>/update/', BizUpdateView.as_view(), name='list-update'),
    path('list/<int:pk>/delete/', BizDeleteView.as_view(), name='list-delete'),
    path('about/', views.about, name='biz-about'),
    path('category/', views.category, name='biz-category'),
]
