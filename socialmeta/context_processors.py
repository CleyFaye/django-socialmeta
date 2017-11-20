"""Implementation of the context processor for SocialMeta"""
import logging
from os.path import join
from django.conf import settings
from socialmeta.mixins import SocialMetaMixin

logg = logging.getLogger(__name__)


def socialmeta(request):
    """Inject the default socialmeta settings into the context.

    Default values are:
     - socialmeta.title: settings.SOCIALMETA['title']
     - socialmeta.description: settings.SOCIALMETA['description']
     - socialmeta.image: settings.SOCIALMETA['image']

    If settings.SOCIALMETA is not defined, or if settings.SOCIALMETA['enabled']
    is False, these elements are not added.
    """
    CONFIG_DICT_KEY = 'SOCIALMETA'
    CONFIG_ENABLED_KEY = 'enabled'
    CONFIG_TITLE_KEY = 'title'
    CONFIG_DESCRIPTION_KEY = 'description'
    CONFIG_IMAGE_KEY = 'image'

    DEFAULT_IMAGE_PATH = join(settings.STATIC_URL,
                              'img',
                              'socialmeta',
                              'base.png')

    logg.debug('Retrieving socialmeta configuration')
    socialmeta_settings = getattr(settings,
                                  CONFIG_DICT_KEY,
                                  None)

    enabled = (socialmeta_settings is not None
               and CONFIG_ENABLED_KEY in socialmeta_settings
               and socialmeta_settings[CONFIG_ENABLED_KEY])
    if not enabled:
        logg.debug('socialmeta disabled in configuration')
        return {
            (SocialMetaMixin.CONTEXT_KEY_PREFIX
             + SocialMetaMixin.CONTEXT_KEY_ENABLED): False
            }

    meta_title = socialmeta_settings[CONFIG_TITLE_KEY]
    logg.debug('socialmeta.title=%s', meta_title)
    if CONFIG_DESCRIPTION_KEY not in socialmeta_settings:
        logg.debug('socialmeta.description missing')
        meta_description = None
    else:
        meta_description = socialmeta_settings[CONFIG_DESCRIPTION_KEY]
    logg.debug('socialmeta.description=%s', meta_description)

    if CONFIG_IMAGE_KEY not in socialmeta_settings:
        meta_image = DEFAULT_IMAGE_PATH
        logg.debug('socialmeta.image missing')
    else:
        meta_image = socialmeta_settings[CONFIG_IMAGE_KEY]
    logg.debug('socialmeta.image=%s', meta_image)

    result = {
        SocialMetaMixin.CONTEXT_KEY_PREFIX
        + SocialMetaMixin.CONTEXT_KEY_ENABLED: enabled,

        SocialMetaMixin.CONTEXT_KEY_PREFIX
        + SocialMetaMixin.CONTEXT_DEFAULT_PREFIX
        + SocialMetaMixin.CONTEXT_KEY_TITLE: meta_title,

        SocialMetaMixin.CONTEXT_KEY_PREFIX
        + SocialMetaMixin.CONTEXT_DEFAULT_PREFIX
        + SocialMetaMixin.CONTEXT_KEY_DESCRIPTION: meta_description,

        SocialMetaMixin.CONTEXT_KEY_PREFIX
        + SocialMetaMixin.CONTEXT_DEFAULT_PREFIX
        + SocialMetaMixin.CONTEXT_KEY_IMAGE: meta_image
    }
    return result
