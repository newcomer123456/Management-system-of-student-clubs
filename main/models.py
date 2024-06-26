from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    president = models.ForeignKey(Student, related_name='presided_clubs', on_delete=models.CASCADE)
    members = models.ManyToManyField(Student, related_name='member_clubs')

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    club = models.ForeignKey(Club, related_name='events', on_delete=models.CASCADE)
    participants = models.ManyToManyField(Student, related_name='attended_events')

    def __str__(self):
        return self.name

class EventAttendees(models.Model):
    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='event_attendances', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} attending {self.event}"






