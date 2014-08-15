### TIGER Catalog
The [TIGER](http://catalog.coloradocollege.edu/) catalog is the iterative developed minimum viable product that produces BIBFRAME and Schema.org descriptive RDF graphs of Colorado College's intellectual and culture artifacts being purchased, created, remixed, or donated. Part of the ingestion workflow of converting MARC21 records to BIBFRAME graphs leverages various local and national authority bodies like the Library of Congress, OCLC, DBPedia, and other Linked Data sources. This exemplar catalog demonstrates the concepts and components in the Catalog Pull Platform by using the MARC-to-BIBFRAME ingesters of the semantic server project and is based on the design concepts articulated by Aaron Schmidt in a blog post (Schmidt, 2013). The source code for the GPLv2 licensed catalog is available on Github at <https://github.com/jermnelson/tiger-catalog>.

#### Build-Measure-Learn - Iteration One
The first public minimal viable product of the TIGER Catalog implementing a native MARC21 semantic datastore using Redis, Solr, and MongoDB along with limited BIBFRAME entity support. The catalog was publicly released in April 2014 at <http://catalog.coloradocollge.edu>.

Measuring the usage of the catalog involved both custom code that saves query information and what was returned from result set. Cover Art was harvested from commerical sources and additional information from OpenLibrary records of these Works was harvested as well.

#### Build-Measure-Learn - Iteration Two
The second public iteration of the MVP is switching to Fedora4 as the primary data storage technology while using Redis and MongoDB for caching, reporting, and analytics. Content negotiation for RDF/XML, Turtle, and JSON-LD views of individual Works was also developed as well as a short survey for student and other public patrons about their login and authentication choices. Also included in this iteration was support for Google Analytics and more granular reporting structures.

Searching for iteration two switched from using Solr to Elastic Search, primarily because supporting both BIBFRAME and Schema.org was easier in Elastic Search than in Solr.
