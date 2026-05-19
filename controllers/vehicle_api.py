# -*- coding: utf-8 -*-

import json
import logging

from odoo import http
from odoo.http import request, Response

_logger = logging.getLogger(__name__)


class VehicleApiController(http.Controller):

    def _json_response(self, data, status=200):
        return Response(
            json.dumps(data, ensure_ascii=False, default=str),
            status=status,
            content_type='application/json; charset=utf-8'
        )

    @http.route(
        '/api/vehicles/contact/<int:partner_id>',
        type='http',
        auth='public',
        website=False,
        csrf=False
    )
    def get_vehicles_by_contact(self, partner_id, **kwargs):

        try:

            partner = request.env['res.partner'].sudo().browse(partner_id)

            if not partner.exists():
                return self._json_response({
                    'success': False,
                    'message': 'Contacto no encontrado',
                    'vehicles': []
                }, status=404)

            vehicles = request.env['fleet.vehicle.custom'].sudo().search([
                ('partner_id', '=', partner.id)
            ])

            result = []

            for vehicle in vehicles:

                result.append({
                    'id': vehicle.id,
                    'license_plate': vehicle.license_plate,
                    'brand': vehicle.brand,
                    'model': vehicle.model,
                    'year': vehicle.year,
                    'vehicle_type': vehicle.vehicle_type,
                    'color': vehicle.color,
                    'partner_id': partner.id,
                    'partner_name': partner.display_name,
                })

            return self._json_response({
                'success': True,
                'partner_id': partner.id,
                'partner_name': partner.display_name,
                'total_vehicles': len(result),
                'vehicles': result
            })

        except Exception as e:

            _logger.exception('Error consultando vehículos por contacto')

            return self._json_response({
                'success': False,
                'message': str(e)
            }, status=500)