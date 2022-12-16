from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom widget to change add image styling
    to add/edit sport form.
    """

    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'sports/custom_widget_templates/custom_clearable_file_input.html'
        )
