from odoo import api, fields, models
from openerp.tools import amount_to_text_en

from num2words import num2words

from openerp.tools.amount_to_text import amount_to_text

from openerp.tools import amount_to_text


class Pos_edit(models.Model):
	_inherit = 'pos.order'

	#x_cmoto = fields.Char()
	#amount_total

	@api.multi
	def _number2words(self):
	    return num2words(self.amount_total)

	@api.multi
	def _convertir(self):
		return amount_to_text_en(self.amount_total)

	@api.multi
        def amount_to_texto(self, amount_total, currency='INR'):
            return amount_to_text(self.amount_total, currency)


	@api.multi
	def number_to_words(num, self):
            d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
        	6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
         	11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
        	15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          	19 : 'nineteen', 20 : 'twenty',
          	30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          	70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
	    k = 1000
	    m = k * 1000
	    b = m * 1000
	    t = b * 1000

	    num = self.amount_total

	    assert(0 <= num)

	    if (num < 20):
	        return d[num]

	    if (num < 100):
	        if num % 10 == 0: return d[num]
	        else: return d[num // 10 * 10] + '-' + d[num % 10]

	    if (num < k):
	        if num % 100 == 0:
                    print "******************************* entrando al modulo ***************************"
                    return d[num // 100] + ' hundred'
	        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

	    if (num < m):
	        if num % k == 0: return int_to_en(num // k) + ' thousand'
	        else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

	    if (num < b):
	        if (num % m) == 0: return int_to_en(num // m) + ' million'
	        else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

	    if (num < t):
	        if (num % b) == 0: return int_to_en(num // b) + ' billion'
	        else: return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)

	    if (num % t == 0): return int_to_en(num // t) + ' trillion'
	    else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

            raise AssertionError('num is too large: %s' % str(num))
	    temp_amount = str(self.amount_total)
	    if '.' in temp_amount:
	        amount = temp_amount.split('.')
		dollars = amount[0]
		cents = amount[1]
	    else:
	        dollars = temp_amount
		cents = '00'

	    amt = number_to_words(int(dollars))
	    cents = number_to_words(int(cents))
	    total = amt + ' rupees and '+ cents + ' paisa'
	    return total
