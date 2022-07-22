from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

site_url = "http://operations.connect.na.local/support/Reliability/IKOHawkesbury"
ctx = ClientContext(site_url).with_user_credentials("IKOBRAM\hannsyed", "Roofing1SH", allow_ntlm=True)
web = ctx.web
ctx.load(web)
ctx.execute_query()
print("Web title: {0}".format(web.properties['Title'])) 

import os
import tempfile

from office365.sharepoint.client_context import ClientContext
ctx = ClientContext("http://operations.connect.na.local").with_user_credentials("IKOBRAM\hannsyed", "Roofing1SH", allow_ntlm=True)
# file_url = '/sites/team/Shared Documents/big_buck_bunny.mp4'
file_url = "/support/Reliability/IKOHawkesbury/HawkesburyAssetDocuments/(M11300-2000) Carriage Frame CTL Cutter.pdf"
download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(file_url))
with open(download_path, "wb") as local_file:
    file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
    #file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
print("[Ok] file has been downloaded into: {0}".format(download_path))