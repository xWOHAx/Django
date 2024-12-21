from django.db import models

class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    
    description = models.TextField(
        verbose_name="Описание"
    )
    
    image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "файл"
        verbose_name_plural = 'Настройки'  
   

    

class Banner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='banners/', 
        verbose_name="Изображение"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
 


