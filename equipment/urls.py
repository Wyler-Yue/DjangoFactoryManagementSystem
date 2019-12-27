from django.urls import path, re_path
from . import views

urlpatterns = [
    #车间信息
    path('manufacturingshop/', views.shop),
    path('add_shop/', views.addshop),
    path('edit_shop/<int:manufacturingshop_id>/', views.editshop),
    path('delete_shop/<int:manufacturingshop_id>/', views.deleteshop),
    #设备信息
    path('equipment/', views.equipment),
    path('add_equipment/', views.addequipment),
    path('edit_equipment/<int:equipment_id>/', views.editequipment),
    path('delete_equipment/<int:equipment_id>/', views.deleteequipment),
    path('newqrcode/<int:equipment_id>/', views.newqrcode),
    #车间查看设备信息
    path('manufacturingshop/<num>/', views.shopequipment),
    #巡检信息
    path('inspection/', views.inspection),
    path('add_inspection/', views.addinspection),
    path('edit_inspection/<int:inspection_id>/', views.editinspection),
    path('delete_inspection/<int:inspection_id>/', views.deleteinspection),
    #维修信息
    path('maintain/', views.maintain),
    path('add_maintain/', views.addmaintain),
    path('edit_maintain/<int:maintain_id>/', views.editmaintain),
    path('delete_maintain/<int:maintain_id>/', views.deletemaintain),
    #保养信息
    path('upkeep/', views.upkeep),
    path('add_upkeep/', views.addupkeep),
    path('edit_upkeep/<int:upkeep_id>/', views.editupkeep),
    path('delete_upkeep/<int:upkeep_id>/', views.deleteupkeep),
    #员工信息
    path('worker/', views.worker),
    path('add_worker/', views.addworker),
    path('edit_worker/<int:worker_id>/', views.editworker),
    path('delete_worker/<int:worker_id>/', views.deleteworker),

    path('dashboard/', views.dashboard),
]