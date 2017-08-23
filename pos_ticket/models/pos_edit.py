from odoo import api, fields, models
from num2words import num2words


class Pos_edit(models.Model):
	_inherit = 'pos.order'

	amount_total = fields.Float(store=True)
	x_cmoto = fields.Char(compute="convertir_aletras")

	@api.one
	@api.depends('amount_total')
	def convertir_aletras(self):
		for record in self:
			total_numero = record['amount_total']
			try:
				numletras = num2words(total_numero, lang='es')
				record['x_cmoto'] = numletras
			except NotImplementedError:
    			        numletras = num2words(total_numero)
				record['x_cmoto'] = numletras
			print "***************************** **********"
