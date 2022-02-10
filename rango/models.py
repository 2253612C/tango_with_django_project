from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=128,unique=True)
    views=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    slug=models.SlugField(unique=True) #ensure same slug cant be used twice using unique

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        
        return cleaned_data



