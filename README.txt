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

Tag(3.0)
	The Django Admin Site：
		1.django.contrib 包的使用：
			django.contrib包是Django代码的基本组成部分,也是一套庞大的功能集,原码在/usr/lib/python2.7/dist-packages/django/contrib下
		2.功能集之一的admin的使用：
			1.首先需要将django.contrib.admin加入setting.py的INSTALLED_APPS（其实admin也是一个app,他也有视图模版等）
			2.同时在INSTALL_APP中添加'django.contrib.auth','django.contrib.contenttypes'和'django.contrib.sessions'
			  在MIDDLEWARE_CLASSES包含'django.middleware.common.CommonMiddleware','django.contrib.sessions.middleware.SessionMiddleware'
			  和'django.contrib.auth.middleware.AuthenticationMiddleware'
			3.通过python manage.py syncdb创建超级管理员账户
			4.完善url映射:
				from django.contrib import admin
				admin.autodiscover()

				# And include this URLpattern...
				urlpatterns = patterns('',
					# ...
					(r'^admin/', include(admin.site.urls)),
				)
			5.在books应用下建立admin.py(当服务启动时,Django从url.py引导URLconf,然后执行admin.autodiscover()语句.这个函数遍历INSTALLED_APPS配置,
			  并且寻找相关的 admin.py文件. 如果在指定的app目录下找到admin.py,它就执行其中的代码,至于Auth部分的加载则是因为 django.contrib.auth自带admin.py),内容如下：
				from django.contrib import admin
				from mysite.books.models import Publisher, Author, Book

				admin.site.register(Publisher)
				admin.site.register(Author)
				admin.site.register(Book)
			  加载models中的数据到admin中
			6.在models中,给类添加__unicode__方法,设定该类返回的格式,如：
				class Book(models.Model):
					title = models.CharField(max_length=100)
					authors = models.ManyToManyField(Author)
					publisher = models.ForeignKey(Publisher)
					publication_date = models.DateField()

					def __unicode__(self):
						return self.title
			7.设置可选片段:
				email = models.EmailField(blank=True)
				从原码中可以看到EmailFiled等的类都是继承class Field,父类中balnk默认是False
			8.设置别名：
				email = models.EmailField(blank=True, verbose_name='e-mail')
		3.自定义ModelAdmi类
			如：
			class BookAdmin(admin.ModelAdmin):
				list_display = ('title', 'publisher', 'publication_date')
				list_filter = ('publication_date',)
				date_hierarchy = 'publication_date'
				ordering = ('-publication_date',)
				fields = ('title', 'authors', 'publisher', 'publication_date')
				filter_horizontal = ('authors',)
				raw_id_fields = ('publisher',)
			admin.site.register(Book, BookAdmin)
			1.list_display优化显示格式
			2.list_filter过滤器
			3.date_hierarchy根据时间进行索引
			4.ordering排序（-表示降序）
			5.fields定义需要显示的部分,可以用它隐藏掉不想被别人更改的部分
			6.filter_horizontal JavaScript过滤器,允许检索选项,并且可以来回移动
			7.raw_id_fields 它是一个包含外键字段名称的元组,它包含的字段将被展现成文本框,而不再是下拉框,可以减少下拉框因为数据太多导致缓慢的问题
