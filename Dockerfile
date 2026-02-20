FROM odoo:17.0

USER root

# 1. Installation des dépendances système nécessaires pour compiler python-ldap
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. INSTALLATION DU FRONTEND (rtlcss)
RUN apt-get update && apt-get install -y nodejs npm \
    && rm -rf /usr/local/lib/node_modules/rtlcss \
    && npm install -g rtlcss \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 3. PRÉPARATION DE TON PROJET
WORKDIR /opt/odoo
# On copie TOUT ton projet dans /opt/odoo (donc ton odoo.conf et ton custom_addons)
COPY . /opt/odoo

# On installe tes dépendances
RUN pip3 install pip==22.0.4 && pip3 install -r /opt/odoo/requirements.txt

# On s'assure que l'utilisateur odoo a les droits sur les fichiers
RUN chown -R odoo:odoo /opt/odoo
USER odoo