from django.db import models

# Create your models here.
class Post(models.Model):
    # 파이썬이 아닌 sql에 저장하므로 길이제한을 주어야한다.
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 100)

