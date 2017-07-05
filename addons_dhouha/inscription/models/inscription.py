# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Inscritpion(models.Model):   
    _name = 'inscription.inscription'
    
    @api.onchange('inscription_matiere_id')
    def _onchange_matiere_inscri(self):
        matiere_inscri_obj=self.env['matiere.matiere'] 
        for line in matiere_inscri_obj.search([('id','=',self.inscription_matiere_id.id)]):
            self.name_matiere =line.name_matiere
            self.coef_matiere =line.coef_matiere
    
       
    name =fields.Char('nom')
    prenom =fields.Char('prenom')
    date=fields.Date('date de naissance')
    genre=fields.Selection([('homme', 'homme'), ('femme', 'femme')], string='genre')
    details=fields.Text("details")
    ville =fields.Char('ville')
    rue =fields.Char('rue')
    gouv =fields.Char('gouv')
    bac =fields.Char('bac')
    note_matiere=fields.Float('Note')
    inscription_id=fields.Many2one('faculte.faculte','faculte')
    inscription_id2=fields.Many2one('faculte.faculte','faculte')
    inscription_id3= fields.Many2many('inscription.inscription','cles_rel','inscription_id3','faculte_id','etudiant_inscri')
    inscription_matiere_id= fields.One2many('matiere.matiere','matiere_id', 'matiere_inscri')
    inscription_result_id=fields.Many2one('resultat.resultat','Etudiant_resultat')
    
class Faculte(models.Model): 
    _name = 'faculte.faculte'
    
    
    name =fields.Char('nom')
    ville =fields.Char('ville')
    score=fields.Float('score')
    faculte_id=fields.One2many('inscription.inscription','inscription_id2','inscription')
 
    
class Moyenne(models.Model): 
    _name = 'moyenne.moyenne'
    
    @api.multi
    def get_nombre(self):
        elev_obj=self.env['inscription.inscription']
        nbr_elev=0
        for line in elev_obj.search([]):
            if line.id :
                nbr_elev=nbr_elev+1
        self.compt_elev=nbr_elev
        
    @api.onchange('id_moyenne')
    def _onchange_eleve(self):
        elev_obj=self.env['inscription.inscription'] 
        for line in elev_obj.search([('id','=',self.id_moyenne.id)]):
            self.name =line.name
            self.prenom =line.prenom
            self.date=line.date
            self.bac=line.bac
            
        
       
    @api.one
    def get_somme(self):
        somme=0
        math=self.mat1*self.coefmat
        physique=self.mat2*self.coefph
        informatique=self.mat3*self.coefinf
        somme=math+physique+informatique
        return somme
    
    @api.one
    def _get_moyenne(self):
        somme=self.get_somme()
        print somme
        moyenne=somme[0]/(self.coefmat+self.coefph+self.coefinf)
        self.moy=moyenne
        
    name =fields.Char('nom')
    prenom =fields.Char('prenom')
    date=fields.Date('date de naissance')
    bac=fields.Char('bac')
    mat1=fields.Float('math',required=True)
    mat2=fields.Float('physique',required=True)
    mat3=fields.Float('info',required=True)
    coefmat=fields.Float('coefficient',required=True,default=3)
    coefph=fields.Float('coefficient',required=True,default=2)
    coefinf=fields.Float('coefficient',required=True,default=1)
    moy=fields.Float('moyenne',compute='_get_moyenne',)
    compt_elev=fields.Integer('nombre etudiants',compute='get_nombre')
    id_moyenne=fields.Many2one('inscription.inscription','etudiant')

    
class Matiere(models.Model): 
    _name = 'matiere.matiere'
    
    
    name_matiere=fields.Char('nom')
    coef_matiere=fields.Float('coefficient',required=True)
#     matiere_id= fields.Many2many('matiere.matiere','cles_rel1','matiere_id','inscription_matiere_id','matiere_inscri')
    matiere_id=fields.Many2one('inscription.inscription','matiere_inscri')
    matiere_result_id=fields.Many2one('resultat.resultat','matiere_resultat')
    resultat=fields.Float('moyenne',compute='_get_resultat',)
    compt_matiere=fields.Integer('nombre de matieres',compute='get_nombre_mat')
    
    @api.multi
    def get_nombre_mat(self):
        matiere_obj=self.env['matiere.matiere']
        nbr_matiere=0
        for line in matiere_obj.search([]):
            if line.id :
                nbr_matiere=nbr_matiere+1
        self.compt_matiere=nbr_matiere
        

class Resultat(models.Model): 
    _name = 'resultat.resultat'
    
    result_etud_id=fields.One2many('inscription.inscription','inscription_result_id','Etudiant_resultat')
    result_matiere_id=fields.One2many('matiere.matiere','matiere_result_id','matiere_resultat')

     
    @api.onchange('result_etud_id')
    def _onchange_etudiant(self):
        elev_etudiant=self.env['inscription.inscription'] 
        for line in elev_etudiant.search([('id','=',self.result_etud_id.id)]):
            self.name =line.name
            self.prenom =line.prenom
            

    @api.onchange('result_matiere_id')
    def _onchange_matiere(self):
        matiere_obj=self.env['matiere.matiere'] 
        for line in matiere_obj.search([('id','=',self.result_matiere_id.id)]):
            self.name_matiere =line.name_matiere
            self.coef_matiere =line.coef_matiere
                
    

    
    
    

    
