{% if cookiecutter.model_name %}from {{cookiecutter.package_name}} import models

import factory


class {{cookiecutter.model_name}}Factory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.{{cookiecutter.model_name}}{% endif %}
