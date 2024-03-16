FROM kociarz/kottomasz


WORKDIR /app
COPY pom.xml /app

RUN mvn -f /app/pom.xml dependency:go-offline -B 

COPY src /app/src

RUN mvn -f /app/pom.xml clean package
RUN cp -R /app/target/webapp-1.0 /apache-tomcat/webapps/ROOT

EXPOSE 8080

RUN chmod 444 /apache-tomcat/conf/web.xml
RUN chmod 777 /apache-tomcat/work
RUN chmod 777 /apache-tomcat/temp

USER nobody
CMD ["/apache-tomcat/bin/catalina.sh", "run"]