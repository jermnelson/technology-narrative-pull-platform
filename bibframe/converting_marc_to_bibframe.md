# Converting MARC record to BIBFRAME Fedora Objects

The first step in converting MARC records to BIBFRAME Fedora Objects is adding each MARC records as separate datastreams in a Fedora4 repository. In the first iteration of the MARC Fedora4 repository, each MARC fedora object RDFS label was the identification key from Colorado College's legacy integrated library system and was the only non-default triple to be stored with Fedora metadata.

The tool-chain for converting MARC 21 record to BIBFRAME RDF graphs in Fedora 4 is complicated and a good candidate to be streamlined and refactored in future iterations of the semantic server project. The current workflow to convert a MARC21 record to Fedora Object that stores the RDF BIBFRAME graph i:

1. A collection of MARC Records are parsed from a  MARC21 records into Python using Ed Summer's pymarc module.
2. Each MARC21 record is converted to MARCXML and sent to a separate socket serve that runs a simple service to convert MARCXML to BIBFRAME RDF XML file.
3. The BIBFRAME XML RDF file is parsed into a working graph in Python using rdflib.
4. The BIBFRAME graph is then decomposed into separate RDF graphs for each subject.
5. Finally, each subject's BIBFRAME RDF graph is saved to Fedora 4 using a REST API.

