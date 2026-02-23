# 1. Image de base
FROM odoo:17.0

# 2. Passer en root
USER root

# 3. Dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    nodejs \
    npm \
    && rm -rf /usr/local/lib/node_modules/rtlcss \
    && npm install -g rtlcss \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 4. Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 5. Port
EXPOSE 8069

# 6. Workdir
WORKDIR /opt/odoo

# 7. Copier projet avec ownership direct
COPY --chown=odoo:odoo . /opt/odoo

# 8. Installer dépendances Python
RUN pip3 install --no-cache-dir pip==22.0.4 \
    && pip3 install --no-cache-dir -r requirements.txt

# 9. Repasser en user odoo
USER odoo

# 10. Entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# # 1. Image de base
# FROM odoo:17.0

# # 2. Passer en root pour installer et copier des fichiers
# USER root

# # 3. Installation des dépendances système nécessaires pour compiler python-ldap
# RUN apt-get update && apt-get install -y \
#     gcc \
#     python3-dev \
#     libldap2-dev \
#     libsasl2-dev \
#     libssl-dev \
#     && rm -rf /var/lib/apt/lists/*

# RUN apt-get update && apt-get install -y nodejs npm \
#     && rm -rf /usr/local/lib/node_modules/rtlcss \
#     && npm install -g rtlcss \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# # 4. Copier l'entrypoint et le rendre exécutable
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# # 5. Exposer le port d'Odoo
# EXPOSE 8069

# # 6. Préparer le dossier de travail et copier le projet
# WORKDIR /opt/odoo
# # On copie TOUT ton projet dans /opt/odoo (donc ton odoo.conf et ton custom_addons)
# # COPY . /opt/odoo
# COPY --chown=odoo:odoo . /opt/odoo

# # 7. On installe tes dépendances
# RUN pip3 install pip==22.0.4 && pip3 install -r /opt/odoo/requirements.txt

# # 8. On s'assure que l'utilisateur odoo a les droits sur les fichiers
# RUN chown -R odoo:odoo /opt/odoo

# # 9. Repasser en utilisateur odoo pour exécuter le service
# USER odoo

# # 10. Définir l’entrypoint pour générer le odoo.conf et lancer Odoo
# ENTRYPOINT ["/entrypoint.sh"]