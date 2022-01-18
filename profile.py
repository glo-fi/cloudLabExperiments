"""
Basic Geni-lib example

Goal: Get Apache running via this scripting interface.
"""


# import portal object

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request Obect to start building the rspec
request = portal.context.makeRequestRSpec()

# Add a RawPC named node to the request
node0 = request.RawPC("node0") # User
node1 = request.RawPC("node1") # Apache

node1.disk_image = "urn:publicid:IDN+utah.cloudlab.us+image+noplab-PG0:small-lan.node1"

# Create Link Between Them
link1 = request.Link(members = [node0, node1])

# Write the request in rspec format
node1.addService(rspec.Execute(shell="bash", command='sudo /usr/local/apache2/bin/apachectl'))
node0.addService(rspec.Execute(shell="bash", command='sudo /local/repository/generateData.sh'))
portal.context.printRequestRSpec()
