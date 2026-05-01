FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=lms
ENV MYSQL_USER=lms_user
ENV MYSQL_PASSWORD=lms_password
COPY lms.sql /docker-entrypoint-initdb.d/01-lms.sql
VOLUME ["/var/lib/mysql"]
EXPOSE 3306
