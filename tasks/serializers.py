from rest_framework import serializers

from tasks.models import Task, Gallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("photo",)


class TaskSerializer(serializers.ModelSerializer):
    photos = GallerySerializer(many=True, read_only=True)

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

    def create(self, validated_data):
        photos_data = self.context.get("request").FILES.getlist("photos")
        user = self.context.get("request").user
        print("\n\n\n\n", user)
        task = Task.objects.create(user=user, **validated_data)

        for photo_data in photos_data:
            gallery = Gallery.objects.create(task=task, photo=photo_data)
            task.photos.add(gallery)

        return task

    def update(self, instance, validated_data):
        photos_data = self.context.get("request").FILES.getlist("photos")

        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.due_date = validated_data.get("due_date", instance.due_date)
        instance.priority = validated_data.get("priority", instance.priority)
        instance.is_completed = validated_data.get(
            "is_completed", instance.is_completed
        )

        instance.save()

        if len(photos_data) > 0:
            instance.photos.clear()
            for photo_data in photos_data:
                gallery = Gallery.objects.create(task=instance, photo=photo_data)
                instance.photos.add(gallery)

        return instance
