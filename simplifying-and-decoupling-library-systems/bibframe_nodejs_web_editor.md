### BIBFRAME node.js web editor

In May of 2014, the Library of Congress released a web-based editor for creating new RDF graphs of BIBFRAME entities as a Github repository at <https://github.com/lcnetdev/bfe/>. The author contributed a node.js web server that was extended so that librarians, staff, volunteers, and interested patrons could create new BIBFRAME RDF graphs as Fedora objects.

The node.js BIBFRAME editor uses the extensive REST web services now available in Fedora 4 to connect and save the JSON linked data output created in the BIBFRAME editor. The BIBFRAME web editor allows an individual to create/edit multiple BIBFRAME entities and then associate those entities with the main Work and Instance graphs that describe the artifact being cataloged. Currently the web editor requires configuration information to be hard-coded into the HTML template but the mechanism is in place but not yet fully implemented to provide different profiles for different types of materials and workflows.

There are a number of challenges that remain before the BIBFRAME editor will work as expected with Fedora 4 including the loading of existing BIBFRAME RDF graphs from Fedora 4 into the BIBFRAME editor.
