#!/bin/bash
set -e

# Générer le fichier odoo.conf avec les variables d'environnement
cat <<EOF > /etc/odoo/odoo.conf
[options]
data_dir = /var/lib/odoo
db_host = ${DB_HOST}
db_port = ${DB_PORT}
db_user = ${DB_USER}
db_password = ${DB_PASSWORD}
admin_passwd = superadmin123
addons_path = addons, custom_addons
proxy_mode = True

EOF

# Lancer Odoo
exec odoo