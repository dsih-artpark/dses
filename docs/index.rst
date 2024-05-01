####################################################
Data Standards for Environmental Surveillance (dses)
####################################################

.. warning::
    These standards are currently in alpha (under active development) and might be changing. Check out our Github to see the latest changes.

This is the documentation for the data standards for environmental surveillance, developed by the Data Science Innovation Hub at `ARTPARK <https://www.artpark.in/>`_ at the `Indian Institute of Science <https://iisc.ac.in>`_.


Introduction: Why do we need Standards?
------------------------------------------

Environmental Surveillance has the capability to complement public health surveillance at the national and sub-national levels. At the moment, environmental surveillance research is largely fragmented across different groups across the world. Specifically, in India,
environmental surveillance is performed primarily by various research institutions who further deliver the results of their analyses to the relevant public health authority within the government. This involves the collection of various types of samples across various sites and locations. There are also various use-cases for the utilisation of this data.
For instance, environmental surveillance for SARS-CoV-2 was crucial in identifying Variants of Concern in waste-water before there was an outbreak. 
For animal diseases, it might be targetted to identify epidemics and guide vaccination strategies in endemic areas. 

Environmental Surveillance is also already existent in public health systems - in India and in various tropical countries - where there is a significant incidence of dengue. In India, for instance, there is a systematic government effort under the *National Vector Borne Disease Control Program* (NVBDCP) to identify breeding spots for *Aedes Aegypti* and *Aedes Albopictus*.
These breeding spots are systematically identified and eliminated, in programs commonly referred to together as *Source Reduction Activities*. 

There are various diseases of interest - animal diseases such as Foot-and-mouth Disease, Lumpy Skin Disease and Avian Influenza, and human diseases like COVID19, Influenza, and dengue. 
The goals for each environmental surveillance program might differ - but various policymakers turn to epidemiologists to engage in disease modelling using the results of environmental surveillance, the larger goal remaining an integrated environmental surveillance program within health ministries worldwide.
There is therefore a need for a consistent framework and data definitions, that will allow researchers to engage in disease modelling using data from various sites and groups. 
This will also allow tools and models to be extensible from one disease to another, which will prove crucial for similar diseases (for e.g. dengue, malaria, and chikungunya).

Principles
----------

Existing groups, such as the `Public Health Alliance for Genomic Epidemiology (pha4ge) <https://pha4ge.org>`_  are working to establish Data Structures for Genomic Epidemiology. 
The goal of this set of standards is to complement such efforts and create an extensible framework for the standards that can be used by any research group or public entity that intends to start working on genomic epidemiology and environmental surveillance.
Crucially, the efforts listed here are built to complement clinical surveillance, and eventually integrate with existing health surveillance systems at national and subnational levels, at scale.
The framework and standards we develop would need to comply with the following principles so we can solve the problems mentioned above:

#. **Fast and Easy to Adopt**: The standard would need to be constructed keeping different users in mind. For instance, the standard should be easy to adopt for a team of researchers collecting data on excel sheets, but should also allow fast development of applications for use at scale by public health authorities.
#. **Modular, Extensible, and Adaptable across Contexts**: The standard would need to be constructed to ensure that only the absolutely crucial aspects are mandatory, allowing for specific users to add modules of their own.  This is also to ensure that a standard that might work in one context are not enforced across contexts.  For instance, rather than enforcing an ontology for disease codes, we allow different users to use the ontology that makes the most sense in their context. For human diseases, the logical conclusion might be the `ICD <https://icd.who.int/en>`_ or `SNOMED CT <https://www.snomed.org/use-snomed-ct>`_. For animal diseases, this might reference the `Terrestrial Animal Health Code <https://www.woah.org/en/what-we-do/standards/codes-and-manuals/>`_, or rely on the standards being developed by the `Global Burden of Diseases and the OIE <https://bulletin.woah.org/?panorama=03-3-2021-1_aho>`_.
#. **Works well with existing standards**: The framework and standard would also attempt to ensure inter-operability with existing standards from the ground up. This will involve ensuring that the data can be converted to formats specified by the pha4ge, and also ensuring to use existing ontologies and standards. This could mean using ontologies like ICD/SNOMED/GBAD/OIE, as mentioned above. This could also mean creating country agnostic standards for administrative regions, and relying on country specific standards for administrative units within each country, while providing a base framework to aid uniform implementation.
#. **Public Domain and Open Source**: Crucially, this will also involve constructing these standards, from the ground up, in an open source manner, allowing members of the genomics, epidemiology, public health, and developer communities to contribute and provide feedback, and allow for researchers using the standards on the ground to provide real feedback, and extend the standards as they see fit for their own use case. This also involves constructing the standards in a manner that is friendly for both developers and non-developers to understand, implement, and provide feedback.


Approach
--------

When we get started with building our application to aid environmental surveillance efforts on the ground with a group of researchers, we turned to the `pha4ge <https://pha4ge.org>`_ standards to get started. They define a set of columns that are to be maintained, some optional, some mandatory, and some recommended.
Our approach to construct our framework and standards starts with the following steps:

#. Take the broader columns defined by pha4ge, and modularise these columns based on two primary criteria - who will collect/compute this information, and who will finally use this information. A sample might be collected on the field by a technician, who will log the sample collection site, and the barcode associated with the sample. They would also log the environmental conditions during sample collection. On the other end of the *environmental surveillance supply chain*, a bioinformatician might take all the relevant information provided by the sample collection technician, the molecular biologist, and the sequencing team, and use that information to conduct an analysis, perhaps engage in disease modelling. This step also includes defining the accepted datatypes for all data points that someone who uses our framework might use.
#. We then focus on making these columns friendly for developers and computer systems, and, crucially, understanding how these columns can be standardised. This includes tying them to any existing ontologies. For instance, as mentioned above, we would rely on the `Census of India <https://censusindia.gov.in/census.website/>`_ and the `Ministry of Panchayati Raj's LGD <https://lgd.gov.in>`_ for the names and codes of administrative units in India. We can rely on ISO standards for date, time, latitude and longitude, and country codes, and the WHO and OIE/GBAD for disease specific ontologies and codes. 

These steps can be likened to the first step being to create the larger framework and standards that can be used across contexts and diseases, and the second step can be likened to creating our very own implementation guide for this framework, similar to the approach taken by `FHIR HL7 <https://hl7.org/fhir/>`_.



Table of Contents
-----------------

.. toctree::
    :maxdepth: 2

    data_standards/index.md
    example.ipynb
    changelog.md
    contributing.md
    conduct.md

Contributing
-------------

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

Credits
-------------

Data Standards for Environmental Surveillance (`dses <https://github.com/dsih-artpark/dses>`_) was created with `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_ and the `py-pkgs-cookiecutter` `template <https://github.com/py-pkgs/py-pkgs-cookiecutter>`_. The documentation is rendered using `sphinx <https://www.sphinx-doc.org/>`_ and hosted on `readthedocs.io <https://readthedocs.io>`_, and uses `poetry <https://python-poetry.org/>`_ to manage dependencies in the rendering scripts.
