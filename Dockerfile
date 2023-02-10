FROM postgres
ENV POSTGRES_PASSWORD NQRLGaAjR44JM5Zk
ENV POSTGRES_DB postgres
COPY create_db.sql /docker-entrypoint-initdb.d/

#docker build -t eu.gcr.io/wagon-bootcamp-355610/workshopdb:prod .
#docker push eu.gcr.io/wagon-bootcamp-355610/simpledb:prod
