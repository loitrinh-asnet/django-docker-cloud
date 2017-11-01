#######################################################
# Dockerfile to build a nginx image
# Build by command: "docker build -t loitrinh/nginx:0.1.0 ."
# Run by command: "docker run --name my-nginx-instance -P -d my-nginx"
#######################################################
# Base image is nginx
FROM nginx

# Author: Mr. Loi Trinh
MAINTAINER Mr. Loi Trinh <loi.trinhxuan@asnet.com>

# Copy nginx configuration
COPY ./compose/nginx/config/nginx.conf /etc/nginx/nginx.conf

# Data volume
VOLUME /var/log/nginx

# Expose port 8000
EXPOSE 8000

# Launch nginx server in the foreground
CMD ["nginx", "-g", "daemon off;"]
