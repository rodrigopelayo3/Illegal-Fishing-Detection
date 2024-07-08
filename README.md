# Illegal Fishing Detection

## Table of Contents

1. [Illegal Fishing Detection](#illegal-fishing-detection)
   1. [Project Overview](#project-overview)
      1. [Problem Area](#problem-area)
      2. [Data Science Solution](#data-science-solution)
      3. [Impact](#impact)
   2. [Built With](#built-with)
   3. [Dataset Description](#dataset-description)
2. [Datasets from Global Fishing Watch](#datasets-from-global-fishing-watch)
   1. [Dataset: Welch et al. (2022) - Hotspots of Unseen Fishing Vessels](#dataset-welch-et-al-2022---hotspots-of-unseen-fishing-vessels)
   2. [Dataset: Fishing Effort](#dataset-fishing-effort)
   3. [Merged Dataset Overview](#merged-dataset-overview)
      1. [Columns Description](#columns-description)
3. [Getting Started](#getting-started)
   1. [Prerequisites](#prerequisites)
   2. [Installation](#installation)
   3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)
6. [Acknowledgements](#acknowledgements)

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

To build a comprehensive dataset for this project, I utilized various datasets provided by Global Fishing Watch and meticulously integrated all relevant features and data. This was a challenging and iterative process, but it was essential to ensure the dataset's completeness and accuracy. Below is an overview of the final dataset and the process involved in its creation.

Before we start, I would like to mention why Global Fishing Watch was an important part of this project (Click on the image for a YouTube video "Open in a new tab" is recomended):

<p align="center">
  <a href="https://www.youtube.com/watch?v=tKxCuW-WWng">
    <img src="https://img.youtube.com/vi/tKxCuW-WWng/0.jpg" alt="Watch the video">
  </a>
</p>

## Datasets from Global Fishing Watch

The goal of this capstone project is to develop a predictive model to identify illegal fishing activities by analyzing vessel behavior using AIS (Automatic Identification System) and related datasets. The aim is to provide a tool for policymakers and fishery managers to detect and prevent illegal, unreported, and unregulated (IUU) fishing.

In order to achieve this It was crucial to obtain a dataset with good quality and comprehensive data on global fishing activities. After thorough research, I discovered an organization called Global Fishing Watch (GFW), which provides data on global fishing activities. GFW's mission is to advance ocean sustainability through increased transparency in fishing activities. They offer a range of datasets that are useful for analyzing and understanding fishing behaviors and identifying potential illegal activities.

Since I took an aproach at a professional level I encountered a really good challenge on how to build a good dataset. I looked at 13 different Datasets with different many insane amount of csv files each which i had to concatenate and merge to grab sense of data, as well as making sure I was grabbing the right features and making sure the data was not altered or if it was that was altered in the right way.

On the first Sprint I decided to go for 4 datasets but after a really intense research among the project had been advancing I have been grabing the best features for my dataset and finally picked 3 main Datasets and added a little bit of my investigation.

After analyzing those 13 different datasets from GFW data, I decided to keep 3 and add information from my own research.

1. Fishing Effort:
    Given the large size of this dataset, and for being able to match it with the Hotspost Unseen Fishing Vessels i grabbed data from the year of 2017 to 2019. This will Allow me to match the boats among the events that this boats went missing and give the best approach on how to board the problem from my perspective.
     
2. Welch et al. (2022) - Hotspots of Unseen Fishing Vessels:
   Data on suspected AIS disabling events by commercial fishing vessels between 2017-2019. The dataset identifies when and why fishing vessels intentionally stop broadcasting their position, potentially indicating illegal activities.

3. Carrier Vessel Portal events:
    This Dataset deploys all the fishing vessels that encountered a carrier vessel by events and it goes from 2017 till the current month, for the matter of this investigation I am going to grab data from 2017 to 2019. This dataset is important because most of the fishing boats don´t come back to shore or ports to deliver their catch, instead they have an encounter with a carrier vessel, this allows the fishing vessel to stay at opean sea for longer periods of time since they transfer the catch and recieve fuel and supplies from the carrier vessel, This is a good thing but also it can be be counterproductive since the practice of this encounters could be queue for Illegal activities, since they make difficult to keep track and control of where the origin of the fish were caught, as well as another illegal activities.

Now that the Datasets were difined and all the iterations were done, I came accros on this dataset, I have to clarify that I had to perfom unsupervised learning since I didn´t have Labeled data for IUU vessels, I am going to talk about this step later on this notebook.

## Data Dictionary

| Column                           | Data Type | Description                                                                         |
|----------------------------------|-----------|-------------------------------------------------------------------------------------|
| `gap_id`                         | `object`  | Unique identifier for each gap event that a vessel went missing.                                               |
| `mmsi`                           | `int64`   | Maritime Mobile Service Identity, a unique identifier for vessels.                  |
| `vessel_class`                   | `object`  | Class of the vessel, indicating its type of fishing vessel.                                           |
| `flag`                           | `object`  | Flag state of the vessel, indicating the country of registration.                   |
| `vessel_length_m`                | `float64` | Length of the vessel in meters.                                                     |
| `vessel_tonnage_gt`              | `float64` | Gross tonnage of the vessel.                                                        |
| `gap_start_lat`                  | `float64` | Latitude where the gap event started.                                               |
| `gap_start_lon`                  | `float64` | Longitude where the gap event started.                                              |
| `gap_start_distance_from_shore_m`| `float64` | Distance from shore where the gap event started, measured in meters.                |
| `gap_end_lat`                    | `float64` | Latitude where the gap event ended.                                                 |
| `gap_end_lon`                    | `float64` | Longitude where the gap event ended.                                                |
| `gap_end_distance_from_shore_m`  | `float64` | Distance from shore where the gap event ended, measured in meters.                  |
| `gap_hours`                      | `float64` | Duration of the gap event in hours.                                                 |
| `Distance_to_High_Risk_Zone_NM`  | `float64` | Distance to the nearest high-risk zone, measured in nautical miles (NM).            |
| `IUU_Risk_Proximity`             | `int64`   | Proximity score to illegal, unreported, and unregulated (IUU) fishing risk areas.   |
| `Distance_to_MPA_NM`             | `float64` | Distance to the nearest Marine Protected Area (MPA), measured in nautical miles.    |
| `Closest_MPA`                    | `object`  | Name of the closest Marine Protected Area (MPA).                                    |
| `MPA_Proximity_Level`            | `int64`   | Proximity level to the nearest MPA, with a lower value indicating closer proximity. |
| `encountered_carrier_during_day` | `int64`   | Indicates whether the vessel encountered a carrier during the day (1 = Yes, 0 = No).|
| `Distance_event_start_to_end_NM` | `float64` | Distance from the start to the end of the event, measured in nautical miles.        |
| `IUU_Classified`                      | `int64`   | Classification of the event as IUU or non-IUU (1 = IUU, 0 = non-IUU).               |


### IUU Classification explanation 

The journey to classify IUU (Illegal, Unreported, and Unregulated) fishing events has been both challenging and enlightening. IUU fishing is a complex issue influenced by various factors such as regional regulations, environmental conditions, and evolving vessel behaviors. These complexities, combined with limited data availability, have made it difficult for researchers to develop concrete machine learning models for IUU detection. However, organizations like Global Fishing Watch are helping bridge this gap by providing access to SAS and AIS data, which can be integrated to enhance our understanding and detection of IUU activities.

Initial Attempts and Manual Classification Approach

In my initial attempts, I utilized unsupervised learning techniques such as K-Means, Gaussian Mixture Models (GMM), and agglomerative clustering. Despite significant feature engineering and iterative adjustments, these models were only partially successful, primarily classifying data based on proximity to shores. This led me to develop a manual points-based system to classify IUU events, considering factors like the duration of AIS deactivation, the type of fishing vessel, and whether the vessel was flagged by a high-risk country known for IUU activities. This approach provided a practical starting point but was not a long-term solution.

Isolation Forest: A Promising Unsupervised Approach

Revisiting unsupervised learning models, I identified Isolation Forest as a promising approach. Isolation Forest is effective in detecting anomalies, which is crucial for identifying IUU fishing patterns. Preliminary results indicated that this method provided meaningful classifications aligned with known IUU activities. The model highlighted anomalous behaviors and regions, offering a more nuanced understanding of the data.

Integration with Supervised Learning Models

Following the initial anomaly detection with Isolation Forest, I integrated supervised learning models to refine the classification. Models like Logistic Regression, Random Forest, and XGBoost were employed to enhance the detection accuracy of IUU fishing activities. These models allowed for better prediction and understanding of IUU events based on the identified anomalies.

### Investigation: Vessel Types and Their Association with IUU Fishing

| Rank | Vessel Type        | Known IUU Risk Level | Average Speed                              | Average Fishing Time | Description                                                                                                                                                |
|------|--------------------|----------------------|--------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | Trawlers           | High                 | 10-12 knots (18.5-22.2 km/h or 11.5-13.8 mph) | 12-18 hours per day  | **IUU Risk**: Frequently engage in illegal fishing in restricted areas and overfishing. **Description**: Trawlers are heavily associated with IUU fishing due to their large catch capacity and operations in restricted zones. |
| 2    | Tuna Purse Seiners | High                 | 12-15 knots (22.2-27.8 km/h or 13.8-17.3 mph) | 4-8 hours per set    | **IUU Risk**: Known for illegal fishing in marine protected areas and exceeding quotas. **Description**: Tuna purse seiners are large and highly mobile, often implicated in unreported fishing activities. |
| 3    | Drifting Longlines | Medium to High       | 8-10 knots (14.8-18.5 km/h or 9.2-11.5 mph)  | 24-48 hours per set  | **IUU Risk**: Involved in bycatch and unreported catches, especially of endangered species. **Description**: Operate in vast ocean areas, making them a significant concern for IUU fishing, particularly for high-value species like tuna and swordfish. |
| 4    | Squid Jiggers      | Medium               | 10-12 knots (18.5-22.2 km/h or 11.5-13.8 mph) | 6-12 hours per night | **IUU Risk**: Often fish in international waters with weak regulations. **Description**: Typically implicated in IUU fishing where squid populations are not well-regulated, leading to overfishing and unreported catches. |
| 5    | Other              | Variable             | Varies widely depending on vessel type       | Variable             | **IUU Risk**: Includes smaller, artisanal boats and other less common vessel types. **Description**: The IUU risk in this category depends on the specific type of vessel and fishing practice, with smaller boats often involved due to lack of monitoring, especially in developing regions. |

**Summary**:
- **Trawlers** and **tuna purse seiners** are most notorious for IUU activities due to their large-scale operations and capacity to evade regulations.
- **Drifting longliners** are significant concerns for IUU fishing, particularly in high seas, due to extensive reach and frequent bycatch.
- **Squid jiggers** pose IUU threats mainly in international waters with weak enforcement.
- **Other vessels** include a wide range of boats with varying IUU risks, often influenced by local enforcement and fishing practices.


With this and after analyzing the map we can see that vessels in red (IUU vessels) Tend to be close to Marine Protected areas, as well as the type of fishing vessel it is or even the amopunt of hours spend offline. After this approach and explanation we can continue with the modeling.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Example</title>
</head>
<body>
    <h1>Welcome to My Project</h1>
    <img src="map.html" alt="Example Image">
</body>
</html>

We can clearly see that the map is following a pattern based on the number of hours AIS (Automatic Identification System) has been turned off in each event. This aligns closely with the results of the unsupervised Isolation Forest model used to detect anomalies. The model has successfully identified events where boats have turned off their AIS, which is a common tactic used in IUU (Illegal, Unreported, and Unregulated) fishing activities.

- Patterns in AIS Deactivation:

	-	Duration of AIS Deactivation: The map highlights regions where vessels have turned off their AIS for extended periods. This is a strong indicator of potential IUU activities, as longer AIS gaps are often used by vessels to avoid detection while engaging in illegal fishing.
	-	Anomaly Detection: The red dots on the map represent suspected illegal activities identified by the Isolation Forest model. These anomalies are flagged based on patterns in the AIS data, such as extended deactivation periods and other relevant features.

- Proximity to Marine Protected Areas (MPAs):
	
	-	High Density of Anomalies Near MPAs: The map shows a high concentration of red dots near MPAs (marked by blue indicators). This suggests that vessels are turning off their AIS systems to engage in illegal fishing activities within or near these protected zones.
	-	Enforcement Challenges: The presence of numerous anomalies near MPAs underscores the challenges in monitoring and enforcing fishing regulations in these sensitive areas. MPAs are established to protect marine biodiversity, but the proximity of suspected illegal activities highlights the ongoing risk to these environments.

- Regional Insights:

	-	South America (Pacific Coast): High concentrations of anomalies are observed near the coastlines of Colombia, Ecuador (Galápagos Islands), Peru, and northern Chile. These areas are known for their rich marine resources and stringent protection laws, making them prime targets for IUU activities.
	-	West Africa: The Gulf of Guinea, Senegal, and Mauritania show dense clusters of suspected illegal activities. This region’s rich fisheries and presence of MPAs make it a critical area for monitoring and enforcement.
	-	Western Pacific Ocean: The Indonesian Archipelago and the waters around the Philippines display significant red dot clusters, indicating widespread suspected IUU fishing in these biodiverse regions.
	-	Caribbean and Central America: The Caribbean Sea, especially near Central American countries, shows noticeable clusters of anomalies, highlighting potential IUU activities in these productive waters.

The map provides a visual confirmation of the patterns detected by the Isolation Forest model. It highlights the critical areas where vessels are turning off their AIS, particularly near MPAs, to engage in suspected illegal fishing activities. This analysis emphasizes the need for robust monitoring, better enforcement mechanisms, and international cooperation to combat IUU fishing effectively.

By aligning the map with the results from the Isolation Forest model and focusing on regions with high densities of anomalies, we can enhance our strategies for detecting and preventing illegal fishing activities. This approach ensures the protection of marine resources and biodiversity, especially within and around MPAs.

## Getting Started

### Prerequisites
- List any software, libraries, or tools required to work with the project. TBD

### Installation
- Provide step-by-step instructions on how to set up the project locally. TBD

### Usage
- Explain how to run the project, including any scripts or commands. TBD

## Contributing
- Guidelines for contributing to the project. TBD

## License
- Information about the project's license. TBD

## Acknowledgements
- Acknowledge any individuals, organizations, or resources that contributed to the project. GLOBAL FIHSING WATCH

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

## Conclusion

I feel proud and confident that my capstone project on detecting illegal fishing went really well. My approach to managing and merging the datasets and using them to find a way of addressing the problem from my point of view was effective. I also recognize that this is not the definitive solution to the problem but it is another way to tackle and identify suspicious patterns among fishing vessels. The fact that we now have this research can truly support the development of new techniques or improve measures on how this huge global problem is addressed.

My investigation and skills in data science were significant supports in creating this approach to the problem, as well as showcasing my ability to bring solutions to problems through data. I am proud that I showcased my technical skills in machine learning in such an ambitious project that can tackle a major world problem, demonstrating what we can achieve with the correct scope and tools. This last sprint is a testament to all the effort and the process that was experienced during this project.

Using unsupervised learning to identify anomalies and supporting them with supervised learning was a crucial part of the project. The implementation of the Isolation Forest algorithm to detect anomalous behaviors among vessels provided a strong foundation for identifying potential illegal, unreported, and unregulated (IUU) fishing activities. By focusing initially on sensitivity, we ensured that as many true anomalies were detected as possible, which is critical in the initial stages of anomaly detection for IUU fishing. This approach minimized the risk of missing true illegal activities, even though it might have resulted in a higher number of false positives.

Throughout this project, the use of various machine learning models and techniques underscored the importance of a multi-faceted approach to complex problems like IUU fishing. The combination of unsupervised and supervised learning allowed for a comprehensive analysis, starting from anomaly detection to classification and validation. The visualization tools, including ROC and precision-recall curves, confusion matrices, and heatmaps, provided clear and interpretable insights into the models’ performance, aiding in the continuous refinement of the detection system.

In summary, this project not only demonstrated the power of machine learning in tackling global issues but also highlighted the importance of rigorous data analysis, model evaluation, and iterative improvement. The journey from data preprocessing to anomaly detection, and finally to the classification of legal and illegal activities, showcased the potential of data science in making impactful contributions to real-world problems. This project stands as a testament to the hard work, dedication, and analytical skills developed throughout this capstone experience, paving the way for future advancements in the fight against illegal fishing.

© 2024 Rodrigo Pelayo Ochoa
