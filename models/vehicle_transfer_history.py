# -*- coding: utf-8 -*-

from odoo import fields, models

class VehicleTransferHistory(models.Model):
    """Modelo para registrar el historial de transferencias de vehículos.
    
    Este modelo mantiene un registro detallado de cada transferencia de vehículos
    de un contacto a otro, incluyendo fechas, motivos y usuario que realizó la transferencia.
    Esto permite auditar y rastrear los cambios de propietario de cada vehículo.
    
    Atributos:
        vehicle_id (Many2one): Vehículo que fue transferido
        old_partner_id (Many2one): Contacto anterior (propietario anterior)
        new_partner_id (Many2one): Nuevo contacto (nuevo propietario)
        transfer_date (Datetime): Fecha y hora de la transferencia
        reason (str): Motivo de la transferencia
        user_id (Many2one): Usuario que realizó la transferencia
    """
    _name = 'vehicle.transfer.history'
    _description = 'Vehicle Transfer History'
    _order = 'transfer_date desc'

    vehicle_id = fields.Many2one(
        comodel_name='fleet.vehicle.custom',
        string='Vehículo',
        required=True,
        ondelete='cascade',
    )

    old_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contacto Anterior',
        required=True,
    )

    new_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Nuevo Contacto',
        required=True,
    )

    transfer_date = fields.Datetime(
        string='Fecha de Transferencia',
        default=fields.Datetime.now,
        required=True,
    )

    reason = fields.Text(
        string='Motivo',
    )

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Transferido Por',
        default=lambda self: self.env.user,
        required=True,
    )