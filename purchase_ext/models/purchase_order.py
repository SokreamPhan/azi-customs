# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    requester_id = fields.Many2one('res.users', 'Resquester',track_visibility='onchange')
    quotation_by = fields.Many2one('res.users', 'Find Quotation By')
    purchase_request_ref = fields.Char('Request Nº')
    project_name = fields.Char('Project Name')