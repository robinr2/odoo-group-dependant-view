FROM odoo:16.0

USER root

RUN pip install debugpy

COPY ./entrypoint.sh /

RUN chmod +x /entrypoint.sh

USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
