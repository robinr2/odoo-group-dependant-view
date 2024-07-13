reload bug:

- change users group from group_p1 to group_p2
- open a contact
- the p1 field is still visible
- refresh the page and the p2 field is visible

odoo.conf:
[options]
addons_path = /mnt/extra-addons
data_dir = /var/lib/odoo

docker-compose.yml:
services:
web:
build: .
depends_on: - db
ports: - "8069:8069" - "5678:5678"
volumes: - odoo-web-data:/var/lib/odoo - ./config:/etc/odoo - ./addons:/mnt/extra-addons
environment: - PASSWORD_FILE=/run/secrets/postgresql_password
secrets: - postgresql_password
db:
image: postgres:15
environment: - POSTGRES_DB=postgres - POSTGRES_PASSWORD_FILE=/run/secrets/postgresql_password - POSTGRES_USER=odoo - PGDATA=/var/lib/postgresql/data/pgdata
volumes: - odoo-db-data:/var/lib/postgresql/data/pgdata
secrets: - postgresql_password
volumes:
odoo-web-data:
odoo-db-data:
secrets:
postgresql_password:
file: odoo_pg_pass

Dockerfile:
FROM odoo:16.0

USER root

RUN pip install debugpy

COPY ./entrypoint.sh /

RUN chmod +x /entrypoint.sh

USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]

odoo_pg_pass:
POSTGRES_PASSWORD=odoo

entrypoint.sh:
#!/bin/bash
python3 -m debugpy --listen 0.0.0.0:5678 --wait-for-client /usr/bin/odoo
