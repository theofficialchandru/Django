from django.contrib import admin
from libary.models import Book_management,Patron_management,Book_Borrowing
admin.site.register(Book_management)
admin.site.register(Patron_management)
admin.site.register(Book_Borrowing)
