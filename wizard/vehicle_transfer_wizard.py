# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import ValidationError


class VehicleTransferWizard(models.TransientModel):
    _name = 'vehicle.transfer.wizard'
    _description = 'Vehicle Transfer Wizard'

    vehicle_id = fields.Many2one(
        comodel_name='fleet.vehicle.custom',
        string='Vehículo',
        required=True,
    )

    current_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contacto Actual',
        related='vehicle_id.partner_id',
        readonly=True,
    )

    new_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Nuevo Contacto',
        required=True,
    )

    reason = fields.Text(
        string='Motivo',
    )

    def action_transfer_vehicle(self):

        self.ensure_one()

        if self.vehicle_id.partner_id == self.new_partner_id:
            raise ValidationError(
                'El nuevo contacto debe ser diferente al actual.'
            )

        old_partner = self.vehicle_id.partner_id

        self.vehicle_id.partner_id = self.new_partner_id.id

        self.env['vehicle.transfer.history'].create({
            'vehicle_id': self.vehicle_id.id,
            'old_partner_id': old_partner.id,
            'new_partner_id': self.new_partner_id.id,
            'reason': self.reason,
        })

        return {
            'type': 'ir.actions.act_window_close',
        }