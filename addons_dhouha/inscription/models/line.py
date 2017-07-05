from odoo import api, fields, models, _


class Line(models.Model):   
    _inherit='sale.order.line'
    
    prix=fields.Integer('prix')