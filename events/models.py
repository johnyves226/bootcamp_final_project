from django.db import models
from datetime import date,datetime
from django.core.files import File
import qrcode
from io import BytesIO
from PIL import Image,ImageDraw
from user.models import User

class Event(models.Model):
    name = models.CharField(max_length=200, null=False);
    description = models.TextField()
    qrcode = models.ImageField(upload_to='images/', blank=True);
    date = models.DateField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    is_active = models.BooleanField(default=False)



    def __str__(self):
        return  str(self.name)

    def save(self,*args,**kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas= Image.new('RGB',(290,290),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qrcode.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)
