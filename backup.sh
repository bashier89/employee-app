#!/bin/bash

DATE=$(date +%Y%m%d)

docker compose exec -T mysql mysqldump -uroot -ppassword employee_db > backup_$DATE.sql

if [ $? -eq 0 ]; then
  echo "Backup completed successfully"
else
  echo "Backup failed"
fi


