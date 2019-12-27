from .models import Equipment, ManufacturingShop, Inspection, Maintain, Upkeep, Worker
from django.contrib import admin
#注册

class EquipmentInfo(admin.StackedInline):
    model = Equipment
    extra = 1

class ManufacturingShopAdmin(admin.ModelAdmin):
    inlines = [EquipmentInfo]

    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10
admin.site.register(ManufacturingShop,ManufacturingShopAdmin)

class EquipmentAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['id', 'name', 'specifications', 'device_type', 'status', 'site', 'director', 'manufacturer', 'distributor', 'purchase_time', 'use_time', 'number']
    list_filter = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10
admin.site.register(Equipment,EquipmentAdmin)


class InspectionAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['id', 'time', 'name', 'results', 'status', 'worker']
    list_filter = ['id', 'time']
    search_fields = ['time']
    list_per_page = 10
admin.site.register(Inspection, InspectionAdmin)

class MaintainAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['id', 'time', 'name', 'results', 'status', 'worker']
    list_filter = ['id', 'time']
    search_fields = ['time']
    list_per_page = 10
admin.site.register(Maintain, MaintainAdmin)


class UpkeepAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['id', 'time', 'name', 'results', 'status', 'worker']
    list_filter = ['id', 'time']
    search_fields = ['time']
    list_per_page = 10
admin.site.register(Upkeep, UpkeepAdmin)

class WorkerAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['id', 'number', 'name', 'duty']
    list_filter = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10
admin.site.register(Worker, WorkerAdmin)

admin.site.site_title = "设备管理"
admin.site.site_header = "设备管理"