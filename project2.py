from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint

# Setup
if not sys.warnoptions:
	warnings.simplefilter("ignore")
configuration = deepsecurity.Configuration()
configuration.host = 'https://cloudone.trendmicro.com/api'

# Authentication
configuration.api_key['api-secret-key'] = 'FA6321CE-DF1D-5C16-BB49-8B8B8300FAFD:69E9529F-1A3B-3E59-F24D-BD530A6AF277:Rucxf8cjJg5lNj9VCw8BAzGRZqzBFhw8P3O6hGxJmcw='

# Initialization
# Set Any Required Values
api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(configuration))
api_version = 'v1'
expand_options = deepsecurity.Expand()
expand_options.add(expand_options.none)
expand = expand_options.list()
overrides = False

try:
	api_response = api_instance.list_computers(api_version, expand=expand, overrides=overrides)
	pprint(api_response)
except ApiException as e:
	print("An exception occurred when calling ComputersApi.list_computers: %s\n" % e)

f= open ("project2.csv", "w")
f.write(str (api_response))
f.close()

