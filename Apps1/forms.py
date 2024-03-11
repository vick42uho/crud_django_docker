from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname','Card','Mobile','gender')
        labels = {
            'fullname':'ชื่อ - นามสกุล',
            'Card':'เลขประจําตัวประชาชน',
            'Mobile':'เบอร์โทรศัพท์',
            'gender':'เพศ'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['Card'].required = False