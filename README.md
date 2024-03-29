# Object-Detection.

Revolutionizing seismic image interpretation, our project employs cutting-edge deep learning techniques, specifically Convolutional Neural Networks (CNNs), to automate workflows and enhance accuracy in subsurface resource exploration. Addressing the challenges of expert-dependent interpretations in low-resolution sections with intricate structures, our algorithm, trained on synthetic seismic data from coal mines, excels in identifying faults, folds, and flat layers. Through a comparative analysis of instance segmentation algorithms, Detectron2 emerges as the superior choice, boasting an impressive mAP and rapid detection speed of 0.76 frames/second. This project marks a pivotal step towards efficient and precise automated seismic interpretation for complex subsurface structures, leveraging the power of deep learning.

![](https://i.imgur.com/oX9Q5PY.jpg)

## Abstract
Seismic image interpretation is a widely employed method for subsurface resource exploration and reservoir monitoring. This study focuses on investigating automated workflows for interpreting seismic images using deep learning techniques. Current techniques, including fault and horizon picking, seismic attributes, and reservoir characterization, often require expert geologists' interpretation, leading to uncertainties, especially in low-resolution sections with complex structures. To address this, we employ deep learning algorithms, specifically Convolutional Neural Networks (CNNs) for structure identification. CNNs, serving as instance segmentation algorithms, classify structures by detecting faults, folds, and flat layers. Our proposed algorithm guides seismic interpretation by training on synthetic seismic sections generated from interpreted cross-sections of coal mines. We compare two instance segmentation algorithms, Detectron2 and YOLO v7/v8, assessing their ability to identify and segment seismic images for subsurface structure interpretation, including their detection speed. Results indicate that Detectron2 outperforms YOLO v8 and v7 (mAP50-95 = 82% vs. mAP50-95 = 66% and mAP50-95 = 52%) and can segment 640 × 640 seismic section images at a speed of 0.76 frames/second, identifying approximately one and a half structures per second. This method is a crucial advancement in automating seismic image interpretation for complex subsurface structures using deep learning.

## Introduction
The application of machine learning (ML) methods, particularly computer vision models developed by technology companies, has garnered significant interest in the structural interpretation of seismic data for faster subsurface characterization with reduced uncertainty. While these models, rooted in deep learning principles, have shown success in diverse fields such as social media, self-driving vehicles, and medical imaging, their adaptation to the complex nature of subsurface seismic images poses unique challenges. Seismic images, derived from raw seismic reflection data, are susceptible to errors, noise, and distortion, making traditional computer vision models less effective. Researchers are exploring the integration of deep learning computer vision models into geoscientists' workflows to address these challenges. The complexity of subsurface structures and the imperfections in seismic images necessitate the construction of synthetic seismic datasets for training deep learning models. While some studies have employed end-member conceptual models, there is a growing recognition of the need for synthetic models based on free-hand subsurface interpretation to enhance the generalization and accuracy of deep learning algorithms. Transfer learning has shown promise in training CNNs for subsurface structural interpretation with smaller datasets, offering a potential solution to the extensive data requirement. Various studies have demonstrated the feasibility of training CNNs for fault segmentation and subsurface interpretation, highlighting the evolving landscape of ML applications in geoscience.

![](https://i.imgur.com/y89SmU4.jpg)

## Dataset Preparation  
This study employed a Python code, available on GitHub as Synthetic-Seismicon, to generate synthetic seismic data using vector images. Synthetic seismic sections were created based on coalmines data from the Ruhr subbasin in Germany. The stratigraphic model facilitated the assignment of lithology, average standard velocities, and densities to each cross-section. Acoustic impedance was calculated by multiplying rock density by velocity, and reflection coefficients were computed. Subsurface cross-sections from coal mining fields were obtained, scanned, georeferenced, and digitized. These digitized cross-sections were modeled to generate synthetic acoustic impedance and seismic sections, resulting in 137 synthetic acoustic impedance sections and 137 seismic sections. The labeled dataset, comprising 45 cross-sections annotated for flat layers, folds, and faults, was used for training and validation. The remaining 92 cross-sections, along with ten seismic images from the public domain, constituted the test dataset. The trained instance segmentation algorithm aimed to differentiate instances of these classes and outline their boundaries. Limitations include inherent uncertainty in interpretation and seismic modeling, and class imbalance in the dataset, with 887 folds, 824 faults, and 225 flat layers in the training dataset. Addressing these challenges goes beyond the scope of this study, but it recommends exploring the impact of class imbalance on accuracy, comparing Detectron2 and YOLO v8 algorithms.

![](https://i.imgur.com/EVIr5NW.jpg)

Ruhr Coalmines DataSet
=====================
The study area is explored by high-resolution, closely spaced, coal mines with an aerial extent of 323.29 km2 and a depth of 2 km. The subsurface data are provided by mine-workings (galleries, adits and shafts) as well as accompanying boreholes and seismic reflection profiles, which are supported by surface exposure enhanced by open-cast pits. These data were interpreted by Drozdzewski et al. (1980), who reported these observations and erected their own geological interpretations on a series of paper maps and cross-sections. 

They are a set of 12 serial cross-sections with a spacing of 1 to 2 km and tied by two cross-lines. Further, Drozdzewski et al. (1980) indicate the levels of confidence in their interpretations critically using descriptive criteria. The stratigraphic column present in this study is put together and generated after Drozdzewski et al. (1980), Drozdzewski (1993), Suess et al. (2007), Cleal et al. (2009) and Uhl and Cleal (2010). The lithology, formations names, coal seams and stratigraphic units in this stratigraphic column are constrained by correlating the stratigraphic units from Drozdzewski et al. (1980) to other recent studies (e.g. Cleal et al. 2009; Uhl and Cleal 2010). 

**Dataset can be found in the following links:**
1. **Interpreted Images** https://drive.google.com/drive/folders/1j4PBXQyVx89rkVTvMS7Yjl7e7y5OTDrC?usp=sharing
2. **Digitised Cross Sections** https://drive.google.com/drive/folders/1EabQCWqC1JExdLTRCJRx8MDAGHAhHy5N?usp=sharing
3. All the maps and cross-section of the Ruhr subbasin, lower Rhine basin is available in the North Rhine-Westphalia Geological Survey – State Office – (GD NRW) for a fee https://www.gd.nrw.de/pr_kd.htm
4. All the CSV files used in this study https://drive.google.com/drive/folders/14f8_Hzbos23ww6Do96CO2KGeDIIE870h?usp=sharing

## Synthetic Seismic Dataset
1. **Acoustic Impedance Sections** https://drive.google.com/drive/folders/1ANce0auhTOXS0lcIoMfbTcG2r4lTdgfX?usp=sharing
2. **Synthetic Seismic Sections** https://drive.google.com/drive/folders/1C6TAHjFPzltrU4nS1oeHeEdBsEVkWzDM?usp=sharing

## Training, Validation and Testing Datasets
1. **Object Detection Data** https://drive.google.com/drive/folders/1d1NtLFIHlRqjYtQvGjbJoVEzKlmHcwmj?usp=sharing 

## Results
The study compares the overall performance of three models—YOLO v7, YOLO v8, and Detectron2—using various evaluation metrics, including training and validation loss, precision-recall curve, confusion matrix, and mAP on cross-sections labeled in the study. The evaluation involved a validation set of 45 unlabeled synthetic acoustic impedance images and a testing set of 92 synthetic seismic sections from coalmines and 10 seismic images from the public domain. Detectron2 exhibited superior performance with an mA50-mAP95 of 0.81%, outperforming YOLO v8 (0.66%) and YOLO v7 (0.52%). The average Recall, average Precision, and mAP50 values for Detectron2 were higher than YOLO v8 and v7, indicating better detection, segmentation, and prediction. While Detectron2 was the fastest to train (2.25 hours), YOLO v8 was ten times faster in evaluating the testing set (7.3 ms per image). Despite the class imbalance in the dataset (887 folds, 824 faults, and 225 flat layers), Detectron2 showed better overall performance, emphasizing the impact of class instances on algorithm performance. The study suggests the need for larger datasets, closer to 6000 instances (2000 per class), for optimal performance in segmentation algorithms, particularly when dealing with imbalanced classes.

![](https://i.imgur.com/DehfzbE.jpg)

## Conclusion
Seismic data is a cornerstone in subsurface resource exploration, offering crucial insights into geological structures and potential reservoirs. While human interpretation has long been the norm, the integration of machine learning techniques has advanced automatic seismic interpretation models. These models hold promise in providing efficient and unbiased interpretations. However, it's important to note that these models heavily rely on training with synthetic seismic data derived from simplified conceptual end member models, posing a limitation in accurately representing subsurface complexity. This study showcases the application of deep learning-based instance segmentation algorithms in interpreting seismic sections using synthetic acoustic impedance images generated from free-hand interpreted subsurface cross-sections. Detectron2, outperforming YOLO v8 and v7, demonstrated higher training speed and Average Precision. The study highlights the feasibility of using deep learning algorithms in seismic structural interpretation, even with a limited dataset. It suggests the potential for expanding interpretation capabilities by combining synthetic data with end-member conceptual models during training. Further research is essential to validate performance thresholds on diverse synthetic seismic sections.

![](https://i.imgur.com/Xj8t46Y.jpg)

## Final Remarks
This study highlights the potential of using a deep learning algorithm for interpreting seismic sections, particularly those of good to fair quality, interpretable by experts. Demonstrating success, the research discriminates simple structures on subsurface seismic sections using synthetic acoustic impedance images from legacy-interpreted cross-sections. Applicable to resource exploration, such as coal mines and oil and gas, the approach is cost-effective, utilizing legacy data for scalability. 

Future work
===========
Future studies should explore deep learning with low-resolution seismic images and complex structures, extending the methodology to distinguish between various geological features.

Acknowledgements 
=================
The work contained in this paper contains work conducted during a PhD study undertaken as part of the Natural Environment Research Council (NERC) Centre for Doctoral Training (CDT) in Oil and Gas funded 50% through its National Productivity Investment Fund grant number NE/R01051X/1 and 50% by the University of Aberdeen through its PhD Scholarship Scheme. The support of both organisations is gratefully acknowledged. The work is reliant on Open-Source Python Libraries, particularly Pytorch, Detectron2, YOLO v7 and v8, and contributors to these are thanked, along with GitHub for open access hosting of the Python scripts for the study.

I extend my sincere gratitude to Roboflow for their invaluable contribution to this notebook. Their guidance has been instrumental in expanding the scope of knowledge presented here. For further insights, please visit their GitHub repository. Many thanks for their generous support. [Roboflow Notebooks](https://github.com/roboflow/notebooks)

![University of Aberdeen](https://i.imgur.com/PILyj4m.jpg)

![NERC-CDT](https://nerc-cdt-oil-and-gas.ac.uk/wp-content/uploads/news/2015-news-NERC-funding.jpg)

![NERC](https://auracdt.hull.ac.uk/wp-content/uploads/2019/11/UKRI_NER_Council-Logo_Horiz-RGB.png)

![CDT](https://i.imgur.com/QDOhcN3.png)
