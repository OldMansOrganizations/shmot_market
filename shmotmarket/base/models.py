from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Categories(models.Model):
	id_category = models.AutoField(primary_key=True)
	name_category = models.CharField(max_length=45, verbose_name='Имя категории')
	category_slag = models.CharField(max_length=50, verbose_name='Имя категории для ссылки')
	photo_categories = models.ImageField(upload_to='images/categories/')
	
	class Meta:
		app_label = 'base'
		verbose_name = "Категорию"
		verbose_name_plural = "Категории"
		db_table = 'categories'
	
	def __str__(self):
		return self.name_category


class SubCategories(models.Model):
	id_subcategory = models.AutoField(primary_key=True)
	name_subcategory = models.CharField(max_length=45, verbose_name='Имя допкатегории')
	subcategory_slag = models.CharField(max_length=50, verbose_name='Имя допкатегории для ссылки')
	photo_subcategories = models.ImageField(upload_to='images/subcategories/')
	
	class Meta:
		app_label = 'base'
		verbose_name = "Подкатегорию"
		verbose_name_plural = "Подкатегории"
		db_table = 'subcategories'
	
	def __str__(self):
		return self.name_subcategory


class Products(models.Model):
	name_product = models.CharField(max_length=45, verbose_name='Название продукта')
	gram = models.PositiveSmallIntegerField(verbose_name='Количество грамм')
	description = models.TextField(verbose_name='Описание')
	id_category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
	id_subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE, verbose_name='Подкатегория')
	price = models.FloatField(verbose_name='Цена')
	discount = models.DecimalField(verbose_name='Скидка', decimal_places=1, max_digits=1, default=0.0)
	balance = models.PositiveSmallIntegerField(verbose_name='Количество продуктов на складе')
	product_slag = models.CharField(verbose_name='Имя товара для ссылки', max_length=50)
	company_name = models.CharField(max_length=45, verbose_name='Компания производитель')
	country_name = models.CharField(max_length=45, verbose_name='Страна производитель')
	photo_product = models.ImageField(upload_to='images/products/')
	
	class Meta:
		app_label = 'base'
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"
		db_table = 'products'
	
	def __str__(self):
		return self.name_product
	