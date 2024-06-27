import django_setup
from main.models import Student, Club, Event, EventAttendees

from datetime import datetime


def add_student():
    first_name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")
    email = input("Введіть email: ")

    if Student.objects.filter(email=email).exists():
        print("Студент з таким email вже існує.")
    else:
        student = Student(first_name=first_name, last_name=last_name, email=email)
        student.save()
        print("Студент успішно доданий.")

def add_club():
    name = input("Введіть назву клубу: ")
    description = input("Введіть опис клубу: ")
    president_id = input("Введіть ID президента: ")

    try:
        president = Student.objects.get(id=president_id)
        club = Club(name=name, description=description, president=president)
        club.save()
        print("Клуб успішно доданий.")
    except Student.DoesNotExist:
        print("Президент з таким ID не знайдений.")

def add_event():
    name = input("Введіть назву заходу: ")
    date_str = input("Введіть дату (YYYY-MM-DD): ")
    venue = input("Введіть місце проведення: ")
    club_name = input("Введіть назву клубу: ")

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        club = Club.objects.get(name=club_name)
        event = Event(name=name, date=date, venue=venue, club=club)
        event.save()
        print("Захід успішно доданий.")
    except Club.DoesNotExist:
        print("Клуб з такою назвою не знайдений.")
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат YYYY-MM-DD.")

def add_event_attendee():
    event_name = input("Введіть назву заходу: ")
    student_id = input("Введіть ID студента: ")

    try:
        event = Event.objects.get(name=event_name)
        student = Student.objects.get(id=student_id)
        attendee = EventAttendees(event=event, student=student)
        attendee.save()
        print("Учасник успішно доданий до заходу.")
    except Event.DoesNotExist:
        print("Захід з такою назвою не знайдений.")
    except Student.DoesNotExist:
        print("Студент з таким ID не знайдений.")

def delete_student():
    student_id = input("Введіть ID студента для видалення: ")
    try:
        student = Student.objects.get(id=student_id)
        student.delete()
        print("Студента успішно видалено.")
    except Student.DoesNotExist:
        print("Студент з таким ID не знайдений.")

def delete_club():
    club_id = input("Введіть ID клубу для видалення: ")
    try:
        club = Club.objects.get(id=club_id)
        club.delete()
        print("Клуб успішно видалено.")
    except Club.DoesNotExist:
        print("Клуб з таким ID не знайдений.")

def delete_event():
    event_id = input("Введіть ID заходу для видалення: ")
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
        print("Захід успішно видалено.")
    except Event.DoesNotExist:
        print("Захід з таким ID не знайдений.")

def delete_event_attendee():
    event_id = input("Введіть ID заходу: ")
    student_id = input("Введіть ID студента: ")
    try:
        attendee = EventAttendees.objects.get(event_id=event_id, student_id=student_id)
        attendee.delete()
        print("Учасника успішно видалено із заходу.")
    except EventAttendees.DoesNotExist:
        print("Учасник заходу з такими даними не знайдений.")

def list_students():
    students = Student.objects.all()
    for student in students:
        print(f"ID: {student.id}, Ім'я: {student.first_name}, Прізвище: {student.last_name}, Email: {student.email}")

def list_clubs():
    clubs = Club.objects.all()
    for club in clubs:
        print(f"ID: {club.id}, Назва: {club.name}, Опис: {club.description}, Президент ID: {club.president.id}")

def list_events():
    events = Event.objects.all()
    for event in events:
        print(f"ID: {event.id}, Назва: {event.name}, Дата: {event.date}, Місце проведення: {event.venue}, Клуб ID: {event.club.id}")

def list_event_attendees():
    attendees = EventAttendees.objects.all()
    for attendee in attendees:
        print(f"Захід ID: {attendee.event.id}, Студент ID: {attendee.student.id}")

def menu():
    while True:
        print("\nМеню:")
        print("1. Додати студента")
        print("2. Додати клуб")
        print("3. Додати захід")
        print("4. Додати учасника до заходу")
        print("5. Видалити студента")
        print("6. Видалити клуб")
        print("7. Видалити захід")
        print("8. Видалити учасника із заходу")
        print("9. Переглянути студентів")
        print("10. Переглянути клуби")
        print("11. Переглянути заходи")
        print("12. Переглянути учасників заходів")
        print("13. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_club()
        elif choice == '3':
            add_event()
        elif choice == '4':
            add_event_attendee()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            delete_club()
        elif choice == '7':
            delete_event()
        elif choice == '8':
            delete_event_attendee()
        elif choice == '9':
            list_students()
        elif choice == '10':
            list_clubs()
        elif choice == '11':
            list_events()
        elif choice == '12':
            list_event_attendees()
        elif choice == '13':
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    menu()