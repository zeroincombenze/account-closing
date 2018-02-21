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

Manage prepaid expense and revenue based on start and end dates
===============================================================

This module adds a **Start Date** and **End Date** field on invoice lines. For
example, if you have an insurance contrat for your company that run from April
1st 2013 to March 31st 2014, you will enter these dates as start and end dates
on the supplier invoice line. If your fiscal year ends on December 31st 2013,
3 months of expenses are part of the 2014 fiscal year and should not be part of
the 2013 fiscal year. So, thanks to this module, you will create a *Prepaid
Expense* on December 31st 2013 and Odoo will identify this expense with the
3 months that are after the cut-off date and propose to generate the
appropriate cut-off journal entry.

Please contact Alexis de Lattre from Akretion <alexis.delattre@akretion.com>
for any help or question about this module.

Installation
------------




Configuration
-------------




Usage
-----







Known issues / Roadmap
----------------------




Bug Tracker
-----------




Credits
-------









### Contributors





* Alexis de Lattre <alexis@via.ecp.fr>
* Stéphane Bidoul <stephane.bidoul@acsone.eu>
* Daniel Rodríguez Lijo <drl.9319@gmail.com>

### Funders

### Maintainer








.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

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
