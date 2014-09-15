## Aristotle Library Apps

With the success of the Aristotle Discovery Layer built using Django and Solr,
the Tutt Library started examining other areas where the library could leverage
the same code base for other purposes. With mobile apps hype cycle cresting in
2012 and early 2013, we focused on an mobile apps for library services and resources
seems logical but overtime resulted in some technical decisions that was 
too much complex and confusing for users. Trying to duplicate a mobile app store
user interface for accessing small, individual library apps become too difficult to 
design and support for the extremely small development staff at Tutt Library.

While no longer being used for active development, the different branches of the 
Aristotle Library Apps are still being used on a daily basis by library staff.
Eventually, the plan is retire all of the public apps and aborb the internal
MARC Processing App into the ingestion functionality for new TIGER Catalog.  

### Call-Number App and Redis
The inspiration for call-number app, an embedded iframe widget
in the record detail view of the Aristotle Discovery Layer, was Stanford 
University's SearchWorks Discovery layer as outlined in a earlier article
for Code4Lib (Nelson, 2013). While the Call-Number app was initially success
in demonstrating the approach of normalizing and sorting a book's Library
of Congress Call Number, problems starting to become apparent with trying
to use Redis for the entire Tutt Library collection. In Redis, the entire
data store is loaded into Random Access Memory of the computer or virtual
machine, with periodic or activity-based save points to hard disk. After about
3/4 of Tutt Library's MARC records were loaded into Redis, we started running
into memory issues (the virtual machine had approximately 20 GB available) and
little budget or opportunity to add more RAM, alternative configurations were
explored including using multiple Redis hosts on different 
virtual machines and client-side sharding across a number of workstations 
in a Library computer instruction lab that ran Redis as backend process.

The additional code complexity and operational support for this Call-Number
App in particular, was helpful in exploring the operational capabilities of 
Redis as a primary bibliographic datastore but was eventually unsustainable
for continued support by the Tutt Library.
