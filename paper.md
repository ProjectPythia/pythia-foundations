---
title: 'Pythia Foundations: A community learning resource for Python-based computing in the geosciences'
tags:
  - Python
#   - astronomy
#   - dynamics
#   - galactic dynamics
#   - milky way
authors:
  - name: Brian E. J. Rose
    orcid: 0000-0002-9961-3821
    affiliation: 1 # (Multiple affiliations must be quoted)
  - name: Robert R. Ford
    orcid: 0000-0001-5483-4965
    affiliation: 1
  - name: Anderson Banihirwe
    orcid: 0000-0001-6583-571X
    affiliation: 2
  - name: M. Drew Camron
    orcid: 0000-0001-7246-6502
    affiliation: 3
  - name: John Clyne
    orcid: 0000-0003-2788-9017
    affiliation: 4
  - name: Orhan Eroglu
    orcid: 0000-0003-3099-8775
    affiliation: 4
  - name: Katelyn FitzGerald
    orcid: 0000-0003-4184-1917
    affiliation: 4
  - name: Maxwell A. Grover
    orcid: 0000-0002-0370-8974
    affiliation: 5
  - name: Julia Kent
    orcid: 0000-0002-5611-8986
    affiliation: 4
  - name: Ryan May
    orcid: 0000-0003-2907-038X
    affiliation: 3
  - name: Kevin Paul
    orcid: 0000-0001-8155-8038
    affiliation: 6
  - name: Kevin R. Tyle
    orcid: 0000-0001-5249-9665
    affiliation: 1
  - name: Anissa Zacharias
    orcid: 0000-0002-2666-8493
    affiliation: 4
  - name: Author Without ORCID
    affiliation: 2
affiliations:
 - name: Department of Atmospheric and Environmental Sciences, University at Albany (State University of New York)
   index: 1
 - name: CarbonPlan
   index: 2
 - name: NSF Unidata, University Corporation for Atmospheric Research
   index: 3
 - name: Computational Information Systems Lab., NSF National Center for Atmospheric Research
   index: 4
 - name: Environmental Science Division, Argonne National Laboratory
   index: 5
 - name: NVIDIA Corporation
   index: 6
date: 26 June 2025
bibliography: paper.bib
---

# Summary

Pythia Foundations [1] is the flagship product of the first phase of Project Pythia [2], a broad community effort to build, house, share, and maintain high-quality learning resources for Python-based computing in the geosciences. Project Pythia’s central mission is to accelerate progress across the geosciences by reducing roadblocks to sharing technical knowledge, particularly related to scalable and reproducible data analysis in the cloud using the open-source Python software ecosystem. 

Pythia Foundations is a geoscience-flavored introduction to essential tools in the scientific Python ecosystem and Pangeo [3] stack (e.g., JupyterLab, NumPy [4], Matplotlib [5], Pandas [6], [7], Cartopy [8], Xarray [9], Dask [10]), plus environment management tools (conda), basics of version control (git), and effective use of GitHub as an technical communication platform (Figure 1). It is a community-owned executable textbook backed by computational resources for automated health-checking and interactive use. It covers the foundational knowledge that is needed to get started with Python in the computational geosciences, as well as to become an effective citizen-practitioner in key open geoscience software ecosystems. It is intended for anyone from undergraduate students through established geoscientists who are relatively new to working in Python. The book assumes a basic knowledge of programming concepts, but a brief "Quickstart" lesson highlights distinctive features of Python for users migrating from other languages.

A distinguishing feature of Pythia Foundations is its rigorous quality control and maintenance. All Python code and external web links are tested nightly, and book contents are kept up to date as the software ecosystem and data sources evolve. Users can run the examples with a “one click” launch into a dedicated cloud-based Binder service [11].

# Statement of Need
Today’s geoscientists require not only domain expertise but also proficiency with specialized software and high-level technical skills to effectively analyze, manipulate, and manage potentially vast volumes of digital data in a complex and ever-changing computing environment. The scientific Python ecosystem and the emergence of cloud computing have been game-changers for many, providing an abundance of open-source tools with wide ranging functionality. Ironically, however, this abundance is often untapped, and can be a source of great frustration. Scientists spend an inordinate amount of time pondering questions such as: Which tool or technology should I use? How do I use it? Can I trust it? Is it compatible with other tools in my workflow? Often, the answers are unclear, due to inadequate documentation or difficulty in finding relevant up-to-date working examples. The result is too much time spent navigating or avoiding technology—time that could have been spent productively doing science. Pythia Foundations fills this need by providing a trusted community-owned, web-accessible, geoscience-specific education and training resource for scientists and students at all career stages who want to know what tools to use and how to use them to explore their data. 

The Foundations book embodies the FAIR principles [12] that play a central role in open science. Findability is served by gathering geoscience-specific tutorials into a high-visibility community archive. Accessibility is served by our automated CI testing and integrated public binder. Tutorials and example code are largely Interoperable due to reliance on a common ecosystem of tools (e.g., NumPy and Xarray). Reusability is addressed through permissive licensing of book content and geoscience relevance of the examples, as well as our commitment to maintaining up-to-date working examples—an essential need in light of the widespread problem of rapid obsolescence of computational notebooks [13]. 

# Content, instructional design, and usage
The scope of Pythia Foundations is limited to tools and packages that are currently in broad use across multiple geoscience disciplines; packages tailored to more narrow scientific domains are not covered in Foundations but may be suitable for a Cookbook. The book outline was designed collaboratively by the core author team, informed by community feedback, and drawing on our substantial collective experience in teaching Python-based scientific workflows in classrooms, workshops, and outreach events.

The book is organized into two main sections: Foundational skills and Core Scientific Python packages (Figure 1). The foundational skills section covers “getting started” skills such as how to install Python and manage environments and how to run Python code in JupyterLab. There is also a set of tutorials on the use of GitHub and git for version control and collaboration on open source projects. The scope of this section was chosen with the specific goal of enabling users to contribute back to Pythia Foundations.

A template notebook and contribution guide is provided for new content, encouraging consistency of style and organization. Each chapter includes explicit prerequisites, references, and estimated learning time. The book is intended primarily for self-study and reference, backed by the interactive Binder or deployed on user machines following the detailed guidance in the book. From web-based metrics, Pythia Foundations served roughly 29,000 users in 111 countries during calendar year 2024. 

Subsets of the book contents have been modified and repackaged for various workshops and short courses. A few examples include the 2022 EarthCube-AMGeO Hackathon, the ERAD 2024 Open Radar Science Shortcourse [14], the Climatematch Academy international virtual summer school (annually since 2023), and in Spanish-language translation for a Colombian hydrometeorological workshop in 2023 [15]. Co-authors Rose and Tyle have integrated material from Foundations into the formal curriculum for several semester-length undergraduate and graduate level courses at the University at Albany. 

# Computational infrastructure
The book is deployed as an easy-to-navigate website using JupyterBook [16] and MyST-MD [17], including “one-click” Binder links to interactive versions of every chapter. It features complete reproducibility: source materials are stored in a GitHub repository as unexecuted Jupyter notebooks, and all content is recreated in a bespoke computational environment during nightly builds and whenever the book pages are re-rendered. A full preview of the executed and rendered book is created whenever a change is proposed via a Pull Request. Development of the novel notebook publishing infrastructure enabling this full reproducibility was driven by the Pythia team’s need to collaborate on a large computational document. The build-and-preview automation that our team developed while authoring Foundations is now in wide use by the community of Cookbook creators. The automation notably includes the ability to route notebook execution through the same Binder environment offered to users, guaranteeing that the output of the automated builds are identical to those that users see when running code examples interactively. 

# Future plans
Pythia Foundations is a living document and is receiving continuous updates [18] and improvements, both from the core author team and the broader community of user-contributors. On the content side, Project Pythia is simultaneously fostering a growing collection of more advanced and domain-specific tutorials in our crowd-sourced community Cookbook gallery, with explicit links to prerequisites from Foundations. We anticipate periodic reviews of the Cookbook collection to identify cross-cutting content that should be abstracted back to Foundations, e.g., common data access patterns or analysis workflows. 

The computational and publishing infrastructure for Foundations is also continuously evolving. As of this writing, Foundations and all other Pythia content has just undergone a significant refresh and upgrade with the migration to JupyterBook 2 which is based on the MyST-MD publishing engine [17]. Among the compelling new functionality unlocked by this transition is a rich content cross-referencing and embedding model that will enable more modular reuse and repacking of Foundations content tailored to specific courses or audiences. 

# Acknowledgements
The authors gratefully acknowledge support from the broad open geoscience communities of Project Pythia and Pangeo for their feedback, suggestions, pull requests, and enthusiasm. Development and maintenance of Pythia Foundations was supported by the U.S. National Science Foundation (NSF) awards 2026899, 2026863, 2324302, 2324303 and 2324304. The Pythia BinderHub is deployed on Jetstream2 [19] at Indiana University through allocations EES230007 and SEE240014 from the Advanced Cyberinfrastructure Coordination Ecosystem: Services & Support (ACCESS) program [20], which is supported by NSF grants 2138259, 2138286, 2138307, 2137603, and 2138296.

# References
