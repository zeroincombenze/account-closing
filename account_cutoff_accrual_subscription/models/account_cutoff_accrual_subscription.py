# -*- coding: utf-8 -*-
# Copyright 2019 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountCutoffAccrualSubscription(models.Model):
    _name = 'account.cutoff.accrual.subscription'
    _description = 'Subscriptions to compute accrual cutoffs'
    _order = 'subscription_type, name'

    company_id = fields.Many2one(
        'res.company', string='Company',
        ondelete='cascade', required=True,
        default=lambda self: self.env['res.company']._company_default_get())
    company_currency_id = fields.Many2one(
        string='Company Currency',
        related='company_id.currency_id', readonly=True, store=True)
    name = fields.Char(required=True)
    subscription_type = fields.Selection([
        ('revenue', 'Revenue'),
        ('expense', 'Expense'),
        ], default='expense', required=True, string='Type')
    partner_type = fields.Selection([
        ('none', 'No Partner'),
        ('one', 'Specific Partner'),
        ('any', 'Any Partner'),
        ], default='one', string='Partner Type', required=True)
    partner_id = fields.Many2one(
        'res.partner', string='Supplier',
        domain=[('parent_id', '=', False), ('supplier', '=', True)],
        ondelete='restrict')
    active = fields.Boolean(default=True)
    periodicity = fields.Selection([
        ('month', 'Monthly'),
        ('quarter', 'Quarterly'),
        ('semester', 'Semesterly'),
        ('year', 'Yearly'),
        ], string='Periodicity', required=True)
    start_date = fields.Date(required=True)
    min_amount = fields.Monetary(
        string='Minimum Expense Amount', required=True,
        currency_field='company_currency_id',
        help='Minimum expense amount without taxes over the period')
    provision_amount = fields.Monetary(
        string='Default Provision Amount',
        currency_field='company_currency_id')
    account_id = fields.Many2one(
        'account.account', string='Account', required=True,
        domain=[('deprecated', '=', False)])
    analytic_account_id = fields.Many2one(
        'account.analytic.account', string='Analytic Account')
    tax_ids = fields.Many2many(
        'account.tax', string='Taxes',
        domain=[('price_include', '=', False)])

    @api.constrains('start_date')
    def check_start_date(self):
        for sub in self:
            start_date_dt = fields.Date.from_string(sub.start_date)
            if start_date_dt.day != 1:
                raise ValidationError(_(
                    "On subscription %s, the start date is not the first "
                    "day of a month.") % sub.display_name)

    _sql_constraints = [
        ('min_amount_positive',
         'CHECK(min_amount >= 0)',
         'The minimum amount must be positive.'),
        ('provision_amount_positive',
         'CHECK(provision_amount >= 0)',
         'The default provision amount must be positive.'),
        ]

    @api.onchange('min_amount')
    def min_amount_change(self):
        if self.min_amount > 0 and not self.provision_amount:
            self.provision_amount = self.min_amount

    @api.onchange('account_id')
    def account_id_change(self):
        if self.account_id:
            self.tax_ids = self.account_id.tax_ids

    @api.onchange('partner_type')
    def partner_type_change(self):
        if self.partner_type != 'one':
            self.partner_id = False
