# IPython log file

get_ipython().magic('logstart sql')
from blog.models import Category, Label, Article
from myblog.models import Category, Label, Article
c= Category(name='category test')
c.save()
t=Label(name='label test')
t.save()
get_ipython().magic('logoff ')
help
help(log)
get_ipython().magic('logstart sql append')
from myblog.models import Category, Label, Article
from django.utils import timezone
from django.contrib.auth.models import User
user = User.objects.get(username='Huilin')
c = Category.objects.get(name='category test')
a = Article(title='title test', article_text='test', created_time=timezone.now(), modified_time=timezone.now(), category=c, author=user)
p.save()
a.save()
l=Label.objects.get(name='label test')
a = Article(title='title test', article_text='test', created_time=timezone.now(), modified_time=timezone.now(), category=c, author=user, label=l)
a.save()
Category.objects.all()
get_ipython().magic('logoff ')
