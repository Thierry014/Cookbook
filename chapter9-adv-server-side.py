# Changing the user that performs an action
from multiprocessing import Condition


sudo()
# Calling a method with a modified context
#! new understand 
book = self.book_id.with_context(have_ctx=True)
book.call_fun()
create a copy existing record => with ctx => apply function on this copy record

in call_fun() we can set up Condition for record with different ctx


#! more about ctx 
In a record => click button => to a wizard 
record have ctx => pass to wizard and can be used to set default value for some fields
# Executing raw SQL queries
#todo
# Writing a wizard to guide the user
#? step and code in tempalte 
# Defining onchange methods

# Calling onchange methods on the server side

# Defining a model based on an SQL view

# Adding custom settings options
# todo 
# implied_group in field => (optional)
# res.conf.py, create some setting fields 
# view => form view
# link back to setting (menuitem => action.window) (optional)

# Implementing init hooks
hooks fun 