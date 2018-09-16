# use -dt if detached mode
docker build -t my-temp-app-collect . && docker run -it --rm --privileged --network="host" --name my-running-temp-collect my-temp-app-collect
