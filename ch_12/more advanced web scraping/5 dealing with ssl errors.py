import ssl
from urllib.request import urlopen
import certifi

# Define the custom CA bundle path
custom_ca_bundle_path = "C:\\Users\\marol\\Desktop\\projects\\repo\\shared-repo\\custom_ca_bundle_path\\cacert-2023-08-22.pem"

# Create an SSL context using the custom CA bundle
ssl_context = ssl.create_default_context(cafile=custom_ca_bundle_path)

# Use the SSL context when making the HTTPS request
url = "https://sha384.badssl.com/"
response = urlopen(url, context=ssl_context)