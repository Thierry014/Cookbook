# Model 

# Todo LIst
# name_get() => customize rec_name

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