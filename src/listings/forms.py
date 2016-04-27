from django.forms import ModelForm
from django import forms
import itertools
from django.utils.text import slugify
from .models import Listing
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class ListingForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ListingForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit_survey'
    #     self.helper.add_input(Submit('submit', 'Submit'))

    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title'),
            Field('location'),
            Field('description'),
            Field('price'),
            Field('picture'),
            FormActions(Submit('submit', 'Submit', css_class="btn-success")),
            )

    class Meta:
        model = Listing
        exclude = ['user', 'pub_date', 'published']


