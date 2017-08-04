elasticache-auto-discovery
===
Python client for AWS Elasticache [Auto Discovery Endpoint](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/AutoDiscovery.html).

## Usage

```python
>>> import elasticache_auto_discovery
>>> print elasticache_auto_discovery.discover('ELASTICACHE_ENDPOINT:11211')
[['HOSTNAME1', 'IP_ADDR1', 'PORT1'],
 ['HOSTNAME2', 'IP_ADDR2', 'PORT2']]
```


You can also pass a time to timeout(by seconds)

```python
>>> elasticache_auto_discovery.discover('ELASTICACHE_ENDPOINT:11211',
                                        time_to_timeout=5.0)
```
