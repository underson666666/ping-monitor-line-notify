# ping-monitor-line-notify

This is command line tool that is to nofity 'line notify' with ping monitoring.

## How to use

### Environment valiables

You need to set envinronment varialbe 'LINE_API_TOKEN'.
```sh
export LINE_API_TOKEN='<you token>`
`'```

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
