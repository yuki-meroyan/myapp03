from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Menu, Material, Stock

class ModelFormWithFormSetMixin:

    def __init__(self, *args, **kwargs):
        super(ModelFormWithFormSetMixin, self).__init__(*args, **kwargs)
        self.formset = self.formset_class(
            instance=self.instance,
            data=self.data if self.is_bound else None,
        )

    def is_valid(self):
        return super(ModelFormWithFormSetMixin, self).is_valid() and self.formset.is_valid()

    def save(self, commit=True):
        saved_instance = super(ModelFormWithFormSetMixin, self).save(commit)
        self.formset.save(commit)
        return saved_instance

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ('name', 'amount', 'unit')

MaterialFormSet = forms.inlineformset_factory(
    parent_model = Menu,
    model        = Material,
    fields = '__all__',
    extra  = 5,
    form   = MaterialForm
)

class MenuForm(ModelFormWithFormSetMixin, ModelForm):
    formset_class = MaterialFormSet
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Menu
        fields = ('menu_name','menu_number',)