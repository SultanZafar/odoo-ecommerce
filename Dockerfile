FROM odoo:18.0

USER root

COPY ./custom_addons /mnt/extra-addons

COPY odoo.conf /etc/odoo/odoo.conf

EXPOSE 8069

USER odoo
