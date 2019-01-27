## Required

<ul>
    <li>pip3</li>
    <li>python >= 3</li>
</ul>


## Dependencies

<ul>
    <li>Check : <code>requirements.txt</code></li>
</ul>

## Structure

```
Performics
│   README.md
│   requirements.txt   
│   server.py
│
└───controller
│   │   __init__.py
│   │   user.py
│   
│   
└───db 
│   │   __init__.py
│   │   conf.py
│   │   errorManager.py
│   
│   
└───router 
│   │   __init__.py
│   │   user.py
```

## Settings
__*DB connection infos : <code>./db/conf.py</code>*__

## Features
<h5>Basic API for User</h5>
<ul>
    <li><code>POST</code> : add new user</li> 
    <li><code>PUT</code> : update user by id</li> 
    <li><code>DELETE</code> : remove user by id</li> 
    <li><code>GET</code> : list users</li> 
    <li><code>GET</code> : show user by id</li> 
</ul>


## Get started
<ul>
    <li><code>$ python3 server.py</code></li>
</ul>





