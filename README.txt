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
