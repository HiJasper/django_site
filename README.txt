I love python
I love web
So i think choose django maybe a good idea

You can find the example in :
	djangobook.py3k.cn/2.0/chapter02/

28/11/2014

This Tag(1.0):
	use django-admin.py startproject to create a Django project
	use python manage.py runserver to start the local server 
	After those two steps, you can check the web by http://127.0.0.1:8000/

Tag(1.1)
	Create hello web page

Tag(1.2)
	Create time web page
		('^time/$', current_datetime),

Tag(1.3)
	Create time/plus/(\d{1,2})/ page
		Notes: 
			1.The page will not be found if you use \d{1, 2},because the space between 1 and 2
			2.Use () to pass the parameters

Tag(1.4)
	Use template module
	Notes:
		1.Need change the value of TEMPLATE_DIRS in setting.py
		2.Use function get_template to get the template from the path of TEMPLATE_DIRS
Tag(1.5)
	render_to_response was used instead of get_template and HttpResponse
	Notes:
		You can use locals() instead of {'current_date':now},but the value of locals() also include the key-value about request

Tag(1.6)
	使用模版继承优化current_datetime.html和hours_ahead.html

Tag(2.0)
	模型：
		新建project: library 
		新建app: books

		1.数据库的配置：
			DATABASES = {
				'default': {
					'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
					'NAME': '/home/jasper/Desktop/django/django_site/library/mydata.db',
					'USER': '',                      # Not used with sqlite3.
					'PASSWORD': '',                  # Not used with sqlite3.
					'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
				'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
				}
			}
		2.use python manage.py startrapp books建立app
		3.在models.py中建立模型
		4.更改setting.py里面关于INSTALLED_APPS和MIDDLEWARE_CLASSES的部分
			MIDDLEWARE_CLASSES = (
				#'django.middleware.common.CommonMiddleware',
				#'django.contrib.sessions.middleware.SessionMiddleware',
				#'django.middleware.csrf.CsrfViewMiddleware',
				#'django.contrib.auth.middleware.AuthenticationMiddleware',
				#'django.contrib.messages.middleware.MessageMiddleware',
			)


			INSTALLED_APPS = (
				#'django.contrib.auth',
				#'django.contrib.contenttypes',
				#'django.contrib.sessions',
				#'django.contrib.sites',
				#'django.contrib.messages',
				#'django.contrib.staticfiles',
				"library.books",
			)
		5.python manage.py validate 验证模型有效性
		6.python manage.py sqlall books生成CREATE TABLE语句
		7.python manage.py syncdb 提交SQL语句到数据库
		8.可以通过shell交互导入数据
			>>> from books.models import Publisher
			>>> p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
			...     city='Berkeley', state_province='CA', country='U.S.A.',
			...     website='http://www.apress.com/')
			>>> p1.save()
			>>> p2 = Publisher.objects.create(name="O'Reilly",
			...     address='10 Fawcett St.', city='Cambridge',
			...     state_province='MA', country='U.S.A.',
			...     website='http://www.oreilly.com/')
			>>> publisher_list = Publisher.objects.all() #查询语句
			>>> publisher_list
		9.Publisher.objects.filter对数据筛选
		  Publisher.objects.get获取单个对象
		  Publisher.objects.order_by对数据排序
		  也可以用Publisher.objects.filter(country="U.S.A.").order_by("-name")进行连锁查询
		  数据的删除：
			  >>> p = Publisher.objects.get(name="O'Reilly")
			  >>> p.delete()
