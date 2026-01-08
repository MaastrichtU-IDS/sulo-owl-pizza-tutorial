---
layout: page
title: ESWC 2026 Tutorial
description: FAIR Ontology Engineering with SULO - ESWC 2026
---

# FAIR Ontology Engineering with SULO: An ESWC 2026 tutorial

## Overview
Designing high-quality ontologies that are Findable, Accessible, Interoperable, and Reusable (FAIR) remains a key challenge in
practice. This tutorial introduces a fully integrated workflow for principled ontology engineering based on the Simplified Upper Level Ontology
(SULO), a lightweight upper-level ontology designed to guide conceptual representation. Through a hands-on, end-to-end examples, participants
will (re)conceptualize, formalize, and automatically reason over the pizza domain using SULO design patterns in a notebook setting. Participants will use the OntoStart platform to
publish their own ontology in a FAIR manner. The tutorial is aimed at students, researhers, and practitioners building domain ontologies. Participants will
learn methodology and leave with a practical skills to bootstrap their own FAIR ontology projects.


## Objectives
This tutorial addresses a persistent gap in applied ontology: the absence of accessible,
end-to-end workflows for producing FAIR, modular, reusable ontologies
with high conceptual and engineering quality. The tutorial objectives are to:
* Introduce a coherent, end-to-end workflow for engineering FAIR and
principled OWL ontologies, from conceptualization to publication.
* Demonstrate the value of the Simplified Upper Level Ontology ([SULO](https://w3id.org/sulo/github)) as
an upper-level ontology to guide high-quality ontology representation
across domains.
* Showcase [OntoStart](https://github.com/micheldumontier/ontostart) as a practical framework for creating FAIR ontology
projects with automated versioning, documentation, and quality assessment.
* Contrast conceptual modeling and formal implementation, using
SULO patterns to motivate OWL axioms and ontology design decisions.
* Present complementary tooling ecosystems, including Protégé and
owlready2, for interactive and programmatic ontology development and reasoning.
* Extend the legendary OWL Pizza tutorial5 with a diversity of representational
problems (e.g. class/individual, identity, equivalence and disjointness,
spatial (containment and mereology) and processual (transformational,
developmental), qualities, quantities, roles and information objects through
concrete examples such as the classification of pizzas based on their toppings
and their qualitative and quantitative spicyness, the loss and gain of identity
in the making of dough, the roles played by individuals and devices in the
making and delivering of pizzas (SULO Pizza Tutorial)6.
* Empower participants to adopt reproducible, maintainable, and FAIR
engineering practice for their own ontology projects.

## Target Audience
The tutorial aims to balance theory with hands-on ontology engineering over the pizza domain. 
The tutorial is pitched at a basic to intermediate level; no
prior knowledge of upper level ontologies or OWL is required. Attendees that
have knowledge of python may choose to implement the tutorial with python,
otherwise attendees will be expected to run Protege.

## Learning goals
The learning goals of the tutorial are twofold:
1. Develop competency in the use of SULO to conceptualize and formalise a domain
* Explain the role of an upper-level ontology and apply SULO’s categories and design patterns to conceptualize a domain.
* Distinguish parts, features, roles, capabilities, processes, and quantities within a domain using SULO semantics.
* Formalize domain concepts in OWL, translating SULO-based conceptual models into logical axioms.
* Re-design the pizza ontology by applying SULO patterns in OWL for the pizza domain and validate them using tooling.

2. Publish and maintain ontology projects following FAIR practices
* Initialize a new FAIR ontology project using OntoStart, including metadata files, documentation structure, and CI-based quality checks.
* Use Protégé 7 to build, visualize, and test ontology class structures.
* Use owlready2 8 in Python to construct, manipulate, and reason over ontologies programmatically.
* interpret FOOPS! [2] FAIRness reports and identify steps to improve ontology FAIRness.



### 🕒 Schedule (May 10/11 2026)
A half-day tutorial with two components
*  SULO-based knowledge representation
*  Hands-on session to implement with Python (or Protege)

| Activity | Duration | Description | OWL constructs
| :--- | :--- |
| What is an ontology? | 15 min | 
| SULO in a nutshell | 45 min| Classes, Object and Data Properties, Datatypes, Literals, Property expressions (Object and Data Property), Data Ranges
| Declaration | 20 min | Entity Declarations (Class, Individual), Axioms (Subclass, Disjoint), Annotation Properties
| Composition | 20 min | Class Expression Exioms: Class Expressions, Propositional Connectives, Existential and Universal Quantification, Object Property Cardinality Restrictions (minimum, maximum, exact)
| Qualities | 15 min | 
| Quantities |
| Identity, transformation, and development | 20 min |  Individuals, Individual equality and inequality
| Spatial containment and movement | 20 min |
| Time | 20 min |
| OntoStart Deployment | 20 min | Ontology IRI, OWL Versioning, Ontology Annotations, OWL Syntaxes
| FAIRness assessment | 15 min |


### Speakers
Michel Dumontier is the Distinguished Professor of Data Science at Maastricht
University and co-founder of the Department of Advanced Computing
Sciences. He is a leading researcher in biomedical ontologies, knowledge graphs,
and Semantic Web technologies. He co-founded the FAIR principles, leads major
EU and US research initiatives, and has extensive experience teaching ontology
engineering, knowledge graphs, and Semantic Web technologies at undergruadate
and graduate level. He is a co-creator of SULO and created the ontostart
FAIR ontology template project.

Remzi Celebi is an Assistant Professor in the Department of Advanced Computing
Sciences at Maastricht University. His research focuses on semantic data
integration, biomedical ontologies, knowledge graphs, and machine learning methods
for health applications. Remzi is an experienced instructor and teaches
courses on semantic web, knowledge graphs, machine learning, and FAIR data
stewardship. He regularly supervises MSc and PhD students in ontology engineering,
data integration, and representation learning.

