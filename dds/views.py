from django.shortcuts import render, redirect, get_object_or_404
from .models import CashFlow, Status, Type, Category, Subcategory
from .forms import CashFlowForm
from django.http import JsonResponse
from .forms import StatusForm, TypeForm, CategoryForm, SubcategoryForm

def index(request):
    records = CashFlow.objects.all()
    # Фильтрация
    filters = {
        "status": request.GET.get("status"),
        "type": request.GET.get("type"),
        "category": request.GET.get("category"),
        "subcategory": request.GET.get("subcategory"),
    }
    if request.GET.get("start") and request.GET.get("end"):
        records = records.filter(date__range=[request.GET.get("start"), request.GET.get("end")])
    for field, value in filters.items():
        if value:
            records = records.filter(**{f"{field}_id": value})

    context = {
        "records": records,
        "statuses": Status.objects.all(),
        "types": Type.objects.all(),
        "categories": Category.objects.all(),
        "subcategories": Subcategory.objects.all(),
    }
    return render(request, "dds/index.html", context)

# Создание новой записи
def create_record(request):
    if request.method == "POST":
        form = CashFlowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CashFlowForm()
    return render(request, "dds/form.html", {"form": form})


# Редактирование существующей записи
def edit_record(request, pk):
    record = get_object_or_404(CashFlow, pk=pk)
    if request.method == "POST":
        form = CashFlowForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CashFlowForm(instance=record)
    return render(request, "dds/form.html", {"form": form})

def delete_record(request, pk):
    record = get_object_or_404(CashFlow, pk=pk)
    record.delete()
    return redirect("index")

def get_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse({'categories': list(categories)})

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse({'subcategories': list(subcategories)})

# Страница управления справочниками
def dictionaries(request):
    # Обработка форм (POST)
    if request.method == "POST":
        if 'add_status' in request.POST:
            StatusForm(request.POST).save()
            return redirect("dictionaries")
        elif 'add_type' in request.POST:
            TypeForm(request.POST).save()
            return redirect("dictionaries")
        elif 'add_category' in request.POST:
            CategoryForm(request.POST).save()
            return redirect("dictionaries")
        elif 'add_subcategory' in request.POST:
            SubcategoryForm(request.POST).save()
            return redirect("dictionaries")

    context = {
        "statuses": Status.objects.all(),
        "types": Type.objects.all(),
        "categories": Category.objects.select_related("type"),
        "subcategories": Subcategory.objects.select_related("category"),
        "status_form": StatusForm(),
        "type_form": TypeForm(),
        "category_form": CategoryForm(),
        "subcategory_form": SubcategoryForm(),
    }
    return render(request, "dds/dictionaries.html", context)