 #! Model 

 # Todo Goal: 
# Creating and installing a new add-on module
#? library 
# Completing the add-on module manifest
# Organizing the add-on module file structure
# Adding models
# Adding menu items and views
#? add menu
#! sub menu add 
<menuitem name="Books" id="library_book_menu"  parent="library_base_menu" action="library_book_action">
        <menuitem name="B1" id="library_book_submenu_1" action="library_book_action"/>
        <menuitem name="B2" id="library_book_submenu_2" action="library_book_action"/>
        <menuitem name="B3" id="library_book_submenu_3" action="library_book_action"/>
</menuitem>
#? https://www.odoo.com/documentation/14.0/developer/howtos/rdtraining/06_firstui.html

#todo groupby in search view
# Adding Access Security
