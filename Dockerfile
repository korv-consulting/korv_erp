FROM odoo:17.0

USER root

# 1. TRADUCTION DE TES COMMANDES 'dnf install' (Version Debian/Ubuntu)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpq-dev \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# 2. INSTALLATION DU FRONTEND (rtlcss)
RUN npm install -g rtlcss

# 3. PRÉPARATION DE TON PROJET
WORKDIR /opt/odoo
# On copie TOUT ton projet dans /opt/odoo (donc ton odoo.conf et ton custom_addons)
COPY . /opt/odoo

# On installe tes dépendances
RUN pip3 install pip==22.0.4 && pip3 install -r /opt/odoo/requirements.txt

# On s'assure que l'utilisateur odoo a les droits sur les fichiers
RUN chown -R odoo:odoo /opt/odoo
USER odoo