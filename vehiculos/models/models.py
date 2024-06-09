# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vehiculos(models.Model):
    _name = 'vehiculos.vehiculos'
    _description = 'vehiculos.vehiculos'

    nombre = fields.Char()
    modelo = fields.Char()
    placa = fields.Char()
    chofer = fields.Char()
    anio = fields.Char()
