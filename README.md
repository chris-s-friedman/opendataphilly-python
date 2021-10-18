# opendataphilly-python

python utilities for interacting with OpenDataPhilly

To extract data from the 311 dataset:

```python
from odphilly_tools.extract_311 import *

# To extract 311 requests between June 1 and October 10 2021:
df = extract("2021-06-01", "2021-10-10")
```
