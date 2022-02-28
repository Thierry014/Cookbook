# Model 

# Todo LIst
# name_get() => customize rec_name
def name_get(self):
    result = []
    for record in self:
        rec_name = f"{record.name}-({record.date_release})"
        result.append((record.id, rec_name))
    return result
#? Book 2-(1992-04-05)
#? _rec_name can be used to setup simple record name    

# Date, Datetime field in DB are store as Date/Datetime not String 

# Model Constraint 
    #? DB 
    _sql_constraints = [
    ('name_uniq', # cons name
    'UNIQUE (name)', # cons
    'Book title must be unique.') #warning
    ]
    #? SERVER 
    @api.constrains('date_release') #when field update => trigger

# computed field

# make field searchable 
    #? 1. in xml add domain =>
    #? 2. add search when define field =>

    # 2. owner2 = fields.Many2one('res.partner', string="Owner without mobile", domain=[('mobile','!=',False)] )
    # 1. <filter string="No Authors" name="without_author" domain="[('author_ids','=',False)]"/>

# Related field
publisher_city = fields.Char('Publisher City',related='publisher_id.city',readonly=True)

# selection field vs reference field 
static => field.Selection([(k:v),(k:v),(k:v)])
dynamic => fields.Reference(selection='_function_cal_selection')

function return [(x.k,x.v) for x in self.searhc()...]

# inheritance 