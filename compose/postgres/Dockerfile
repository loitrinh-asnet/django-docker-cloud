###########################################
# Dockerfile to build an Postgres image
###########################################

# Base image is Postgres 9.6
FROM postgres:9.6

# Author Mr.Trinh
MAINTAINER Mr.Trinh <loi.trinhxuan@asnet.com.vn>

# Copy backup database script
COPY ./scripts/backup.sh /usr/local/bin/backup
RUN chmod +x /usr/local/bin/backup

# Copy restore database script
COPY ./scripts/restore.sh /usr/local/bin/restore
RUN chmod +x /usr/local/bin/restore

# Copy the list of backups script
COPY ./scripts/list-backups.sh /usr/local/bin/list-backups
RUN chmod +x /usr/local/bin/list-backups

