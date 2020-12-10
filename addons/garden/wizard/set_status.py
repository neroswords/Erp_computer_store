# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class PlotSetStatus(models.TransientModel):
    _name = 'plot.set.status'
    _description = 'Set Plot Slot Color'

    line_ids = fields.One2many(
        comodel_name='plot.set.status.line',
        inverse_name='wiz_id',
        string='Slot'
    )
    plot_id = fields.Many2one(
        comodel_name='plot',
        string='Plot'
    )

    @api.model
    def default_get(self, fields):
        res = super(PlotSetStatus, self).default_get(fields)
        res_id = self._context.get('active_id')
        plot_id = self.env['plot'].browse(res_id)
        lines = []
        for slot in plot_id.slot_ids:
            lines.append(
                (0, 0, {
                    'slot_id': slot.id,
                     'is_yellow': slot.is_yellow,
                      'is_blue': slot.is_blue,
                }))
        res.update({
            'plot_id': res_id,
            'line_ids': lines
        })

        return res

    def confirm(self):
        for rec in self:
            for line in rec.line_ids:
                slot = line.slot_id
                if slot:
                    slot.write({
                        'is_yellow': line.is_yellow,
                        'is_blue': line.is_blue,
                    })
                partners = self.env['res.partner'].search([])
                gardener = partners.mapped('is_gardener')
                _logger.warning(gardener)


class PlotSetStatusLine(models.TransientModel):
    _name = 'plot.set.status.line'
    _description = 'Set Plot Slot Color'

    wiz_id = fields.Many2one(
        comodel_name='plot.set.status',
        string='Wizard'
    )
    slot_id = fields.Many2one(
        comodel_name='slot',
        string='Slot'
    )
    is_blue = fields.Boolean(
        string='Blue'
    )
    is_yellow = fields.Boolean(
        string='Yellow'
    )

    @api.onchange('slot_id')
    def _onchange_slot_id(self):
        for rec in self:
            slot = rec.slot_id
            rec.is_blue = slot.is_blue
            rec.is_yellow = slot.is_yellow