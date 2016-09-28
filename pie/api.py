from tastypie.resources import ModelResource
from tastypie.constants import ALL

from pie.models import Pie

class PieResource(ModelResource):
	class Meta:
		queryset = Pie.objects.all()
		resource_name = 'pie'
		filtering = {'title': ALL}