mqttgraph
=========

Send MQTT JSON metrics to a graphite (carbon) server.


Configuration
-------------

Configure by editing _~/.mqttgraph.yml_:

    'mqtt_server': 'mqttserver'
    'mqtt_topics':
    		'home/bedroom/sensor1': ['temperature']
    'carbon_server': 'carbonserver'
    'carbon_port': 2003

Usage
-----

Python3 is required. Set up the config file, then run _mqttgraph_

    ./mqttgraph

Next, find a way to run this permanently (though screen always works...)

Credits
-------

Christian Bryn <chr.bryn@gmail.com> 2017
