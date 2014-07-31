# Converting MARC records to BIBFRAME Fedora Objects

## Important Pivots in Iterative Development

The first experiments with creating a BIBFRAME catalog started with using Django for the web front-end and the NoSQL Redis datastore to store information on BIBFRAME entities. An example of this minimum viable product of catalog is still accessible at <http://tuttdemo.coloradocollege.edu/> as a "discovery app" borrowing the look of a commercial discovery layer with three sources of records; MARC records from random selection of  libraries in the Colorado Alliance of Research Libraries consortium, MODS records harvested from Tutt Library's digital repository, and over 45,000 RDF XML records from Project Gutenberg. All three sources of records were converted to BIBFRAME key-values in Redis using custom Python code that made a lot of modeling and mapping assumptions that were changed or dropped as the BIBFRAME model and vocabulary matured.

Redis to MongoDB to Fedora 4

## Current MARC-to-BIBFRAME Process

The first step in converting MARC records to BIBFRAME Fedora Objects is adding each MARC records as separate datastreams in a Fedora4 repository. In the first iteration of the MARC Fedora4 repository, each MARC fedora object RDFS label was the identification key from Colorado College's legacy integrated library system and was the only non-default triple to be stored with Fedora metadata.

The tool-chain for converting MARC 21 record to BIBFRAME RDF graphs in Fedora 4 is complicated and a good candidate to be streamlined and re-factored in future iterations of the semantic server project. The current workflow to convert a MARC21 record to Fedora Object that stores the RDF BIBFRAME graph as triples associated with the object:

1. A collection of MARC Records are parsed from a  MARC21 records into Python using Ed Summer's pymarc module.
2. Each MARC21 record is converted to MARCXML and sent to a separate socket serve that runs a simple service to convert MARCXML to BIBFRAME RDF XML file.
3. The BIBFRAME XML RDF file is parsed into a working graph in Python using rdflib.
4. The BIBFRAME graph is then decomposed into separate RDF graphs for each subject.
5. Finally, each subject's BIBFRAME RDF graph is saved to Fedora 4 using a REST API.

There a number of issues with this multiple-step process, starting with the slow conversion process that even at its best, only converts a few hundred MARC records per minute.
The second issue is that the current MARC-to-BIBFRAME conversion produces a large number of RDF graphs per MARC record (anywhere from 30-70) that requires a primitive de-duplication service using Fedora 4 SPARQL queries on the existing BIBFRAME Fedora object's authorizedAccessPoint, name, or RDF label.

The next iteration of this tool will look at extending existing Fedora 4 functionality so that the entire conversion process from MARC21 to BIBFRAME RDF graphs occurs within a native Java process in Fedora.
