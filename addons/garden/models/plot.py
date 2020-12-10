# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Plot(models.Model):
    _name = 'plot'
    _description = 'Garden Plot'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
    ]

    name = fields.Char(
        string='Plot Name',
        required=True,
    )
    plot_type = fields.Char(
        string='Type',
        required=True,
    )
    gardener_ids = fields.Many2many(
        comodel_name='gardener',
        relation='gardener_plot_rel',
        string='Gardener',
    )
    slot_ids = fields.One2many(
        comodel_name='slot',
        inverse_name='plot_id',
        string='Slot',
    )
    slot_size = fields.Integer(
        string='Slot Size',
        track_visibility='onchange',
    )
    use_slot_count = fields.Integer(
        string='Used Slot',
        compute='_compute_slot'
    )
    avail_slot_count = fields.Integer(
        string='Available Slot',
        compute='_compute_slot',
        inverse='_set_slot',
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('process', 'Process'),
        ],
        default='draft',
    )

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The plot name must be unique"),
    ]

    @api.constrains('name')
    def _check_verbal_case(self):
        for rec in self:
            plot_name = rec.name
            if plot_name:
                if plot_name[0] in ('A', 'E', 'I', 'O', 'U'):
                    raise ValidationError(
                        "Plot name cannot start with verbal."
                    )

    @api.depends('slot_ids')
    def _compute_slot(self):
        for rec in self:
            if rec.slot_ids:
                rec.use_slot_count = len(rec.slot_ids)
                rec.avail_slot_count = rec.slot_size - len(rec.slot_ids)
            else:
                rec.use_slot_count = 0
                rec.avail_slot_count = rec.slot_size

    def process(self):
        for rec in self:
            rec.state = 'process'

    def set_status(self):
        for rec in self:
            return {
                        'name': 'Set Status',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'plot.set.status',
                        'view_id': self.env.ref(
                            'garden.plot_set_status_wizard_form').id,
                        'type': 'ir.actions.act_window',
                        'target': 'new',
                    }

    def _set_slot(self):
        for rec in self:
            rec.slot_size = rec.avail_slot_count + rec.use_slot_count
