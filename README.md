# ChemSteet

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


Rendering Proteins and Molecules on AR

An ARKit iOS project for HackInOut 2017.

This is a code bump of scripts, services and IOS Project for HackInOut 2017 submission. Please ignore the shammy code commits.


## What does the App Do?

The App extracts chemical names from a large text in real-time and renders the molecules/proteins in an AR environment.

- Get real-time text from iOS camera using OCR module (AbbyyRtrSDK.framework).
- Find Chemical compounds/molecules/proteins from text from ML Modules.
  - Wit.AI for processing keywords/traits and extracting entities
  - Locally trained CoreML model instead of Wit.AI (TODO)
- Fetch the chemical name and search for information on ChemSpider 
- The backend service takes a .MOL file containing the molecular data and renders into a 3D scene with OpenGL+PyMOL+MeshTool.
- The rendered .DAE (Collada) files are used to project Chemical formulae on AR Scene (using ARKit) in iOS App.

## Demo link (YouTube)

[![Chemstreet](https://img.youtube.com/vi/W6PZENy11IY/0.jpg)](https://youtu.be/W6PZENy11IY)

## ChemSteet iOS App includes

### TextCapture module:
- `AVCaptureSession` is used for preview the iOS Camera layer for text recognition.
- Text recognition is done using [ABBYY Real-Time Recognition SDK](https://github.com/abbyysdk/RTR-SDK.iOS/). 
- On recognition of stable text input from camera & ABBYY SDK, locally it is processed for API request.
- API call for fetching list of chemical elements/molecules/proteins are obtained by Wit.AI backend which helps in mapping local DAE models for ARView.
- On selected chemical to view in AR, AR module is initialised for rendering local DAE model to display on ARView

### AR Module:
- Initialise `ARSCNView` with `ARWorldTrackingConfiguration` for rendering AR model (which in the form of DAE format) for the chemical chosen.
- `renderScene()` render's with geometrical orientation & rotation of the AR model which is mapped for chemical (DAE chemical model present locally in the asset).
- Additional information of the chemical model such as `average_mass, molecular_weight, molecular_formula & common_name` are displayed along the AR model in Scene using `SCNText`

## ChemSteet flask service includes
[`mol_to_deb_service`](https://vast-dusk-78988.herokuapp.com/process/?q=%22It%20reacts%20with%20hydroxyl%20radical%20(%E2%80%A2OH)%20to%20produce%20a%20radical%20intermediate%20%E2%80%A2HOCO,%20which%20transfers%20rapidly%20its%20radical%20hydrogen%20to%20O2%20to%20form%20peroxy%20radical%20(HO2%E2%80%A2)%20and%20carbon%20dioxide%20(CO2)%22) for processing extracted text and serving molecule data from ChalkSteet API.

`mol2dae.workflow` an OSX AppleScript to automate .mol to .dae conversion. (`daes/` has all the extracted Daes files that can be rendered on AR.)

## ChemStreet AI service includes

The entity recognition model etc will be uploaded soon.


## TODO

[ ] Cleanup the project for contributions.

[x] Make a better readme page.

### License and Copyrights

   Copyright [2017] [Sricharan Chiruvolu]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
