from django import forms
from multiupload.fields import MultiFileField

from tasks.models import Task, Gallery


class TaskCreationForm(forms.ModelForm):
    photos = MultiFileField(min_num=0, max_num=3)

    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "photos",
            "due_date",
            "priority",
            "is_completed",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Enter the title", "class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Enter the description", "class": "form-control"}
            ),
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "priority": forms.Select(
                attrs={"placeholder": "Select the priority", "class": "form-control"}
            ),
            "is_completed": forms.CheckboxInput(
                attrs={
                    "placeholder": "Is the task completed?",
                    "class": "form-check-input",
                }
            ),
        }

    def save(self, commit=True):
        task = Task(**self.cleaned_data)
        task.save(commit=False)

        for photo in self.cleaned_data.get("photos"):
            gallery = Gallery(photo=photo)
            gallery.save()
            task.photos.add(gallery)

        if commit:
            task.save()

        return task


class TaskUpdateForm(forms.ModelForm):
    photos = MultiFileField(min_num=0, max_num=3, max_file_size=1024 * 1024 * 5)

    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "photos",
            "due_date",
            "priority",
            "is_completed",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Enter the title", "class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Enter the description", "class": "form-control"}
            ),
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "priority": forms.Select(
                attrs={"placeholder": "Select the priority", "class": "form-control"}
            ),
            "is_completed": forms.CheckboxInput(
                attrs={
                    "placeholder": "Is the task completed?",
                    "class": "form-check-input",
                }
            ),
        }

    def save(self, commit=True):
        task = Task(**self.cleaned_data)
        task.save(commit=False)

        for photo in self.cleaned_data.get("photos"):
            gallery = Gallery(photo=photo)
            gallery.save()
            task.photos.add(gallery)

        if commit:
            task.save()

        return task
