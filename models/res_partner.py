# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    """Extensión del modelo de Contactos para incluir gestión de vehículos.
    
    Hereda del modelo res.partner para agregar funcionalidades de gestión de flota.
    Permite asociar múltiples vehículos a un contacto (propietario) y mantener
    un conteo automático de vehículos asignados a cada contacto.
    """
    _inherit = 'res.partner'

    vehicle_ids = fields.One2many(
        comodel_name='fleet.vehicle.custom',
        inverse_name='partner_id',
        string='Vehículos',
    )

    vehicle_count = fields.Integer(
        string='Cantidad de Vehículos',
        compute='_compute_vehicle_count',
    )

    @api.depends('vehicle_ids')
    def _compute_vehicle_count(self):
        """
        Calcula la cantidad total de vehículos asociados al contacto.
        
        Este método se ejecuta automáticamente cada vez que cambia el campo
        vehicle_ids y actualiza el conteo de vehículos para cada contacto.
        """
        for partner in self:
            partner.vehicle_count = len(partner.vehicle_ids)