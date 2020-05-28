from invoke import task
s
@task
def clean(c):
    c.run("find . -name '*.pyc' -delete")


@task
def local(c):
    print("Starting Server Local")
    c.run("find . -name '*.pyc' -delete")
    c.run("python manage.py")


