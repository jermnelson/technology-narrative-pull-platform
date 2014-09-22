# A Technological Narrative of a Library Catalog

The library's catalog, usually the core of what is called the library's integrated library 
systems and now being marketed as "library services platform" (Breeding 2012), 
touches most areas of the library's operations, collections, and public services. 
The functionality needed to support acquisition and circulation work-flows 
- not mention the increasingly complex electronic resource management for 
journals and e-books - traditionally requires these large enterprise software systems to include 
all this functionality into large monolithic "black-boxes". 

In the Spring 2014 issue of Reference and User Services Quarterly, Diane Cmor
and Rory Litwin argue if libraries should keep the traditional library OPAC in
favor of discovery systems or what Athena Hoeppner describes as "web-scale
discovery services" (Hoeppner 2012). Cmor's position, that because library
patrons prefer to using discovery systems to the traditional OPAC for finding
the library's materials, the added costs of maintaining two separate systems argue
in favor of dropping or eliminating the traditional library ILS/OPAC or catalog.
Litwin's counter-argument for retaining the traditional catalog revolve around
the catalog's utility for advanced searching by scholars and experts is better for
their specific information needs than the current crop of discovery systems that
focus on the general undergraduate at a academic library.(Cmor and Litwin 2014)

Although that might not have been the intentions of either Cmor or Litwin in
their debate on retiring the library catalog, there is another alternative to
what either of them suggest for library catalog. Instead of purchasing a commercial
discovery system or deploying one of the open-source discovery layer alternatives,
libraries should consider if their rate-of-return on their technology investment
for resource discovery would be better spent through online adverting of their
collections on the major commercial general search like Google or Microsoft
Bing. This radical approach has already been investigated by libraries as 
Utrecht University Library, where their student patrons start their search 
83% of the time from a search engine with under 1% using a online databases and
the library website. (Kortekaas 2012)  

With such library
luminaries as Roy Tennent calling for the demotion of the library catalog by
encouraging libraries to
"Take that anachronistic library catalog and turn it back into what it really
only ever was - an inventory control system." (Tennent 2014) or as Diane Cmor
says "Obviously, we still need  back-end catalogs (or the equivalent) to feed
our holdings into our discovery systems, but the user interface
is no longer necessary." (Cmor and Litwin 2014)  Lacking from these
analysis is that poor user interface for backend enterprise
systems, even stripped down to bare functionality as envisioned by Tennent and Cmor, 
have real and significant costs that are borne by library staff and administration 
when trying to accomplish their workflow in the library.  

Considering that library catalog primary purpose has been for
patrons, librarians, and staff to access or "discovery" materials in the in the
institution's collections; an important belief of Tutt Library is that the library catalog is a 
core operational and intellectual asset of the library. Over the past four years,
the Tutt Library at Colorado College has been actively building open-source software 
services for public and internal use by librarians and staff. Starting off 
with dual development of a Discovery Layer, a Solr-index of the library's MARC records, 
and a submission form for Colorado College senior student to self-ingest
their senior thesis to the library's digital repository, the Tutt Library 
expanded its efforts to 
building tools that 
connect legacy and current systems with the people that need information or 
services. The Tutt Library also starting exploring existing bibliographic 
models like FRBR and its RDA descendants to emerging Linked-Data based vocabularies 
such as BIBFRAME and schema.org and how these standards can be used with 
popular NoSQL technologies like Redis and MongoDB.

The library software development philosophy at Colorado College 
centers around creating simple, standalone web applications with minimal 
external dependencies. Some of these applications replaces lengthly manual 
MARC-based workflows for normalizing MARC records for Tutt Library's legacy
ILS along with the indexing into the Aristotle Discovery Layer. Other Fedora-based 
institutional repository utilities including staff productivity tools that allowed
repository managers to easy move collections around in Fedora as well as batch
templates that added one to any number of stub Fedora objects that shared similar
metadata and were all co-located in the same collection. These linked-data vocabularies
were also examined to see they could be used for 
operational improvement of library services and expansion of access to the 
library's patrons. This philosophy  offers loosely coupled components for rapid,
iterative, Lean Startup inspired (Ries 2012) Build-Measure-Learn software development 
cycles for Colorado
College's linked data research, experiments, and digital services. The
highest profile project is a new catalog with a Fedora 4 and Flask-based
semantic server made up of Colorado College's MARC records that have been
converted to BIBFRAME and Schema.org linked data.

This article will trace the development history of library systems at Tutt Library, 
starting from Discovery Layer, to tigthly-coupled Django-based web applications, to 
more fluid and flexibly platform approach that loosely connects applications based 
on Linked Data and common web practices that resulted the growing realization of 
the potential for libraries to expanded their services and become first-class citizens
in the Semantic web with operational tools that support and enhance a new vision of
the library catalog. 

## Starting with Aristotle Discovery Layer 
In the Spring 2011 work began on a forked copy of the  Django-based
[Kochief](https://code.google.com/p/kochief/) repository that eventually
became the [Aristotle Discovery Layer](https://github.com/jermnelson/Discover-Aristotle) 
that was also heavily influenced by the [Blacklight](http://projectblacklight.org/) 
project. The user interface for the Discover Layer was initially created by 
White Whale Web Services, a higher education design firm, as part of a general new
website design for the entire campus while the backend search index uses Solr, a common
implementation choice for both open-source and commercial discovery services. 

<img src="/static/img/aristotle-discovery-layer.png" width="640" height="480px">

*Screen shot from Aristotle Discovery Layer at <http://discovery.coloradocollege.edu>.* 

In the sixteen criteria Rider University Libraries used to evaluate Discovery 
Tools, Aristotle Discovery Layer still meets at least a portion 
10/16 of the criteria including <em>State-of-the-art web interface</em>, 
<em>Enriched Content</em>, <em>Faceted navigation</em>, <em>Persistent links.</em>,
and <em>Mobile compatibility.</em>(Chickering and Yang 2014) despite not being actively 
improved since 2013.

## CCETD Application and Aristotle Library Apps
The most visible and actively developed application built and supported by
Tutt Library is a web-based authentication and form submission for senior
and master students at Colorado College to self-submit their final thesis,
portfolio, or project to the library's digital repository. The first
iteration was a rough proof-of-concept that displayed a simple form that 
was demonstrated to Colorado College Business and Economic professor at an
departmental meeting in the fall of 2011. Based on their feedback, an early 
prototype was built to use the same Django environment as Aristotle Discovery
Layer that was later upgraded to currently use the Aristotle Library Apps 
environment.

<img src="/static/img/ccetd-2013-2014.png" width="640" height="480px">

*Screenshot from 2013-2014 iteration of the CCETD App*

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

## MARC Batch and Fedora Utilities

Like many libraries, Tutt Library's shift in collection activity from paper
journals to electronic journals continued with more vendors and databases
offering more online resources. One method for improving access to these
resources, and an increasingly larger percentage of ebooks, was that the
library was manually manipulating the MARC records provided by vendors.
While the macro capabilities of alternatives like MARCEdit could have
worked, we decided instead to create a web app that would allow library
staff to upload the vendor MARC record, automatically normalize the MARC
fields to the Tutt Library and Consortium standards for MARC records, and
then download the resulting modified MARC records to the staff's local
workstation that can then be imported into the Tutt Library's legacy ILS.

Tutt Library's digital repository is part of the Colorado Alliance of
Research Library's consortium digital repository service that uses Islandora
and Fedora. The Fedora Utilities App provided a couple of tools for library
staff to accomplish tasks that were extremely time-consoming in the old version
of Islandora (moving an entire collection of objects from one collection to
another) or difficult (create stub records of common metadata for an entire collection
of Fedora Objects).

<img src="/static/img/ala-fedora-utilities.png" width="640px" height="480px">

*Screen shot of active Fedora Utilities App*

## BIBFRAME Demonstrations

The first experiments with creating a BIBFRAME catalog started with using Django
 for the web front-end and the NoSQL Redis datastore to store information on 
BIBFRAME entities. An example of this minimum viable product of catalog is still 
accessible at <http://tuttdemo.coloradocollege.edu/> as a "discovery app" that 
borrowed the look of a commercial discovery layer as shown in this screen-shot:

<img src="/static/img/tuttdemo-prospector.png" width="640px" height="480px">

*Screenshot from <http://tuttdemo.coloradocollege.edu/>*
 
This BIBFRAME demonstration used 
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

# Simplifying and De-coupling Library Technology

Inspired by John Hegel III's and John Seely Brown's early conception a pull 
platforms, the Tutt Library has embarked on approach for library catalog
software development that emphasis emergent design, loosely coupled, 
people focused with incremental cycles that provide immediate feedback from
the end users of these services (Hegal II and Brown 2008). The current
technical infrastructure includes open-source projects like Fedora Commons
and Elastic search for RDF and datastream management and search functionality
while supporting existing MARC21 works and newer command-line and web-based
tools for manipulating RDF graphs of BIBFRAME and schema.org vocabularies. This
infrastructure is illustrated below:

<img src="/static/img/cpp-components.svg">

This simplifying process will eventually center around using Fedora 4 as both a
replacement for the MARC-based ILS through direct datastream management of the
exported MARC records at Tutt Library while also directly supporting the ingestion
and use of BIBFRAME and Schema.org triples for Tutt Library's creative works. 
To maximize utility and leverage the wide adoption of JSON, JSON linked data 
representations of these creative works are published and consumed between the 
front-end web applications, Fedora, and Elastic Search using JSON-LD serializations
from Fedora, represented in the above graph as bi-directional maroon arrows. 

Four projects so far use this new infrastructure, TIGER Catalog, BIBFRAME Editor,
MARC-to-BIBFRAME Conversion, and Schema.org web editor, all of which will be
explained in more depth below. 

## Reimagining the TIGER Catalog

The [TIGER](http://catalog.coloradocollege.edu/) catalog is the iterative
developed, minimum viable product, that consumes and publishes BIBFRAME and
Schema.org descriptive RDF graphs of Colorado College's intellectual and culture
artifacts. In their article on library Linked Open Data in implementing 
systems, Rurik Greenall and Lukas Koster list three reasons why libraries may 
adopt Linked Open Data:

* Exposing or publishing their own data as Linked Open Data for other organizations and individuals to consume.
* Consuming and re-using Linked Open Data from external sources as a way to enrich and enhance their own data
* Using Linked Open Data for a "completely new vendor-independent, Web-based
infrastructure and workflow for cataloguing"
(Greenall and Koster 2014)

In this first iteration of the TIGER catalog uses Greenall's and Koster's first two reasons
for adopting Linked Open Data as a broad design goals.  
The front-end user interface is based on the
design concepts articulated by Aaron Schmidt in a blog post (Schmidt, 2013) and uses
Bootstrap, Knockout.js, and jQuery with the server implemented using the Python 
web microframework Flask. The
source code for the GPLv2 licensed catalog is available on Github at
<https://github.com/Tutt-Library/tiger-catalog>.

#### Build-Measure-Learn - Iteration One

<img src="/static/img/tiger-catalog-iteration-1.png" width="640px" height="480px">

*Screenshot from <http://catalog.coloradocollege.edu/>*

The first public minimal viable product of the TIGER Catalog implemented a
native MARC21 semantic datastore using Redis, Solr, and MongoDB along with
limited BIBFRAME entity support. Tutt Library's MARC records were serialized
into JSON using pymarc and then stored in MongoDB with search
being preformed through a Solr index of the MARC record, an approach borrowed
from existing Discovery layers as well as the Aristotle Discovery Layer. The
catalog was publicly released in April 2014 at <http://catalog.coloradocollge.edu>.

Measuring the usage of the catalog involved both custom code that saves query
information and what was returned from result set. Cover Art was harvested from
commercial sources and additional information from OpenLibrary record. Two sources
for data was the catalog itself through the use of Redis analytics datastore that
efficiently stored daily, monthly, and yearly usage of each MARC record through
the use of Redis bitstrings, a popular approach for using analytics in Redis 
(Avichal 2011)
to store usage data. This data hinted at the potential that a library's catalog
could be more adaptive and responsive to a patron's information searches.

The main learning outcome for this first iteration was demonstrating the viability
of using modern NoSQL and web frameworks to build a working MARC21-based catalog
with a modern user interface. This iteration's support for BIBFRAME or other library
linked-data was minimal, mainly in providing supporting structures for the user
interface's cover art. This iteration also succeeded in evaluating the utility of
MongoDB's JSON document approach for data storage.

#### Build-Measure-Learn - Iteration Two
The second iteration of the MVP is switching to Fedora4 as the primary data
storage technology while using Redis for caching, reporting, and analytics.
Content negotiation for RDF/XML, Turtle, and JSON-LD views of individual Works was
also developed as part of as well as a short survey for student and other public patrons
about their login and authentication choices. Also included in this iteration was
support for Google Analytics and more granular reporting structures.

Searching for iteration two switched from using Solr to Elastic Search, primarily
because supporting both BIBFRAME and Schema.org was easier in Elastic Search than in Solr.
With Elastic Search storing JSON documents, a serialized version of BIBFRAME and Schema.org
in JSON is easily re-purposed as Elastic Search documents for indexing.

The first step in converting MARC records to BIBFRAME Fedora Objects is adding each 
MARC records as a separate datastreams for a in a Fedora4 repository. In the first iteration 
of the MARC Fedora4 repository, each MARC fedora object RDFS label was the identification 
key from Colorado College's integrated library system and was the only non-default triple 
to be stored with Fedora metadata for that MARC21 datastream.

The tool-chain for converting MARC 21 record to BIBFRAME RDF graphs in Fedora 4 is 
complicated and a good candidate to be streamlined and re-factored in future iterations. 
The current workflow to convert a MARC21 record to Fedora Object with RDF BIBFRAME graph as 
triples associated with the object:

1. A collection of MARC Records are parsed from a MARC21 records into Python using Ed Summer's pymarc module.
2. Each MARC21 record is converted to MARCXML and sent to a separate socket serve that runs a simple service to convert MARCXML to BIBFRAME RDF XML file.
3. The BIBFRAME XML RDF file is parsed into a working graph in Python using rdflib.
4. The BIBFRAME graph is then decomposed into separate RDF graphs for each subject.
5. Finally, each subject's BIBFRAME RDF graph is saved to Fedora 4 using a REST API.

There a number of issues with this multiple-step process, starting with the slow 
conversion process that even at its best, only converts a few hundred MARC records per minute.
The second issue is that the current MARC-to-BIBFRAME conversion produces a large number of 
RDF graphs per MARC record (anywhere from 30-70) that requires a primitive de-duplication service 
using Fedora 4 SPARQL queries on the existing BIBFRAME Fedora object's authorizedAccessPoint, name, or RDF label.

The next iteration of this tool will look at extending existing Fedora 4 functionality so that the 
entire conversion process from MARC21 to BIBFRAME RDF graphs occurs within a native Java process in Fedora.

### BIBFRAME node.js web editor

In May of 2014, the Library of Congress released a web-based editor for creating 
new RDF graphs of BIBFRAME entities as a Github repository at <https://github.com/lcnetdev/bfe/>. 
The author contributed a node.js web server that was extended so that librarians, staff, 
volunteers, and interested patrons could create new BIBFRAME RDF graphs as Fedora objects. The
forked BIBFRAME editor is available at <https://github.com/jermnelson/bfe>/

The node.js BIBFRAME editor uses the extensive REST web services now available in Fedora 4 
to connect and save the JSON linked data output created in the BIBFRAME editor. The 
BIBFRAME web editor allows an individual to create/edit multiple BIBFRAME entities and then 
associate those entities with the main Work and Instance graphs that describe the artifact being cataloged. 
Currently the web editor requires configuration information to be hard-coded into the HTML 
template but the mechanism is in place but not yet fully implemented to provide different 
profiles for different types of materials and workflows.

There are a number of challenges that remain before the BIBFRAME editor will work as expected with 
Fedora 4 including the loading of existing BIBFRAME RDF graphs from Fedora 4 into the BIBFRAME editor.

### Schema.org Web Editor
The [Schema.org](http://schema.org/) web editor is an open-source Flask-based 
application that provides a dynamic HTML5 user interface for manipulating Fedora4 
objects as schema.org RDF graphs. Schema.org is an linked-data vocabulary for 
describing resources on the web and is an joint effort by major commercial 
search engines like Google, Microsoft Bing, Yahoo!, and Yandex. (schema.org, 2014).

The schema.org editor, source code available at <https://github.com/jermnelson/schema-org-editor> 
under the MIT open-source license, is an experiment to see if a lightweight web editor could be 
built primarily with client-side javascript that dynamically generates the form elements for each 
schema.org class using a OWL RDF file that is loaded at the beginning of every session. The server 
backend, is a relative small Flask web application that responds to AJAX requests come from the web client.

<img src="/static/img/schema-org-editor.png" width="640px" height="480px">

*Screenshot from Schema.org Web Editor using local running Fedora 4 Instance*


## Concluding Thoughts

This development process of normalizing and creating conventions to support the varied
needs of a small academic library is an exciting opportunity. Given the wide
changes in how libraries need to communicate their stewardship of 
traditional and beautiful physical collections with the new mediums of
increasingly blurring
borders between the digital and physical creations, the library catalog needs to
evolve and change to meet these challenges. The evolutionary nature of bibliographic systems
is illustrated by Tutt Library as a microcosm of larger changes in the library technology as 
we move from a MARC-based discovery to richer linked-data bibliographic systems that can 
meet the many challenges of a networked world with increasingly melded and mashed-up creative works
created and access by our communities.

## References
Bibliography: A Bibliographic Framework for the Digital Age. Washington (DC): Library of Congress. Accessed at <http://www.loc.gov/bibframe/news/framework-103111.html>

Bibliography: Avichal. 2011. Fast, Easy, Realtime Metrics Using Redis Bitmaps. Accessed at <http://blog.getspool.com/2011/11/29/fast-easy-realtime-metrics-using-redis-bitmaps/> 

Bibliography: Breeding, M. 2012. Automation Marketplace 2012: Agents of Change. Accessed at <http://www.thedigitalshift.com/2012/03/ils/automation-marketplace-2012-agents-of-change/>

Bibliography: Chickering, W. Yang, S. 2014. Evaluation and Comparison of Discovery Tools: An Update. Information Technology & Libraries. 33(2):5-30.

Bibliography: Cmor, D. Litwin, R. 2014. Should we retire the catalog? Reference & User Services Quarterly; Spring2014, 53(3):213-216.

Bibliography: Dempsey, L. 2012. Two things prompted by a new website: space as a service and full library discovery. Accessed at <http://orweblog.oclc.org/archives/002202.html>

Bibliography: Greenall, R. Koster, L. 2014. An unbroken chain: approaches to implementing Linked Open Data in libraries; comparing local, open-source, collaborative and commercial systems. Accessed at <http://ifla2014-satdata.bnf.fr/pdf/iflalld2014_submission_Koster_Greenall.pdf>

Bibliography: Hagel, J. Brown, J. Davison, L. 2010. The power of pull: How small moves, smartly made, can set big things in motion. New York (NY): Basic Books.

Bibliography:  Kortekaas, S. 2012. Thinking the unthinkable: a library without a catalogue - Reconsidering the future of discovery tools for Utrecht University library.
LIBER General Annual Conference. Accessed at <http://libereurope.eu/news/thinking-the-unthinkable-a-library-without-a-catalogue-reconsidering-the-future-of-discovery-tools-for-utrecht-university-library/>

Bibliography: Ries, E. 2011. The Lean Startup. New York (NY): Crown Business. p. 294.

Bibliography: Schreur, P. 2014. AV Modeling Study. Accessed at <http://listserv.loc.gov/cgi-bin/wa?A2=ind1408&L=bibframe&T=0&P=9316>.

Bibliography: Schmidt, A. 2013. Catalog by Design. Accessed at <http://www.walkingpaper.org/5979>

