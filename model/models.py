
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subscribers(models.Model):
	_name = 'dpo_assistant.subscribers'

	name = fields.Char()
	email = fields.Char()
	company = fields.Char()
	contact_number = fields.Char(string='Contact Number')
	message = fields.Text()
