# ChemSteet

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)


Rendering Proteins and Molecules on AR

An ARKit iOS project for HackInOut 2017.

This is a code bump of scripts, services and IOS Project for HackInOut 2017 submission. Please ignore the shammy code commits.


### What does the App Do?

The App extracts chemical names from a large text in real-time and renders the molecules/proteins in an AR environment.

- Get real-time text from IOS camera.
- Find Chemical compounds/molecules/proteins from text.
  - Locally trained CoreML model + AbbyyRtrSDK.framework
  - Wit.AI for processing keywords/traits and extracting entitites
- Fetch the chemical name and search for information on ChemSpider
- The backend service takes a .MOL file containing the molecular data and renders into a 3D scene with OpenGL+PyMOL+MeshTool.
- The rendered .DAE (Collada) files are used to project Chemical formulae as an AR Scene.

### Demo Included

https://youtu.be/W6PZENy11IY

### Contents
mol_to_deb_service is a flask based service for processing extracted text and serving molecule data from ChalkSteet API -- 
https://vast-dusk-78988.herokuapp.com/process/?q=%22It%20reacts%20with%20hydroxyl%20radical%20(%E2%80%A2OH)%20to%20produce%20a%20radical%20intermediate%20%E2%80%A2HOCO,%20which%20transfers%20rapidly%20its%20radical%20hydrogen%20to%20O2%20to%20form%20peroxy%20radical%20(HO2%E2%80%A2)%20and%20carbon%20dioxide%20(CO2)%22


mol2dae.workflow is an OSX AppleScript to automate .mol to .dae conversion.


daes/ has all the extracted Daes files that can be rendered on AR.


Finally, (part of the) IOS Project is also enclosed.

The entity recognision models etc will be uploaded soon.

### TODO

Cleanup the project for contributions.
Make a better readme page.
