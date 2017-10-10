from django.db import models


class ResultRun(models.Model):
    run_time = models.DateTimeField(auto_now=True)
