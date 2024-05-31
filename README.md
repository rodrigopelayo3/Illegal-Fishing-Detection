# Illegal Fishing Detection

## Project Overview

### Problem Area

Since I was young, I have always been passionate about nature. I spent as much time as possible outdoors, whether in the mountains or out on the ocean. , I particularly enjoy spearfishing, which gives me an adrenaline rush from catching my own food. As a fisherman and environment enthusiast, I've recently become aware of the significant issue of overfishing and decided to research it further. I discovered that illegal, unreported, and unregulated (IUU) fishing is a major global problem.

IUU fishing violates international fishing regulations and is difficult to monitor and control due to the ocean inmensity. This type of fishing, especially using nets that catch all types of species without mercy, has severe environmental impacts and threatens the socioeconomic stability of many regions across the globe. Developing countries that rely on fishing for food security and economic stability are particularly affected, with annual economic losses estimated at around $34 billion globally due to IUU fishing. The ecosystems, the economy and the species are endangered by these activities, which can also be linked to other illegal practices.

To better understand IUU fishing:
- **Illegal fishing** involves activities that violate applicable laws and regulations.
- **Unreported fishing** includes activities that are not reported or are misreported to relevant authorities, violating national laws and regulations.
- **Unregulated fishing** occurs in areas or for fish stocks without applicable conservation or management measures, conducted in a manner inconsistent with state responsibilities under international law.

Recognizing the severity of this issue, I decided to take action using my data science skills. With the support of Global Fishing Watch, an organization that tracks vessels worldwide and handles big data, I plan to develop a machine learning predictive model to identify illegal fishing activities by analyzing vessel behavior using AIS data.

### Data Science Solution

This project aims to develop a predictive model to identify illegal fishing activities by analyzing vessel behavior using AIS (Automatic Identification System) data and related datasets. By detecting anomalies and patterns indicative of illegal fishing, the model will serve as a valuable tool for policymakers and fishery managers. This tool will enable them to take timely and effective action against illegal activities, helping to protect and conserve marine ecosystems, ensure sustainable fisheries, and support the socioeconomic stability of communities dependent on fishing.

### Impact

The proposed solution can have a significant positive impact by:

- **Protecting Marine Biodiversity:** Reducing illegal fishing activities by preventing it helps preserve marine ecosystems and the diverse species that inhabit them.
- **Supporting Sustainable Fisheries Management:** Providing data-driven insights and predictive capabilities aids in the sustainable management of fish stocks, ensuring long-term viability.
- **Enhancing Enforcement of Fishing Regulations:** Equipping policymakers and fishery managers and governments with a robust tool to identify and act on illegal fishing activities improves compliance with fishing regulations and international laws.

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

To build a comprehensive dataset for this project, I utilized various datasets provided by Global Fishing Watch and meticulously integrated all relevant features and data. This was a challenging and intricate process, but it was essential to ensure the dataset's completeness and accuracy. Below is an overview of the final dataset and the process involved in its creation.

Before we start I would like to mention why Global Fishing Watch was an important part of this project:

<p align="center">
  <a href="https://www.youtube.com/watch?v=tKxCuW-WWng">
    <img src="https://img.youtube.com/vi/tKxCuW-WWng/0.jpg" alt="Watch the video">
  </a>
</p>

1. **Welch et al. (2022) - Hotspots of Unseen Fishing Vessels:**
   - **Description:** Data on suspected AIS disabling events by commercial fishing vessels.
   - **Files:**
     - TBD
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

2. **Fishing Effort:**
   - **Description:** Global datasets of AIS-based fishing effort and vessel presence.
   - **Files and Formats:**
     - TBD
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