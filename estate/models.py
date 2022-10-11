from odoo import models, fields


class estate_property(models.Model):
    _name = "estate.property"
    _description = "Estate test model for Odoo"
    

    name = fields.Char('Name', required=True, translate=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode', required=True)
    date_availability = fields.Datetime('Date of availability', default=fields.Datetime.add(fields.Datetime.today(), months=3), copy=False)
    expected_price = fields.Float()
    selling_price = fields.Float('Selling price', readonly=True, copy=False)
    bedrooms = fields.Integer('Number of rooms', default="2", required=True)
    living_area = fields.Integer('# living area', required=True)
    facades = fields.Integer()
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('# garden area')
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )