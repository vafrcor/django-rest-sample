from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_datatables.pagination import DatatablesPageNumberPagination
import math

DEFAULT_PAGE=1


class CustomPagination(PageNumberPagination):

	# page = DEFAULT_PAGE
	# page_size_query_param = 'page_size'

	# @property
	# def paginator(self):
	# 	q_format= self.request.GET.get('format', None)
	# 	print ('q_format : {}'.format(q_format))
	# 	# return super(CustomPagination, self).paginator()
	# 	if q_format is not None and q_format == 'datatables':
	# 		return super(CustomPagination, self).paginator()
	# 	else:
	# 		if not hasattr(self, '_paginator'):
	# 			if self.pagination_class is None:
	# 				self._paginator = None
	# 			else:
	# 				self._paginator = self.pagination_class()
	# 		return self._paginator

	# # def paginate_queryset(self, queryset):
	# def paginate_queryset(self, queryset, request, view=None):
	# 	# return super(CustomPagination, self).paginate_queryset(queryset, self.request, view=self)
	# 	return DatatablesPageNumberPagination.paginate_queryset(queryset, self.request, view=view)

		# q_format= self.request.GET.get('format', None)
		# raise('XYZ', self.request.GET)
		# # print ('q_format : {}'.format(q_format))
		# if q_format is not None and q_format == 'datatables':
		# 	return super(CustomPagination, self).paginate_queryset(queryset, self.request, view=self)
		# else:
		# 	if self.paginator is None:
		# 		return None
		# 	return self.paginator.paginate_queryset(queryset, self.request, view=self)

	# def get_paginated_response(self, data):
	# 	q_format= self.request.GET.get('format', None)
	# 	print ('q_format : {}'.format(q_format))
	# 	if q_format is not None and q_format == 'datatables':
	# 		return super(CustomPagination, self).get_paginated_response(data)
	# 	else:
	# 		total = self.paginator.page.paginator.count
	# 		pagesize = int(self.request.GET.get('page_size', self.page_size))
	# 		totalpage = math.ceil(total / pagesize)

	# 		return Response({
	# 			'links': {
	# 				'next': self.paginator.get_next_link(),
	# 				'previous': self.paginator.get_previous_link()
	# 			},
	# 			'total': total,
	# 			'total_page': totalpage,
	# 			'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
	# 			'page_size': pagesize,
	# 			'results': data
	# 		})
