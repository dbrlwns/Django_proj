from django.db import models

# Create your models here.
class Log(models.Model):
    # "%(levelname)-4s %(asctime)s %(name)-5s %(message)s "
    level = models.CharField(max_length=20)
    logger_name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        date = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f'{self.logger_name} | {date} | {self.message}'