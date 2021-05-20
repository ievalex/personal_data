from django.db import models
from apscheduler.schedulers.background import BackgroundScheduler #для запуска задач по расписанию
from django.db import connection #для прямого обращения к БД - удаления записей
from rest_framework import routers, serializers, viewsets #для сериализации - для API
from django.core.validators import MinLengthValidator #для ограничения минимальной длины полей

class RequesterData(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=120)
    birth_date = models.DateField()
    passport_no = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    phone_no = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    check_date = models.DateField()
    
class CandidateData(models.Model):
    id = models.IntegerField(primary_key = True, serialize = True)
    name = models.CharField(max_length=120)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    passport_no = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    phone_no = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    education_info = models.CharField(max_length=60)
    health_info = models.CharField(max_length=60)
    check_date = models.DateField()
    
class IndividualBusinessman(models.Model):
    id = models.IntegerField(primary_key = True, serialize = True)
    name = models.CharField(max_length=120)
    birth_date = models.DateField()
    phone_no = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    individual_no = models.CharField(max_length=12)
    bank_account = models.CharField(max_length=12)
    health_info = models.CharField(max_length=60)
    contract_date = models.DateField()


#Код для запуска задач по разписанию
#Расположен именно тут, поскольку должен выполняться при запуске приложения (сайта)
#Таким образом, при каждом старте сайта автоматом начинают выполняться задания
from django.db import connection

sqllite_scheduler = BackgroundScheduler()
job = None

# Формируем команду на удаление заявителей
def delete_requesters():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM app_requesterdata WHERE check_date < datetime('now','-30 day')")
    print('Старые записи заявителей удалены.')

# Формируем команду на удаление кандидатов
def delete_candidates():
    with connection.cursor() as cursor: #заменить на 
        cursor.execute("DELETE FROM app_candidatedata WHERE check_date < datetime('now','-30 day')")
    print('Старые записи кандидатов удалены.')

# Формируем команду на удаление индивидуальных предпринимателей
def delete_individual():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM app_individualbusinessman WHERE contract_date < datetime('now','-30 day')")
    print('Старые записи индивидуальных предпринимателей удалены.')
 
# Запуск задач по расписанию
def start_job():
    global job
    #добавляем задачи в очередь, с указанием интервала для выполнения
    job = sqllite_scheduler.add_job(delete_requesters, 'interval', seconds=60)
    job = sqllite_scheduler.add_job(delete_candidates, 'interval', seconds=60)
    job = sqllite_scheduler.add_job(delete_individual, 'interval', seconds=60)
    try:
        #запускаем выполнение задач
        sqllite_scheduler.start()
    except:
        pass

# Непосредственно запускаем задачи
start_job()
