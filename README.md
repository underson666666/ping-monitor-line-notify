# ping-monitor-line-notify

This is command line tool that is to nofity 'line notLINE_API_TOKENify' with ping monitoring.

## How to use

### Environment valiables

I would suggest setting the environment variable `LINE_API_TOKEN`.
```sh
export TARGET_HOST='<target ip>`
export LINE_API_TOKEN='<you token>`
```

### Monitoring target

Please change the value of valiable `monitor_target` in the python file.  
Maybe soon I will change to accept `monitor_target` from command line arguments. Maybe.

### Install packages

You need to install python packages like this.
```sh
pip install -r requirements.txt
```

### Execute

just like this.
```sh
python main.py
```

You can easily run with the docker command as well.
```sh
docker build -t <your image name> .
docker run -it --rm -e LINE_API_TOKEN=$LINE_API_TOKEN -e TARGET_HOST=<target id> <your image name>
```
