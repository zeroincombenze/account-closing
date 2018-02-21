[![Build Status](https://travis-ci.org/zeroincombenze/account-closing.svg?branch=8.0)](https://travis-ci.org/zeroincombenze/account-closing)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account-closing/badge.svg?branch=8.0)](https://coveralls.io/github/zeroincombenze/account-closing?branch=8.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account-closing/branch/8.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account-closing/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/account-closing/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)
































[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Account Invoice Accrual
=======================

Many companies want to establish a complete accounting situation at the end of
each period. An important aspect of this process is to accrue invoices for
which the goods or services were received / delivered but for which the invoice
has not been received / sent.

Account Invoice Accrual lets you easily create these provisions entries.

Installation
------------





There is nothing special to do to install this module.

Configuration
-------------





The default accrual accounts can be configured on the company form.
Expense and revenue account can be mapped to other accounts when doing
accruals using the the mapping framework provided by the account_cutoff_base
modules (Accounting > Configuration > Accounts > Cut-off account mappings.

Usage
-----







=====

This module adds a new Accrual button draft and pro-forma invoices. This button
triggers a wizard where the user can chose the accrual date, period, journal and account.
When later validating the invoice, the accrual move is automatically reversed 
in the same period as the invoice.

Known issues / Roadmap
----------------------




Bug Tracker
-----------





Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-closing/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/account-closing/issues/new?body=module:%20account_invoice_accrual%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
-------









### Contributors





* Laetitia Gangloff (ACSONE) <laetitia.gangloff@acsone.eu>
* Adrien Peiffer (ACSONE) <adrien.peiffer@acsone.eu>
* Stéphane Bidoul (ACSONE) <stephane.bidoul@acsone.eu>

### Funders

### Maintainer








.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be deployed on local server too.

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
