# Bioportal backend
Backend of Bioportal, web application created to offer frontend a connection to openstack cloud via REST API. This backend runs at [link](http://bio-portal.metacentrum.cz/).
On the server side, it's running in Docker container. The Dockerfile is not provided here yet.

## Requirements
* Python 3
* Nginx
* [python requirements](https://github.com/andrejcermak/openstack/blob/master/requirements.txt)

## Usage
```
sudo sh start.sh
```

## Contributing
1.Fork [openstack](`https://github.com/andrejcermak/openstack/fork`)

2.Create your feature branch (`git checkout -b my-new-feature`)

3.Commit your changes (`git commit -am 'Add some feature'`)

4.Push to the branch (`git push origin my-new-feature`)

5.Create a new Pull Request
