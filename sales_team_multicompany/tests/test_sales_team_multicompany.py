# -*- coding: utf-8 -*-
# © 2016 Chafique DELLI @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError


class TestSalesTeamMultiCompany(TransactionCase):
    def setUp(self):
        #import pdb; pdb.set_trace()
        super(TestSalesTeamMultiCompany, self).setUp()

        # models
        self.company_model = self.env['res.company']
        self.user_model = self.env['res.users']
        self.partner_model = self.env['res.partner']
        self.toto = self.partner_model.browse(267)

        # companies
        self.main_company = self.env.ref('base.main_company')
        self.currency_usd = self.env.ref('base.USD')


    def test_create_sale_order_with_sale_team(self):
        # All of this should be allowed
        vals = {'name': 'SecondCompany',
                'currency_id': self.currency_usd.id,
                'partner_id': self.toto.id,
                }

        secondary_company = self.company_model.create(vals)
        print secondary_company.id
