Terminologies, Concepts and Conventions
========================================

 .. warning::
    This section is under active development and is subject to change.


 .. note::
    These data standards, and the terminologies therein, are based on and heavily inspired by `HL7 FHIR <https://www.hl7.org/fhir/license.html#2.1.23>`_, which is made available using the `Creative Commons License <https://creativecommons.org/publicdomain/zero/1.0/>`_.
    
    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in `RFC 2119 <https://datatracker.ietf.org/doc/html/rfc2119>`_.


#. Data Types:
    #.  Using SQL-esque terminology - any dataset would be made of multiple tables. Each table has fields, or attributes, and often, these fields have a specific type. These are called data types.
    #. **Primitive Data Types**: These include things like boolean, string, float, int, and so on. Refer `here <https://hl7.org/fhir/datatypes.html#primitive>`_ for further details.
    #. **General Purpose Data Types**: These are slightly more complex data types - this could include date and time as per `ISO8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_, range of floating point variables, or codeable concepts, as defined below.
#. Terminology Bindings: 
    * Terminology Bindings are used a specific field is bound to a set of terminologies. This is also useful when there is no existing standard library to rely on - or the standard library is too limited for our purposes.
    * Gender is an example of a concept that is bound to terminologies. Similar to `HL7 FHIR's Administrative Gender <https://hl7.org/fhir/valueset-administrative-gender.html>`_, our standards use a similar set of options - ``female | male | other | unknown``. 
    * Terminology Bindings will also come into place when we are defining sample collection sites for environmental surveillance. For e.g., there may be a smaller Terminology Binding Set for FMD, where bird sanctuary sites might not be relevant.
    * A crucial example of an internally defined terminology binding - is user roles. Environmental Surveillance has a detailed supply chain, all the way from sample collection to delivery, processing, sequencing, and bioinformatics analysis. The different players here will have different roles and different levels of access to the various resources.
       .. note::
        The terminology binding for the list of roles is currently under development.
#. Codeable Concepts:
    * Codeable Concepts are used when existing public repositories or standards are used to create terminology binding sets.
    * The Indian Union Government's `LGD <https://lgd.gov.in>`_ for standard geospatial area codes at various resolutions is a good example of a codeable concept.
    * `WHO's ICD 11 Classification of Diseases <https://www.who.int/standards/classifications/classification-of-diseases>`_ is also a good example.
#. Resources
    * A resource is an entity that has a known value and contains a set of structured data complying with the definition of that resource within this documentation.
    * An example of a resource is a `User <../users.html>`_. Every user within an application developed using these standards, would be a row in a database entry that complies with the standards mentioned here.
    * Resources can be looked at as tables - each table has a data dictionary and a schema, and rule sets and terminology bindings to ensure inter-operability and data integrity.
    * Resources can link to each other, thereby reducing data duplication. For example, each entry in the table for the `Samples <samples.html>`_ resource will have a 'Sample Collector' - which need not mention all the details of the sample collector but simply their ID within the Users table.
    * All resources defined within ``dses`` have an entry for UUID (``User.uuid``, ``Sample.uuid``, and so on). All these uuids comply with the uuid4 specification mentioned in `RFC 4122 <https://www.ietf.org/rfc/rfc4122.txt>`_. All applications built on this spec SHALL use the uuid alone as the unique reference, regardless of any other unique alphanumeric ids available within the databases.
#. Flags and Attributes
    * TODO: (Camel Case. Conventions.) Categories and subcategories are for readability (for now).


      .. csv-table:: Flags
         :file: ../csvs/flag.csv
         :widths: 20,30,50
         :header-rows: 1
