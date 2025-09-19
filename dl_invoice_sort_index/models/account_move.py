# models/account_move.py
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'
    _order = 'name_sort_index asc, id desc'

    name_sort_index = fields.Integer(string="Número (Ordem)", compute="_compute_name_sort_index", store=True)

    @api.depends('name')
    def _compute_name_sort_index(self):
        for move in self:
            try:
                # Extrai o número da fatura, mesmo com prefixos diferentes
                number_part = move.name.split('/')[-1]
                move.name_sort_index = int(number_part)
            except (ValueError, TypeError):
                move.name_sort_index = 0