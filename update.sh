pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d fellowcrm/translations
