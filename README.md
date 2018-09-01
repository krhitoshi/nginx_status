A Python script and a Zabbix template to retrieve and monitor nginx status data.

## Installation

```
location /nginx_status {
    stub_status on;
    access_log  off;
    allow 127.0.0.1;
    allow ::1;
    deny  all;
}
```

```
$ sudo nginx -t
$ sudo nginx -s reload
```

```
$ curl http://localhost/nginx_status
Active connections: 1
server accepts handled requests
 335045 335045 240761
Reading: 0 Writing: 1 Waiting: 0
```

```
$ git clone https://github.com/krhitoshi/nginx_status.git
$ sudo cp nginx_status/nginx_status.py /usr/local/bin/nginx_status.py
$ sudo cp nginx_status/userparameter_nginx.conf /etc/zabbix/zabbix_agentd.d/
$ sudo systemctl restart zabbix-agent.service
```

```
$ /usr/local/bin/nginx_status.py active
1
```

```
$ zabbix_agentd -t "nginx.status[active]"
nginx.status[active]                          [t|2]
```
