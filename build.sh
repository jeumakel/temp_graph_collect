# use -dt if detached mode
docker build -t my-temp-app . && docker run -it --rm --privileged --name my-running-temp my-temp-app
#docker build -t my-temp-app . && docker run -dt --restart unless-stopped --network=host --privileged --name my-running-temp my-temp-app
