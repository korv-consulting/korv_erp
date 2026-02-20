FROM odoo:17.0

USER root
WORKDIR /opt/odoo
# On copie TOUT ton projet dans /opt/odoo (donc ton odoo.conf et ton custom_addons)
COPY . /opt/odoo

# On installe tes dépendances
RUN pip3 install pip==22.0.4 && pip3 install -r /opt/odoo/requirements.txt

# On s'assure que l'utilisateur odoo a les droits sur les fichiers
RUN chown -R odoo:odoo /opt/odoo
USER odoo