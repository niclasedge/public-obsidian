parent: [[Python Skripte]]
tags:
aliases: 
Reference:[[Filesystem]]

---
# connect to sharepoint with python

Property: March 7, 2021 12:21 AM
Status: python

### Status:

- Verbindung zu sharepoint nicht möglich
- diverse optionen getestet
- keine zum laufen bekommen

[https://stackoverflow.com/questions/59979467/accessing-microsoft-sharepoint-files-and-data-using-python](https://stackoverflow.com/questions/59979467/accessing-microsoft-sharepoint-files-and-data-using-python)

pip install pysharepoint

```python
import pysharepoint as ps

sharepoint_base_url = 'https://<abc>.sharepoint.com/'
username = 'username'
password = 'password'

site = ps.SPInterface(sharepoint_base_url,username,password)

source_path = 'Shared Documents/Shared/<Location>'
sink_path = '/full_sink_path/'
filename = 'filename.ext'
sharepoint_site = 'https://<abc>.sharepoint.com/sites/<site_name>

site.download_file_sharepoint(source_path, sink_path,filename,sharepoint_site)
site.upload_file_sharepoint(source_path, sink_path,filename,sharepoint_site)
```