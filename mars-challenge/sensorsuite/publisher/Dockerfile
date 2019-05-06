#Baseimage
FROM busybox


#Copying the publisher binary from  current dir
COPY ./publisher  /mars-challenge/sensorsuite/publisher/

#set Workdir
WORKDIR  /mars-challenge/sensorsuite/publisher/

#running flare component
CMD ["./publisher"]
