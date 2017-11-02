#######################################################
# Dockerfile to build a LOG Volume for nginx Service
# Build by command: "docker build -t nginxlog ."
# Run by command: "docker run --name log_vol nginxlog"
#######################################################
# Base image is BusyBox
FROM busybox:latest

# Author: Mr. Loi Trinh
MAINTAINER Mr. Loi Trinh <loi.trinhxuan@asnet.com>

# Create a data volume at /var/log/apache2, which is
# same as the log directory PATH set for the apache image
VOLUME /var/log/nginx

# Execute command true
CMD ["/bin/true"]
