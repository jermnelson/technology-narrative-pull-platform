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
(Greenall, Koster 2014)

In this first iteration of the TIGER catalog , Greenall's and Koster's first two reasons
 for adopting Linked Open Data. The flexibility of using library Linked Data vocabularies
allowed Tutt Library staff to begin the exploring the potential of linked data as an library 
operational infrastructure for collecting and managing a library's collection. 

Part of the ingestion linked-data workflow for converting MARC21
records to BIBFRAME graphs leverages various local and national linked-data
sources like the Library of Congress, OCLC, DBPedia, among others, for enriching
and enhancing the existing graphs. This exemplar catalog demonstrates the concepts
and components in the Catalog Pull Platform by using the MARC-to-BIBFRAME
ingesters, converting  of the semantic server project and is based on the
design concepts articulated by Aaron Schmidt in a blog post (Schmidt, 2013). The
source code for the GPLv2 licensed catalog is available on Github at
<https://github.com/Tutt-Library/tiger-catalog>.

#### Build-Measure-Learn - Iteration One
The first public minimal viable product of the TIGER Catalog implemented a
native MARC21 semantic datastore using Redis, Solr, and MongoDB along with
limited BIBFRAME entity support. Tutt Library's MARC records were serialized
into JSON using pymarc (Summers, 2014) and then stored in MongoDB with search
being preformed through a Solr index of the MARC record, an approach borrowed
from existing Discovery layers as well as the Aristotle Discovery Layer. The
catalog was publicly released in April 2014 at <http://catalog.coloradocollge.edu>.


Measuring the usage of the catalog involved both custom code that saves query
information and what was returned from result set. Cover Art was harvested from
commercial sources and additional information from OpenLibrary record. Two sources
for data was the catalog itself through the use of Redis analytics datastore that
efficiently stored daily, monthly, and yearly usage of each MARC record through
the use of Redis bitstrings, a popular approach for using analytics in Redis[NEED SOURCE]
to store usage data. This data hinted at the potential that a library's catalog
could be more adaptive and responsive to a patron's information searches.

The main learning outcome for this first iteration was demonstrating the viability
of using modern NoSQL and web frameworks to build a working MARC21-based catalog
with a modern user interface. This iteration's support for BIBFRAME or other library
linked-data was minimal, mainly in providing supporting structures for the user
interface's cover art. This iteration also succeeded in evaluating the utility of
MongoDB's JSON document approach for data storage

#### Build-Measure-Learn - Iteration Two
The second iteration of the MVP is switching to Fedora4 as the primary data
storage technology while using Redis for caching, reporting, and analytics.
Content negotiation for RDF/XML, Turtle, and JSON-LD views of individual Works was
also developed as part of as well as a short survey for student and other public patrons
about their login and authentication choices. Also included in this iteration was
support for Google Analytics and more granular reporting structures.

Searching for iteration two switched from using Solr to Elastic Search, primarily
because supporting both BIBFRAME and Schema.org was easier in Elastic Search than in Solr.

