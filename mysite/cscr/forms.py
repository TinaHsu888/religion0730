from django import forms
class PublicationForm(forms.ModelForm):
	class Meta(object):
		model=Publication
		fields=[
		title,
		book_type,
		author]

		label={
			'title':'書名',
			'book_type'：'類型',
			'author':'作者'

		}
					
