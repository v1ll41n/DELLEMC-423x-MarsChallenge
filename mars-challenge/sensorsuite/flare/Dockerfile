#Baseimage
FROM busybox


#Copying the flare binary from  current dir
COPY ./flare  /mars-challenge/sensorsuite/flare/

#set Workdir
WORKDIR  /mars-challenge/sensorsuite/flare/

#running flare component
CMD ["./flare"]
