# Server side basic
# Defining model methods and using API decorators

# Reporting errors to the user

# Obtaining an empty recordset for a different model
from multiprocessing.sharedctypes import Value


model = self.env['model.name']
# Creating new records
model.create(
    {
    'field_name': Value1,
    'field_name': Value2,
    })
# Updating values of recordset records
    #? only update one field => self.name = ''new val'
    #? update recordset => self.update({k:v,k1:v1})

    #! when update relational_field 
# Searching for records

# Combining recordsets
P186
    #? R1+R2 (duplicate)
    #? R1-R2
    #? R1 & R2 (intersection)
    #? R1 | R2 (no duplication)
# Filtering recordsets
    #? all_books.filter(lambda b: len(b.author_ids) > 1)
# Traversing recordset relations
    #? books.mapped('author_ids.name') => res,partner(1,2,3)
    #? books.mapped('name') => ['David','Henry','James']
    #! If the last field in the path is a relational field, mapped() will return a recordset; otherwise, a Python list is returned.
# Extending the business logic defined in a model
SUPER() => P194 find a case to test

    #? Call super before do modification => res = super().fun(), return res 
    #? call super after modification  => return super().fun()
# Extending write() and create()

# Customizing how records are searched