Minimal social linking META injector
====================================


Purpose
-------
This Django application ease the insertion of simple metadata in template responses.
It can output the following meta tags :

 * og:title
 * og:description
 * og:url
 * og:image
 * twitter:card

It should be enough for most websites to pick up minimal information about the link, and display something nice.


Setup and configuration
-----------------------
The meta tags are defined in a template file inside the project.
It is usually used with {% include %}.
This template file path is "socialmeta/head.html" and should be included in the head tag of the HTML output.

Configuration is done using django settings.
The application will look for settings.SOCIALMETA which should be a dictionary.
It can have the following properties :

 * enabled (mandatory): set to True to enable generation of meta tags
 * title (mandatory): a default value for the og:title meta
 * description (optional): a string used as default description
 * image (optional): an URI relative to the root of the website to serve as the default picture

These values are used by default in every view, and can be overriden by specific views.
If not provided, image will be the result of ```join(settings.STATIC_URL, 'img/socialmeta/base.png')```.

Finally, add "socialmeta.SocialMetaConfig" to the list of Django applications to load and add "socialmeta.context_processors.socialmeta" to your list of templates context processors.


Usage
-----
Unless specified otherwise, views will use the default values in settings to produce metadata.
To alter these values, use the socialmeta.mixins.SocialMetaMixin mixin on your view class.
It is then possible to define local versions of title, description and image.
