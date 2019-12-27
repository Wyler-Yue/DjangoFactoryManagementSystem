from django.db import models
from django.forms import ModelForm

# Create your models here.
#车间
class ManufacturingShop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='车间名称', max_length=64)
    def __str__(self):
        return "%s"%( self.name)
    class Meta:
        verbose_name = '车间信息'
        verbose_name_plural = '车间信息'
#设备信息
class Equipment(models.Model):
    equipment_status = (
        (0, '正常'),
        (1, '故障'),
        (2, '备用'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='设备名称', max_length=64)
    specifications = models.CharField(verbose_name='规格型号', max_length=64)
    device_type = models.CharField(verbose_name='设备类型', max_length=128)
    status = models.SmallIntegerField(choices=equipment_status, default=0, verbose_name='设备状态')
    site = models.ForeignKey("ManufacturingShop", verbose_name='安装地点', max_length=64, on_delete=models.CASCADE)
    director = models.ForeignKey("Worker", verbose_name='设备管理人', max_length=64, on_delete=models.CASCADE)
    manufacturer = models.CharField(verbose_name='生产厂家', max_length=64)
    distributor = models.CharField(verbose_name='供应商', max_length=64)
    purchase_time = models.DateTimeField(verbose_name='购买时间')
    use_time = models.DateTimeField(verbose_name='启用时间')
    number = models.CharField(verbose_name='设备编号', max_length=64)
    parameter = models.TextField(verbose_name='设备参数')
    #picture = models.ImageField
    #handbook =

    def __str__(self):
        return "%s-%s-%s"%(self.name, self.specifications, self.number)
    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = '设备信息'
#巡检信息
class Inspection(models.Model):
    inspection_result_choice = (
        (0, '正常'),
        (1, '异常'),
    )
    inspection_status_choice = (
        (0, '正常运行'),
        (1, '停用'),
    )
    id = models.IntegerField(primary_key=True)
    time = models.DateTimeField(verbose_name='日期')
    name = models.ForeignKey("Equipment", verbose_name='巡检设备', on_delete=models.CASCADE)
    results = models.SmallIntegerField(choices=inspection_result_choice, default=0, verbose_name='结果')
    #picture =
    status = models.SmallIntegerField(choices=inspection_status_choice, default=0, verbose_name='设备状态')
    worker = models.ForeignKey("Worker", verbose_name='巡检人员', max_length=64, on_delete=models.CASCADE)
    def __str__(self):
        return "%s-%s"%(self.id, self.time)
    class Meta:
        verbose_name = '巡检信息'
        verbose_name_plural = '巡检信息'

#维修信息
class Maintain(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.DateTimeField(verbose_name='日期')
    name = models.ForeignKey("Equipment", verbose_name='维修设备', on_delete=models.CASCADE)
    results = models.TextField(verbose_name='维修工单')
    # picture =
    status = models.TextField(verbose_name='故障原因')
    worker = models.ForeignKey("Worker", verbose_name='维修人员', max_length=64, on_delete=models.CASCADE)
    def __str__(self):
        return "%s-%s" % (self.id, self.time)
    class Meta:
        verbose_name = '维修信息'
        verbose_name_plural = '维修信息'

#保养信息
class Upkeep(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.DateTimeField(verbose_name='日期')
    name = models.ForeignKey("Equipment", verbose_name='保养设备', on_delete=models.CASCADE)
    results = models.TextField(verbose_name='保养工单')
    # picture =
    status = models.TextField(verbose_name='保养内容')
    worker = models.ForeignKey("Worker", verbose_name='保养人员', max_length=64, on_delete=models.CASCADE)
    def __str__(self):
        return "%s-%s" % (self.id, self.time)
    class Meta:
        verbose_name = '保养信息'
        verbose_name_plural = '保养信息'
#工作人员
class Worker(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=64)
    number = models.CharField(verbose_name='人员编号', max_length=64)
    duty = models.CharField(verbose_name='职务', max_length=64)
    def __str__(self):
        return "%s-%s-%s" % (self.name, self.number, self.duty)
    class Meta:
        verbose_name = '工作人员信息'
        verbose_name_plural = '工作人员信息'


