from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    email = models.EmailField()
    parol = models.TextField()


class Event(models.Model):
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    content = models.TextField(blank=True)

    IMPORTANCE = (
        ('v', 'Важная'),
        ('s', 'Средняя'),
        ('n', 'Неважная')
    )
    importance = models.CharField(max_length=1, choices=IMPORTANCE, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)




# Create your models here.
