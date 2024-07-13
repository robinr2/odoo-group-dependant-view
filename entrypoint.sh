#!/bin/bash
python3 -m debugpy --listen 0.0.0.0:5678 --wait-for-client /usr/bin/odoo
