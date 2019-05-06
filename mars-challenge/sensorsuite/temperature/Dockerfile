#Baseimage
FROM busybox


#Copying the publisher binary from  current dir
COPY ./temp  /mars-challenge/sensorsuite/temperature/

#set Workdir
WORKDIR  /mars-challenge/sensorsuite/temperature/

#running flare component
CMD ["./temp"]
