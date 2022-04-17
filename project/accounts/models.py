from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.

TYPE_OF_PERSON = (
    ('M', "Male"),
    ('F', "Female")
)
DOCTOR_IN = (
    ('جلدية', "جلدية"),
    ('اسنان', "اسنان"),
    ('نفسى', "نفسى"),
    ('اطفال حديثى الولادة', "اطفال حديثى الولادة"),
    ('مخ واعصاب', "مخ واعصا"),
    ('عظام', "عظام"),
    ('نسا وتوليد', "نسا وتوليد"),
    ('انف واذن وحنجرة', "انف واذن وحنجرة"),
    ('قلب واوعية دموية', "قلب واوعية دموية"),
    ('امراض دم', "امراض دم"),
    ('اورام', "ورام"),
    ('باطنة', "باطنة"),
    ('تخسيس وتغذية', "تخسيس وتغذية"),
    ('جراحة اطفال', "جراحة اطفال"),
    ('جراحة اورام', "'جراحة اورام"),
    ('جراحة تجميل', "جراحة تجمي"),
    (' جراحة اوعية دموية', "جراحة اوعية دموية"),

)
class Profile(models.Model):

    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    name = models.CharField("الاسم", max_length=20)
    subtitle = models.TextField("نبذةعنك ", max_length=2000, blank=True, null=True)
    address = models.CharField("المحافظة ", max_length=100, blank=True, null=True )
    address_detail = models.CharField("العنوان بالتفصيل", max_length=100, blank=True, null=True)
    doctor = models.CharField("دكتور؟", max_length=100,choices=DOCTOR_IN, blank=True, null=True)
    specialist_doctor = models.CharField(" متخصص فى", max_length=100, blank=True, null=True)
    who_i = models.TextField("من انا", max_length=1000)
    price = models.IntegerField("سعر الكشف", blank=True, null=True)
    hour_of_work = models.IntegerField("عدد سعات العمل", blank=True, null=True)
    hour_of_wait = models.IntegerField("مدة الانتظار", blank=True, null=True)
    mobile = models.IntegerField("سعر المكالمة", blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    google = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField("الصورة الشخصية", upload_to="profile", null=True,blank=True)
    type_of_person = models.CharField('نوع الدكتور',choices=TYPE_OF_PERSON,max_length=50)
    slug = models.SlugField("slug", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return "%s" % self.user.username
        #return "%s %s" % (self.who_i, self.name)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Clinic(models.Model):
    namedoc = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image_of_clinic = models.ImageField("صور العيادة", upload_to="clinic", null=True,  blank=True)
    def __str__(self):
        return "%s" % self.namedoc