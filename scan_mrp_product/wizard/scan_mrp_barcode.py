from odoo import api, fields, models
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class WizardMRPSerial(models.TransientModel):
	_name = 'wizard.mrp.scan.dev.serial'
	_description = 'Scan ProductSerial'

	serial = fields.Char(required=True, string='Barcode')
	
	"""@api.onchange('serial')
	def onchange_serial(self):
		if self.serial:
			#search for serial in stock.production.lot
			product = self.env['product.product'].search([('barcode', '=', self.serial)])
			
			move_line = self.mrp_id.move_raw_ids.filtered(lambda r: r.product_id.id == product.id)
			if move_line:
				move_line[0].write({
					'quantity_done': move_line.product_uom_qty,
				})
			else:
				raise UserError("Product doesn't exist")
			#referesh 
			self.serial = ''"""