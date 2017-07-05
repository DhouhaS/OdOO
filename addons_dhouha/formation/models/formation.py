# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Formation(models.Model):   
    _name = 'formation.formation'
    
       
    name =fields.Char('Nom')
    age=fields.Integer("Age")
    moyenne=fields.Float('Moyenne')
    booleen=fields.Boolean('Booleen')
    statut = fields.Selection([('ouvrir', 'Nouveau'), ('confirmer', 'Valider')], string='Statut')
    remarque=fields.Text("Remarque")
    
    
# class FormationType(models.Model):   
#     _name = 'formation.type'
#     
#        
#     name =fields.Char('Nom')

