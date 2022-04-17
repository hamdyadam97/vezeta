# Generated by Django 3.1.6 on 2021-08-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210724_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='type_of_person',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=50, verbose_name='نوع الدكتور'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('جلدية', 'جلدية'), ('اسنان', 'اسنان'), ('نفسى', 'نفسى'), ('اطفال حديثى الولادة', 'اطفال حديثى الولادة'), ('مخ واعصاب', 'مخ واعصا'), ('عظام', 'عظام'), ('نسا وتوليد', 'نسا وتوليد'), ('انف واذن وحنجرة', 'انف واذن وحنجرة'), ('قلب واوعية دموية', 'قلب واوعية دموية'), ('امراض دم', 'امراض دم'), ('اورام', 'ورام'), ('باطنة', 'باطنة'), ('تخسيس وتغذية', 'تخسيس وتغذية'), ('جراحة اطفال', 'جراحة اطفال'), ('جراحة اورام', "'جراحة اورام"), ('جراحة تجميل', 'جراحة تجمي'), (' جراحة اوعية دموية', 'جراحة اوعية دموية')], max_length=100, null=True, verbose_name='دكتور؟'),
        ),
    ]
