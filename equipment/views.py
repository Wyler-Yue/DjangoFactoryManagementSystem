from django.shortcuts import render, redirect
from . import models
from . import forms
from .forms import EquipmentModelForm, InspectionModelForm, MaintainModelForm, UpkeepModelForm, WorkerModelForm, ManufacturingShopModelForm
from .models import ManufacturingShop, Equipment, Inspection, Upkeep, Maintain, Worker
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import qrcode
from django.utils.six import BytesIO
from django.http import HttpResponse
#车间信息
def shop(request):
    #模板取数据
    ManufacturingShopList = ManufacturingShop.objects.all()
    #数据传递给模板，模板渲染页面，渲染好页面传递给浏览器
    return render(request, 'Equipment/shop/ManufacturingShop.html', {"manufacturingshops": ManufacturingShopList})
#增加车间信息
def addshop(request):
    shop_form = ManufacturingShopModelForm
    if request.method == 'POST':
        shop_form = ManufacturingShopModelForm(request.POST)
        if shop_form.is_valid():
            shop_form.save()
            message = '添加成功！'
            return redirect('/manufacturingshop/')
        else:
            return render(request, 'Equipment/shop/add_shop.html', locals())
    shop_form = forms.ManufacturingShopModelForm()
    return render(request, 'Equipment/shop/add_shop.html', locals())
#修改车间信息
def editshop(request, manufacturingshop_id):
    edit_shop = models.ManufacturingShop.objects.get(pk=manufacturingshop_id)
    shop_from = ManufacturingShopModelForm(instance=edit_shop)
    if request.method == 'POST':
        shop_from = ManufacturingShopModelForm(request.POST, instance=edit_shop)
        if shop_from.is_valid():
            shop_from.save()
            return redirect('/manufacturingshop/')
        else:
            return render(request, 'Equipment/shop/edit_shop.html', locals())
    shop_form = forms.ManufacturingShopModelForm(instance=edit_shop)
    return render(request, 'Equipment/shop/edit_shop.html', locals())
#删除车间信息
def deleteshop(request, manufacturingshop_id):
    delete_shop = models.ManufacturingShop.objects.get(id=manufacturingshop_id)
    shop_from = ManufacturingShopModelForm(instance=delete_shop)
    if request.method == 'POST':
        ManufacturingShop.objects.filter(id=manufacturingshop_id).first().delete()
        return redirect('/manufacturingshop/')
    return render(request, 'Equipment/shop/delete_shop.html', locals())

#设备信息
def equipment(request):
    EquipmentList = Equipment.objects.all()
    return render(request, 'Equipment/equipment/Equipment.html', {"equipments": EquipmentList})
#增加设备信息
def addequipment(request):
    equipment_form = EquipmentModelForm
    if request.method == 'POST':
        equipment_form = EquipmentModelForm(request.POST)
        if equipment_form.is_valid():
            equipment_form.save()
            return redirect('/equipment/')
        else:
            return render(request, 'Equipment/equipment/add_equipment.html', locals())
    equipment_form = forms.EquipmentModelForm()
    return render(request, 'Equipment/equipment/add_equipment.html', locals())
#修改设备信息
def editequipment(request, equipment_id):
    edit_equipment = models.Equipment.objects.get(pk=equipment_id)
    equipment_from = EquipmentModelForm(instance=edit_equipment)
    if request.method == 'POST':
        equipment_from = EquipmentModelForm(request.POST, instance=edit_equipment)
        if equipment_from.is_valid():
            equipment_from.save()
            return redirect('/equipment/')
        else:
            return render(request, 'Equipment/equipment/edit_equipment.html', locals())
    equipment_form = forms.EquipmentModelForm(instance=edit_equipment)
    return render(request, 'Equipment/equipment/edit_equipment.html', locals())
#删除设备信息
def deleteequipment(request, equipment_id):
    delete_equipment = models.Equipment.objects.get(pk=equipment_id)
    equipment_from = EquipmentModelForm(instance=delete_equipment)
    if request.method == 'POST':
        Equipment.objects.filter(pk=equipment_id).first().delete()
        return redirect('/equipment/')
    return render(request, 'Equipment/equipment/delete_equipment.html', locals())



def newqrcode(request, equipment_id):
    information = models.Equipment.objects.get(id=equipment_id)
    i = qrcode.make(information)
    buf = BytesIO()
    i.save(buf)
    image_stream = buf.getvalue()
    response = HttpResponse(image_stream, content_type='image/png')
    return response



#车间与设备关联
def shopequipment(request, num):
    manufacturingshop = ManufacturingShop.objects.get(pk=num)
    EquipmentList = manufacturingshop.equipment_set.all()
    return render(request, 'Equipment/equipment/Equipment.html', {"equipments": EquipmentList})

#巡检信息
def inspection(request):
    inspectionList = Inspection.objects.all()
    return render(request, 'Equipment/inspection/inspection.html', {"inspections": inspectionList})
#增加巡检信息
def addinspection(request):
    inspection_form = InspectionModelForm
    if request.method == 'POST':
        inspection_form = InspectionModelForm(request.POST)
        if inspection_form.is_valid():
            inspection_form.save()
            return redirect('/inspection/')
        else:
            return render(request, 'Equipment/inspection/new_inspection.html', locals())
    inspection_form = forms.InspectionModelForm()
    return render(request, 'Equipment/inspection/new_inspection.html', locals())
#修改巡检信息
def editinspection(request, inspection_id):
    edit_inspection = models.Inspection.objects.get(pk=inspection_id)
    inspection_from = InspectionModelForm(instance=edit_inspection)
    if request.method == 'POST':
        inspection_from = InspectionModelForm(request.POST, instance=edit_inspection)
        if inspection_from.is_valid():
            inspection_from.save()
            return redirect('/inspection/')
        else:
            return render(request, 'Equipment/inspection/edit_inspection.html', locals())
    inspection_form = forms.InspectionModelForm(instance=edit_inspection)
    return render(request, 'Equipment/inspection/edit_inspection.html', locals())
#删除巡检信息
def deleteinspection(request, inspection_id):
    delete_inspection = models.Inspection.objects.get(id=inspection_id)
    inspection_from = InspectionModelForm(instance=delete_inspection)
    if request.method == 'POST':
        Inspection.objects.filter(id=inspection_id).first().delete()
        return redirect('/inspection/')
    return render(request, 'Equipment/inspection/delete_inspection.html', locals())

#维修信息
def maintain(request):
    maintainList = Maintain.objects.all()
    return render(request, 'Equipment/maintain/maintain.html', {"maintains": maintainList})
#增加维修信息
def addmaintain(request):
    maintain_form = MaintainModelForm
    if request.method == 'POST':
        maintain_form = MaintainModelForm(request.POST)
        if maintain_form.is_valid():
            maintain_form.save()
            return redirect('/maintain/')
        else:
            return render(request, 'Equipment/maintain/add_maintain.html', locals())
    maintain_form = forms.MaintainModelForm()
    return render(request, 'Equipment/maintain/add_maintain.html', locals())
#修改维修信息
def editmaintain(request, maintain_id):
    edit_maintain = models.Maintain.objects.get(pk=maintain_id)
    maintain_from = MaintainModelForm(instance=edit_maintain)
    if request.method == 'POST':
        maintain_from = MaintainModelForm(request.POST, instance=edit_maintain)
        if maintain_from.is_valid():
            maintain_from.save()
            return redirect('/maintain/')
        else:
            return render(request, 'Equipment/maintain/edit_maintain.html', locals())
    maintain_form = forms.MaintainModelForm(instance=edit_maintain)
    return render(request, 'Equipment/maintain/edit_maintain.html', locals())
#删除维修信息
def deletemaintain(request, maintain_id):
    delete_maintain = models.Maintain.objects.get(id=maintain_id)
    maintain_from = MaintainModelForm(instance=delete_maintain)
    if request.method == 'POST':
        Maintain.objects.filter(id=maintain_id).first().delete()
        return redirect('/maintain/')
    return render(request, 'Equipment/maintain/delete_maintain.html', locals())


#保养信息
def upkeep(request):
    upkeepList = Upkeep.objects.all()
    return render(request, 'Equipment/upkeep/upkeep.html', {"upkeeps": upkeepList})
#增加保养信息
def addupkeep(request):
    upkeep_form = UpkeepModelForm
    if request.method == 'POST':
        upkeep_form = UpkeepModelForm(request.POST)
        if upkeep_form.is_valid():
            upkeep_form.save()
            return redirect('/upkeep/')
        else:
            return render(request, 'Equipment/upkeep/add_upkeep.html', locals())
    upkeep_form = forms.UpkeepModelForm()
    return render(request, 'Equipment/upkeep/add_upkeep.html', locals())
#修改保养信息
def editupkeep(request, upkeep_id):
    edit_upkeep = models.Upkeep.objects.get(pk=upkeep_id)
    upkeep_from = UpkeepModelForm(instance=edit_upkeep)
    if request.method == 'POST':
        upkeep_from = UpkeepModelForm(request.POST, instance=edit_upkeep)
        if upkeep_from.is_valid():
            upkeep_from.save()
            return redirect('/upkeep/')
        else:
            return render(request, 'Equipment/upkeep/edit_upkeep.html', locals())
    upkeep_form = forms.UpkeepModelForm(instance=edit_upkeep)
    return render(request, 'Equipment/upkeep/edit_upkeep.html', locals())
#删除保养信息
def deleteupkeep(request, upkeep_id):
    delete_upkeep = models.Upkeep.objects.get(id=upkeep_id)
    upkeep_from = UpkeepModelForm(instance=delete_upkeep)
    if request.method == 'POST':
        Upkeep.objects.filter(id=upkeep_id).first().delete()
        return redirect('/upkeep/')
    return render(request, 'Equipment/upkeep/delete_upkeep.html', locals())

#人员信息
def worker(request):
    workerList = Worker.objects.all()
    return render(request, 'Equipment/worker/worker.html', {"workers": workerList})
#增加人员信息
def addworker(request):
    worker_form = WorkerModelForm
    if request.method == 'POST':
        worker_form = WorkerModelForm(request.POST)
        if worker_form.is_valid():
            worker_form.save()
            return redirect('/worker/')
        else:
            return render(request, 'Equipment/worker/add_worker.html', locals())
    worker_form = forms.WorkerModelForm()
    return render(request, 'Equipment/worker/add_worker.html', locals())
#修改人员信息
def editworker(request, worker_id):
    edit_worker = models.Worker.objects.get(pk=worker_id)
    worker_from = WorkerModelForm(instance=edit_worker)
    if request.method == 'POST':
        worker_from = WorkerModelForm(request.POST, instance=edit_worker)
        if worker_from.is_valid():
            worker_from.save()
            return redirect('/worker/')
        else:
            return render(request, 'Equipment/worker/edit_worker.html', locals())
    worker_form = forms.WorkerModelForm(instance=edit_worker)
    return render(request, 'Equipment/worker/edit_worker.html', locals())
#删除人员信息
def deleteworker(request, worker_id):
    delete_worker = models.Worker.objects.get(id=worker_id)
    worker_from = WorkerModelForm(instance=delete_worker)
    if request.method == 'POST':
        Worker.objects.filter(id=worker_id).first().delete()
        return redirect('/worker/')
    return render(request, 'Equipment/worker/delete_worker.html', locals())

#仪表盘
def dashboard(request):
    total = models.Equipment.objects.count()
    upline = models.Equipment.objects.filter(status=0).count()
    breakdown = models.Equipment.objects.filter(status=1).count()
    backup = models.Equipment.objects.filter(status=2).count()
    up_rate = round(upline/total*100)
    bd_rate = round(breakdown/total*100)
    bu_rate = round(backup/total*100)
    return render(request, 'Equipment/dashboard.html', locals())