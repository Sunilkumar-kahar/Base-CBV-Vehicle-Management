from .permission_config import PERMISSION_CONFIG
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def assign_permissions(user, role):
    models_permisions = PERMISSION_CONFIG.get(role, {})
    for model, permissions in models_permisions.items():
        content_type = ContentType.objects.get_for_model(model)
        for permission in permissions:
            perm_codename = f"{permission}_{model._meta.model_name}"
            django_prem = Permission.objects.get(content_type = content_type, codename = perm_codename)
            user.user_permissions.add(django_prem)