from django.db import models
from .category import Category

class Todo(models.Model):

    CHOICE = [("pending", "Pending"),
    ("in_progress", "In Progress"),
    ("done", "Done"),]
    
    title = models.CharField(max_length=200)
    content = models.CharField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/")
    status = models.CharField(choices=CHOICE, default="pending")
    created_at = models.DateTimeField(auto_now_add=True) 
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")

    def __str__(self): 
        return self.title