import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from apps.portfolio_app.models import Post, Tag
from django.conf import settings
import random, datetime

#print(settings.EMAIL_HOST_USER)
#print(settings.EMAIL_PASSWORD)

def create_posts(posts_number):
    fake = Faker('en')
    Faker.seed(10)
    #tags_list =
    for _ in range(posts_number):
        headline = fake.sentence(nb_words=3, variable_nb_words=True)
        sub_headline = fake.sentence(nb_words=10, variable_nb_words=False)
        body = fake.paragraph(nb_sentences=20)
        active  = True
        featured = True
        #tags = random.choice(tags_list)
        a = Post(headline=headline,sub_headline=sub_headline, body=body , active=active, featured=featured)
        a.save()

create_posts(5)