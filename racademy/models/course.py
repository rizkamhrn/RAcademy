from odoo import api, fields, models


class Course(models.Model):
    _name = 'racademy.course'
    _description = 'Data Course'

    name = fields.Char(
        string='Course Name',
        required=True,
        help='Fill course name...'
    )

    description = fields.Text(
        string='Description'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    category_id = fields.Many2one(
        comodel_name='racademy.course.category', string='Category')
