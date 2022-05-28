from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Relationship, Tags


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_true = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            check_input = form.cleaned_data
            # print('result', check_input)
            if check_input == {}:
                raise ValidationError('Добавьте подходящие разделы')
            else:
                if check_input['main'] is True:
                    count_true += 1
        if count_true == 0:
            raise ValidationError('Укажите основной раздел')
        elif count_true > 1:
            raise ValidationError('Основным может быть только 1 раздел')

            # raise ValidationError('Добавьте подходящие разделы')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке

        return super().clean()  # вызываем базовый код переопределяемого метода



class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image', 'tags']
    list_display_links = ['title', 'tags']
    inlines = [RelationshipInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag',]
    inlines = [RelationshipInline]