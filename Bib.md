# field 

* many2many, many2one => fields(model_name) 
DB: New rel_table 

* one2many => fields(module_name, column_name)
before define o2m, define a m2o first
DB: show on many side [Show into Book table, publish_id = 1]

* Relateion field attr ondelete='restrict, cascade'

* Date, Datetime field in DB are store as Date/Datetime not String 

* Add field active to make record can be archived 

# computed field 
* always set up a value to a computed field
* always use with @api.depends
* inverse function make computed field editable, should use with store = True
* depends won't trigger when its not a computed field
* computed field always influenced by other field not it self
*! comupted method run when the page rendered (all record in this model will re-calculate)

# context 