"""Implementation of the SocialMetaMixin class"""
import logging
from django.views.generic.base import ContextMixin

logg = logging.getLogger(__name__)


class SocialMetaMixin(ContextMixin):
    """Provide the values for social metadata.

    Views that have this mixin can have the following attributes (each
    attribute can be replaced by a get_*() method) :

     * meta_title: title of the page to display in social media link.
     * meta_description: short page description.
     * meta_image: URL relative to the root of the website to a descriptive
                   image.

    Properties not set will use the default from the project settings.
    To remove a property from a view, set it to empty.
    """
    CONTEXT_KEY_PREFIX = 'socialmeta_'
    CONTEXT_KEY_ENABLED = 'enabled'
    CONTEXT_KEY_TITLE = 'title'
    CONTEXT_KEY_DESCRIPTION = 'description'
    CONTEXT_KEY_IMAGE = 'image'
    CONTEXT_DEFAULT_PREFIX = 'default_'

    def get_meta_title(self):
        return self.meta_title or None

    def get_meta_description(self):
        return self.meta_description or None

    def get_meta_image(self):
        return self.meta_image or None

    def get_context_data(self, **kwargs):
        logg.debug('Injecting socialmeta data into context')
        context = super().get_context_data(**kwargs)
        title = self.get_meta_title()
        description = self.get_meta_description()
        image = self.get_meta_image()
        if title is not None:
            logg.debug('Injecting title')
            context[self.__class__.CONTEXT_KEY_PREFIX
                    + self.__class__.CONTEXT_KEY_TITLE] = title
        if description is not None:
            logg.debug('Injecting description')
            context[self.__class__.CONTEXT_KEY_PREFIX
                    + self.__class__.CONTEXT_KEY_DESCRIPTION] = description
        if image is not None:
            logg.debug('Injecting image')
            context[self.__class__.CONTEXT_KEY_PREFIX
                    + self.__class__.CONTEXT_KEY_IMAGE] = image
        return context
