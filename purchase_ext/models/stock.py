
# -*- coding: utf-8 -*-

from openerp import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    project_name = fields.Char('Project Name')
    requester_id = fields.Many2one('res.users', 'Requester')