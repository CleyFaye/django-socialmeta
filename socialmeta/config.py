"""socialmeta AppConfig"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    """Configuration for socialmeta application."""
    name = 'socialmeta'
    verbose_name = _('Inclusions automatiques de metadonnées pour lien social')
