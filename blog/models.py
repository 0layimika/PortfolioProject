from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=230)
    pub_date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
# Create your models here.
