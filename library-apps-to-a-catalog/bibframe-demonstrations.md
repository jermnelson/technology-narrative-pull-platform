## BIBFRAME Demonstrations

The first experiments with creating a BIBFRAME catalog started with using Django
 for the web front-end and the NoSQL Redis datastore to store information on 
BIBFRAME entities. An example of this minimum viable product of catalog is still 
accessible at <http://tuttdemo.coloradocollege.edu/> as a "discovery app" that 
borrowed the look of a commercial discovery layer. This BIBFRAME demonstration used 
three sources of records; MARC records from random selection of  libraries in the 
Colorado Alliance of Research Libraries consortium, MODS records harvested from Tutt 
Library's digital repository, and over 45,000 RDF XML records from Project Gutenberg. 
All three sources of records were converted to BIBFRAME key-values in Redis using custom 
Python code that made a lot of modeling and mapping assumptions that were changed or 
dropped as the BIBFRAME model and vocabulary matured.

These early experiments in creating bibliographic discovery layers and catalogs using 
Redis, BIBFRAME, and Django really illustrated to the Tutt Library about the problems 
with too closely coupled software in an environment of rapid changes in requirements 
and technology. By separating out the underlying data storage from the front-end 
application, the Catalog Pull Platform is better able to support different HTML and Native 
user interface frameworks and elements.

Following the Modeling BIBFRAME entities in Redis that gained traction with
the release of the formal BIBFRAME vocabulary at the first iteration of the
<http://bibframe.org> website. In early 2013, Nelson published another Code4Lib
article(Nelson, 2013), further describes a Redis-based bibliographic web
applications with designs for Linked Data peer-to-peer and consortia datastores.
At the 2013 Code4Lib conference in Chicago, Nelson co-presented on the current
status of his collaborative work with the University of Denver in a presentation
titled, Evolving Towards a Consortium BIBFRAME Redis Datastore, that further
detailed a multi-institutional BIBFRAME application design. Invited to present at
the BIBFRAME forum at annual ALA conference in the summer of 2012, we demonstrated
a consortium BIBFRAME discovery layer and catalog that included MARC records from
the member institutions of the Colorado Alliance of Research Libraries, all 40,000+
RDF/XML records from Project Gutenberg, and over 5,000 MODS records harvested from
Colorado College's Fedora 2.7 digital repository. 
