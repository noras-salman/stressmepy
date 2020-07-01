# stressmepy
Perform stress tests on your web server
 

## Usage: (Example)
```python
from stressmepy import StressTest 

# Number of concurrent requests to be performed
requests=500

# Construct the request to be performed
s=StressTest("http://www.example.com",requests,options={
    "method":"GET",
    "headers":{"Cookie":"hello_im_a_cookie_header"}
})

# Run the test
s.run()

# Get the results
results=s.results()

# Print the results
print(results)
```


## Runing the example
```sh
pip3.6 install -r requirements.txt
python3.6 main.py
```

## Result format
```json
{
  "url": "http://www.example.com",
  "total_requests": 100,
  "total_time": 2695.2340249999984,
  "time_stat": {
    "highest": 30.288255,
    "lowest": 5.834499,
    "average": 26.952340249999985
  },
  "performance_stat": {
    "success": 100,
    "failed": 0,
    "connected": 100,
    "refused": 0
  },
  "time_log": [
    6.383139,
    5.834499,
    6.39554,
    6.385681,
    29.807131,
    7.675352,
    25.191751,
    26.331101,
    14.317758,
    26.336387,
    25.413511,
    9.27306,
    6.388724,
    29.793909,
    8.179039,
    8.17169,
    25.160307,
    26.314116,
    25.157796,
    17.78298,
    26.29367,
    27.198396,
    8.559547,
    26.307375,
    26.29883,
    26.292404,
    17.770959,
    29.958307,
    29.028845,
    30.166818,
    29.755277,
    30.176896,
    30.101648,
    29.675135,
    29.685821,
    29.660535,
    30.219312,
    29.831223,
    29.65505,
    30.261972,
    29.985171,
    29.654059,
    30.197857,
    30.222116,
    30.062544,
    30.23092,
    30.224509,
    30.176315,
    30.193621,
    30.211671,
    30.258212,
    30.161216,
    30.163154,
    30.191588,
    30.182908,
    30.218157,
    30.255321,
    30.211132,
    30.212257,
    30.222826,
    30.191711,
    30.1777,
    30.187077,
    30.197014,
    30.209539,
    30.190366,
    30.236736,
    30.217192,
    30.198722,
    30.192802,
    30.248453,
    30.18994,
    30.221592,
    30.166217,
    30.195851,
    30.217727,
    30.22965,
    30.191075,
    30.249018,
    30.232097,
    30.268542,
    30.190294,
    30.218866,
    30.229869,
    30.204445,
    30.232434,
    30.284991,
    30.209296,
    30.27161,
    30.274263,
    30.230185,
    30.288255,
    30.248009,
    30.254101,
    30.246737,
    30.188083,
    30.236213,
    30.237246,
    30.181824,
    30.171238
  ],
  "code_log": [
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200
  ],
  "code_map": {
    "200": 100
  }
}
```