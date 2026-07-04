from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_image_alter_blog_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="author",
            field=models.CharField(max_length=200),
        ),
    ]
