# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class FleetVehicleCustom(models.Model):
    """Modelo para gestionar vehículos personalizados de la flota.
    
    Este modelo permite registrar y administrar vehículos en el sistema,
    incluyendo información básica del vehículo como marca, modelo, año y tipo,
    así como su asociación con contactos (propietarios) y el historial de transferencias.
    
    """
    _name = 'fleet.vehicle.custom'
    _description = 'Custom Fleet Vehicle'
    _rec_name = 'license_plate'
    _order = 'id desc'

    license_plate = fields.Char(
    string='Matrícula',
    required=True,
    copy=False,
    )

    brand = fields.Char(
        string='Marca',
        required=True,
    )

    model = fields.Char(
        string='Modelo',
        required=True,
    )

    year = fields.Integer(
        string='Año',
        required=True,
    )

    vehicle_type = fields.Selection([
        ('sedan', 'Sedán'),
        ('pickup', 'Pickup'),
        ('suv', 'SUV'),
        ('truck', 'Camión'),
        ('motorcycle', 'Motocicleta'),
        ('other', 'Otro'),
    ], string='Tipo de Vehículo', required=True)

    color = fields.Char(
        string='Color',
    )

    active = fields.Boolean(
        string='Activo',
        default=True,
    )

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contacto',
        required=True,
        ondelete='restrict',
    )

    transfer_history_ids = fields.One2many(
        comodel_name='vehicle.transfer.history',
        inverse_name='vehicle_id',
        string='Historial de Transferencias',
    )

    _sql_constraints = [
        (
            'unique_license_plate',
            'unique(license_plate)',
            'La placa debe ser única.'
        )
    ]

    @api.constrains('year')
    def _check_year(self):
        """
        Valida que el año del vehículo sea válido.
        
        Comprueba que el año esté entre 1900 y el año actual más uno.
        Lanza ValidationError si el año no es válido.
        """
        current_year = datetime.now().year + 1

        for record in self:
            if record.year < 1900 or record.year > current_year:
                raise ValidationError(
                    _('El año del vehículo debe estar entre 1900 y %s.') % current_year
                )

    def unlink(self):
        """
        Previene la eliminación de vehículos asociados a contactos activos.
        
        Comprueba que ninguno de los vehículos a eliminar esté asociado a un 
        contacto activo. Si lo está, lanza ValidationError.
        
        :return: Resultado de super().unlink()
        :raises ValidationError: Si el vehículo está asociado a un contacto activo.
        """
        for record in self:
            if record.partner_id and record.partner_id.active:
                raise ValidationError(
                    _('No puede eliminar un vehículo asociado a un contacto activo.')
                )

        return super().unlink()