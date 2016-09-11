from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from beat.stud10 import stud10MessageFactory as _



class ITrabalho(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    descricao = schema.Text(
        title=_(u"Descricao"),
        required=False,
        description=_(u"Field description"),
    )
#
    ficha = schema.Text(
        title=_(u"Ficha tecnica"),
        required=False,
        description=_(u"Field description"),
    )
#
    resumida = schema.Text(
        title=_(u"Ficha tecnica resumida"),
        required=False,
        description=_(u"Field description"),
    )
#

    thumbnail = schema.Bytes(
        title=_(u"Imagem para thumbnail"),
        required=True,
        description=_(u"Selecione a imagem padrao"),
    )
#
    banner = schema.Bytes(
        title=_(u"Imagem para banner"),
        required=True,
        description=_(u"Selecione a imagem padrao"),
    )
#
    youtube = schema.TextLine(
        title=_(u"Codigo do Youtube"),
        required=True,
        description=_(u"Insira o codigo do video no youtube"),
    )
#
