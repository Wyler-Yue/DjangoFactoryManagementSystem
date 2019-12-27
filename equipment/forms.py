from django import forms
from .models import *

from django.core.exceptions import ValidationError
#车间信息
class ManufacturingShopModelForm(forms.ModelForm):
    class Meta:
        model = ManufacturingShop
        fields = "__all__"
        widges = {



        }
#设备信息
class EquipmentModelForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"
        widges = {

        }


#巡检信息
class InspectionModelForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = "__all__"
        labels = {
        }
        widgets = {  # 设置每个字段的插件信息
            "id": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "time": forms.widgets.DateInput(attrs={"type": "datetime"}),
        }
#维修信息
class MaintainModelForm(forms.ModelForm):
    class Meta:
        model = Maintain
        fields = "__all__"
        widgets = {

        }
#保养信息
class UpkeepModelForm(forms.ModelForm):
    class Meta:
        model = Upkeep
        fields = "__all__"
        widgets = {

        }
#人员信息
class WorkerModelForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
        widgets = {

        }