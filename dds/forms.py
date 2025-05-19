from django import forms
from datetime import date
from .models import CashFlow, Category, Subcategory
from .models import Status, Type, Category, Subcategory

# Форма для создания и редактирования записей
class CashFlowForm(forms.ModelForm):
    date = forms.DateField(
        initial=date.today,
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Дата"
    )

    class Meta:
        model = CashFlow
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Пустые queryset по умолчанию
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        # Категории по типу
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)
            self.fields['category'].widget.attrs['data-selected'] = self.instance.category.id
        else:
            self.fields['category'].widget.attrs['data-selected'] = ''

        # Подкатегории по категории
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)
            self.fields['subcategory'].widget.attrs['data-selected'] = self.instance.subcategory.id
        else:
            self.fields['subcategory'].widget.attrs['data-selected'] = ''

    def clean(self):
        cleaned_data = super().clean()
        type_ = cleaned_data.get("type")
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")
        amount = cleaned_data.get("amount")

        if not type_:
            self.add_error("type", "Поле обязательно.")
        if not category:
            self.add_error("category", "Поле обязательно.")
        if not subcategory:
            self.add_error("subcategory", "Поле обязательно.")
        if amount is None:
            self.add_error("amount", "Поле обязательно.")

        if category and type_ and category.type != type_:
            self.add_error("category", "Категория не относится к выбранному типу.")
        if subcategory and category and subcategory.category != category:
            self.add_error("subcategory", "Подкатегория не относится к выбранной категории.")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].required = True
        self.fields['category'].required = True
        self.fields['subcategory'].required = True
        self.fields['amount'].required = True

        self.fields['type'].widget.attrs['required'] = True
        self.fields['category'].widget.attrs['required'] = True
        self.fields['subcategory'].widget.attrs['required'] = True
        self.fields['amount'].widget.attrs['required'] = True

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
