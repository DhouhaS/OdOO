from odoo import api, fields, models, _


class Sale(models.Model):   
    _inherit='sale.order'
    
    prenom=fields.Char('prenom')
    
    nom_commande=fields.Char('nom_commande')
    
    timbre_fiscal=fields.Float('Timbre Fiscal',default=0.500)
    
    