# -*- coding: utf-8 -*-
from odoo import api, fields, models
class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    city = fields.Char(string="City:")
    active = fields.Boolean(string="Active", default=True)

