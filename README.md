# odoo_livepos_test
answers to technical test


I created a new module called live_pos_test, when installed the user will see a menu item called Live POS test with sub menu items Users and Apartments. 

Upon clicking the Users menu, the user will see a list of all users/persons including the following fields: lastname, name, email, apartment_ids(shows which apartments are owned by the user/person), total_balance, total_sq_meters. The fields total_balance(overall balance) and total_sq_meters(sum of square meters owned by a person) are computed on the fly. 

The Apartments menu contans a list of all Apartments including the following fields: address, sq_meters, balance and user_id.

The fields balance and total_balance can only be viewed by users part of the group called Live POS Test Admin User. 

I have also committed the updated CSV files containing apartment and user info ready to be imported via Odoo's built-in import feature. 


