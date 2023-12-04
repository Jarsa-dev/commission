
from odoo import api, fields, models

class ResCompany(models.Model):
    
    _inherit = "res.company"
    
    sales_goal = fields.Monetary(
        string='Sales Goal',
        store=True,
        help='Transactional sales goal',
    )
