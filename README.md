# Illegal Fishing Detection

## Project Overview

### Problem Area
Illegal, unreported, and unregulated (IUU) fishing is a significant global problem that threatens marine ecosystems, food security, and the livelihoods of people dependent on fishing. IUU fishing undermines efforts to sustainably manage fish stocks and combat overfishing.

### Data Science Solution
This project aims to develop a predictive model to identify illegal fishing activities by analyzing vessel behavior using AIS (Automatic Identification System) data and related datasets. By detecting anomalies and patterns indicative of illegal fishing, we can provide a tool for policymakers and fishery managers to take timely action.

### Impact
The proposed solution can help in:
- Protecting marine biodiversity by reducing illegal fishing activities.
- Supporting sustainable fisheries management.
- Enhancing the enforcement of fishing regulations.

## Built With

This section lists the major frameworks and libraries used to bootstrap the project:

* [![Python][Python.org]][Python-url]
* [![SQL][SQL.org]][SQL-url]
* [![NumPy][NumPy.org]][NumPy-url]
* [![Pandas][Pandas.pydata.org]][Pandas-url]
* [![Jupyter][Jupyter.org]][Jupyter-url]
* [![Tableau][Tableau.com]][Tableau-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Dataset Description
The project uses multiple datasets, including:

1. **Anonymized AIS Training Data:**
   - **Description:** Training dataset for detecting fishing events and gear type by analyzing AIS vessel tracks.
   - **Files:**
     - drifting_longlines.csv
     - fixed_gear.csv
     - pole_and_line.csv
     - purse_seines.csv
     - trawlers.csv
     - trollers.csv
     - unknown.csv
   - **Table Schema:**
     - `mmsi`: Anonymized vessel identifier
     - `timestamp`: Unix timestamp
     - `distance_from_shore`: Distance from shore (meters)
     - `distance_from_port`: Distance from port (meters)
     - `speed`: Vessel speed (knots)
     - `course`: Vessel course
     - `lat`: Latitude in decimal degrees
     - `lon`: Longitude in decimal degrees
     - `is_fishing`: Label indicating fishing activity
     - `source`: The training data batch

2. **Anchorages:**
   - **Description:** Global database of anchorage locations where vessels congregate.
   - **Files:**
     - named_anchorages_v2_20221206.csv
     - named_anchorages_v2_20201104.csv
     - named_anchorages_v1_20191205.csv
     - named_anchorages_v1_20181108.csv
   - **Table Schema:**
     - `s2id`: unique anchorage identifier
     - `lat`: latitude in decimal degrees
     - `lon`: longitude in decimal degrees
     - `label`: anchorage label (broader port label)
     - `sublabel`: anchorage sublabel (detailed anchorage label)
     - `label_source`: source of label
     - `iso3`: ISO3 code of the EEZ containing the anchorage
     - `distance_from_shore_m`: distance (meters) of the anchorage from shore
     - `drift_radius`: average drift radius (meters) of vessels at the anchorage
     - `dock`: is the anchorage located at a dock

3. **Welch et al. (2022) - Hotspots of Unseen Fishing Vessels:**
   - **Description:** Data on suspected AIS disabling events by commercial fishing vessels.
   - **Files:**
     - ais_disabling_events.csv
   - **Table Schema:**
     - `gap_id`: Unique id of the AIS disabling event
     - `mmsi`: Maritime Mobile Service Identity number
     - `vessel_class`: Geartype of the vessel
     - `flag`: Flag state (ISO3) of the vessel
     - `vessel_length_m`: Vessel length (meters)
     - `vessel_tonnage_gt`: Vessel tonnage (gross tons)
     - `gap_start_timestamp`: Time at the start of the AIS disabling event
     - `gap_start_lat`: Latitude at the start of the AIS disabling event
     - `gap_start_lon`: Longitude at the start of the AIS disabling event
     - `gap_start_distance_from_shore_m`: Distance from shore at the start of the AIS disabling event
     - `gap_end_timestamp`: Time at the end of the AIS disabling event
     - `gap_end_lat`: Latitude at the end of the AIS disabling event
     - `gap_end_lon`: Longitude at the end of the AIS disabling event
     - `gap_end_distance_from_shore_m`: Distance from shore at the end of the AIS disabling event
     - `gap_hours`: Duration of the AIS disabling event

4. **Fishing Effort:**
   - **Description:** Global datasets of AIS-based fishing effort and vessel presence.
   - **Files and Formats:**
     - Fishing effort by flag state and gear type at 100th degree resolution
     - Fishing effort by MMSI at 10th degree resolution
     - Fishing vessel format: fishing-vessels-v2.csv
   - **Table Schema (Example):**
     - `mmsi`: Maritime Mobile Service Identity number
     - `flag`: Flag state
     - `vessel_class`: Geartype of the vessel
     - `registry_vessel_class`: Registered vessel class
     - `inferred_vessel_class`: Inferred vessel class
     - `inferred_vessel_class_score`: Inferred vessel class score
     - `length_m`: Vessel length (meters)
     - `tonnage_gt`: Vessel tonnage (gross tons)
     - `engine_power_kw`: Engine power (kilowatts)
     - `active_[year]`: Activity status for each year

## Getting Started

### Prerequisites
- List any software, libraries, or tools required to work with the project.

### Installation
- Provide step-by-step instructions on how to set up the project locally.

### Usage
- Explain how to run the project, including any scripts or commands.

## Contributing
- Guidelines for contributing to the project.

## License
- Information about the project's license.

## Acknowledgements
- Acknowledge any individuals, organizations, or resources that contributed to the project.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python.org]: https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[SQL.org]: https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=PostgreSQL&logoColor=white
[SQL-url]: https://www.postgresql.org/
[NumPy.org]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=NumPy&logoColor=white
[NumPy-url]: https://numpy.org/
[Pandas.pydata.org]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=Pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Jupyter.org]: https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white
[Jupyter-url]: https://jupyter.org/
[Tableau.com]: https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white
[Tableau-url]: https://www.tableau.com/

r