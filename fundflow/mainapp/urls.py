from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("borrower_signup/", views.borrower_signup, name="borrower_signup"),
    path("lender_signup/", views.lender_signup, name="lender_signup"),
    path("success/", views.success, name="success"),
    path("borrower_data/", views.saveBorrower, name="borrower_data"),
    path("lender_data/", views.saveLender, name="lender_data"),
]
