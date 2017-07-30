from haystack import indexes
from cscr.models import Publication


class PublicationIndex(indexes.SearchIndex,indexes.Indexable):
	text=indexes.CharField(document=True,use_template=True)
	book_type=indexes.CharField(model_attr='book_type')
	author=indexes.CharField(model_attr='author')
	
	def get_model(self):
		return Publication

	def index_queryset(self,using=None):
		return self.get_model().objects.all()