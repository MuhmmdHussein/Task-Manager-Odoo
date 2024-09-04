from odoo import fields, models

class TaskTicket(models.Model):
    _name = 'task.ticket'

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    state = fields.Selection([
        ('start', 'Start'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')],
    )
    file = fields.Binary()
    assign_to = fields.Many2one('res.partner')
    description = fields.Text()
    start_time = fields.Datetime()
    deadline = fields.Datetime()
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')],
    )

    def action_start(self):
        for rec in self:
            rec.state = 'start'

    def action_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_complete(self):
        for rec in self:
            rec.state = 'complete'
