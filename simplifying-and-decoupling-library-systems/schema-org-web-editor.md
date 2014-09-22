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

