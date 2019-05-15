`1.3.2`
-------

- **Fix**: Models without group binded rules were then wrongly reduced to an 'AND FALSE' condition. After https://github.com/odoo/odoo/commit/023dfaeb6b9499943315358edaa01c8f823ee695

`1.3.1`
-------

- **Fix**: Random wrong result on applying rules in backend

`1.3.0`
-------

- **New:** add ``website`` object to a rule evaluation context - to be able to use rules as such ``[('id','=', website.company_id.id)]``

`1.2.0`
-------

- **Add:** Use user's **Current Backend Website** from ``web_website`` module  on evaluating website rules in Odoo backend

`1.1.0`
-------

- **Add:** New setting in ``ir.rule`` model - to bypass website rules when working from backend

`1.0.0`
-------

- **Init version**
