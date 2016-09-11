# -*- coding: utf-8 -*-
"""Definition of the Trabalho content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from beat.stud10 import stud10MessageFactory as _

from beat.stud10.interfaces import ITrabalho
from beat.stud10.config import PROJECTNAME

TrabalhoSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-


    atapi.TextField(
        'descricao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Descricao"),
        ),
        default_output_type = 'text/html',
    ),

    atapi.TextField(
        'ficha',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Ficha tecnica"),
        ),
        default_output_type = 'text/html',
    ),

    atapi.TextField(
        'resumida',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Ficha tecnica resumida"),
        ),
        default_output_type = 'text/html',
    ),

    atapi.ImageField(
        'thumbnail',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Imagem para thumbnail"),
            description=_(u"Selecione a imagem no tamanho 270x150"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
        sizes={
           'thumbnail': (270, 150),
        },
    ),

    atapi.ImageField(
        'banner',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Imagem para banner"),
            description=_(u"Selecione a imagem no tamanho 1080x350px"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
        sizes={
           'banner': (1080, 350),
        },
    ),

    atapi.StringField(
        'youtube',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Codigo do Youtube"),
            description=_(u"Insira o codigo do video no youtube"),
        ),
        required=True,
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

TrabalhoSchema['title'].storage = atapi.AnnotationStorage()
TrabalhoSchema['description'].storage = atapi.AnnotationStorage()
TrabalhoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['subject'].schemata = 'default'
TrabalhoSchema['nextPreviousEnabled'].widget.visible = {"edit": "invisible", "view": "invisible"}
TrabalhoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(
    TrabalhoSchema,
    folderish=True,
    moveDiscussion=False
)


class Trabalho(folder.ATFolder):
    """ """
    implements(ITrabalho)

    meta_type = "Trabalho"
    schema = TrabalhoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    descricao = atapi.ATFieldProperty('descricao')
    ficha = atapi.ATFieldProperty('ficha')
    resumida = atapi.ATFieldProperty('resumida')
    thumbnail = atapi.ATFieldProperty('thumbnail')
    banner = atapi.ATFieldProperty('banner')
    youtube = atapi.ATFieldProperty('youtube')




atapi.registerType(Trabalho, PROJECTNAME)
