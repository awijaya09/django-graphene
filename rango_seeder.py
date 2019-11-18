import os 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                      'app.settings')

django.setup()

from core.models import Category, Page


def populate():
    python_pages = [
        {
            "title": "Data science with Python",
            "url": "https://halobro.com/1"
        },
        {
            "title": "Python for beginners",
            "url": "https://python.org"
        }

    ]

    cats = {"Python": {"pages": python_pages}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("{0} in {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


if __name__ == "__main__":
    print("Starts to give seed values")
    populate()