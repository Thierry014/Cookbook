Module Data

# Using external IDs and namespaces
XML ID => IR.MODEL.DATA
self.env.ref(module_name.record_id) => access XML ID


# Loading data using XML files (manually create)
<odoo> 
    <record id="author_pga" model="res.partner">
        <field name="name">Parth Gajjar</field>
    </record>
    <field name="author_ids" eval="[(6, 0, [ref('author_af'), ref('author_dr'), ref('author_hb')])] 
</odoo>
# Using the noupdate and forcecreate flags
<odoo noupdate="1">
? -i works on installed module ? => Yes 
xxx.conf -i your_addon
#? This will force Odoo to reload your records. This will also cause deleted records to be recreated. Note that this can cause double records
# Loading data using CSV files
# Add-on updates and data migration
# Deleting records from XML files
<record id="book_category_to_delete" model="library.book.category">
    <field name="name">Test Category</field>
</record>

<delete model="library.book.category" id="book_category_to_delete"/>
<delete model="library.book.category" search="[('name','ilike', 'Test')]"/>
# Invoking functions from XML files