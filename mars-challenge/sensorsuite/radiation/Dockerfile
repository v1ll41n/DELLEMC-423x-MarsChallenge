#Baseimage
FROM busybox


#Copying the publisher binary from  current dir
COPY ./radiation  /mars-challenge/sensorsuite/radiation/

#set Workdir
WORKDIR  /mars-challenge/sensorsuite/radiation/

#running flare component
CMD ["./radiation"]
