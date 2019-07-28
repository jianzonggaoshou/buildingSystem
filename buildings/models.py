from django.db import models


# Create your models here.
class Buildings(models.Model):
    """
    Buildings
    """
    building_id = models.IntegerField(unique=True, verbose_name='楼房id')
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name='房屋名')
    households = models.IntegerField(null=True, blank=True, verbose_name='户数')
    location = models.CharField(max_length=128, null=True, blank=True, verbose_name='位置')
    image = models.ImageField(max_length=200, upload_to="images/buildings", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '{}'.format(self.name)


class Files(models.Model):
    """
    文件
    """
    file = models.FileField()

