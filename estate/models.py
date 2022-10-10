from odoo import models, fields


class estate_property(models.Model):
    _name = "estate.property"
    _description = "Estate test model for Odoo"
    _order = "sequence"

    name = fields.Char('Name', required=True, translate=True)
    description = fields.Text()
    postcode = fields.Char('Postcode', required=True)
    date_availability = fields.Date('date', required=True)
    expected_price = fields.Float()