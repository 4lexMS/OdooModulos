from odoo import api, fields, models

class ModeloInc(models,Model):
    _name='mi.modelo'
    campo1=fields.Char()

    def metodo1(self):
    return self