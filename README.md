# Passenger Comfort Assessment in Dynamic Driving Environments

This repository contains the implementation and findings of my Bachelor Thesis, presented at Babeș-Bolyai University, Cluj-Napoca, in 2024. The focus of this research was to explore and develop an AI-based solution for predicting and improving passenger comfort in dynamic driving scenarios.

## Motivation

As the automotive industry shifts towards autonomous vehicles and enhanced user experiences, passenger comfort has emerged as a critical factor. This project was motivated by the need to address this challenge using advanced data analytics and AI models. By analyzing vehicle dynamics data and physiological responses, I aimed to create a reliable system to predict and visualize passenger comfort levels, contributing to safer and more enjoyable travel experiences.

## Repository Structure

The repository is organized into the following sections:

### 1. **Gathered_Data**
   - Contains synchronized datasets collected from vehicle sensors (CAN Bus, OBD-II) and heart rate monitoring devices.
   - **Content Removed:** Some files in this folder have been removed to protect the identity of the test subjects.

### 2. **Jupyter_Notebooks**
   - Includes Python notebooks used for:
     - Data preprocessing and synchronization.
     - Analyzing and visualizing collected data.
     - Testing and evaluating AI models.

### 3. **Media**
   - Includes plots and photos generated during the analysis phase for visual representation.

### 4. **Python_Applications**
   - Scripts for applications such as:
     - Comfort Level Visualization Application (built with PyQt and Plotly).
     - Recorded Data Synchronization tools.
     - Carla Simulator scripts for testing in simulated environments.

### 5. **Trained_Neural_Networks**
   - Contains the trained AI models, including baseline models and personalized models for test subjects.
   - **Content Removed:** Data specific to test subjects has been excluded for privacy reasons.

## Key Features

- **Data Collection and Synchronization**: Efficient integration of vehicle sensor data and heart rate monitoring, processed to align timestamps.  
- **AI-Driven Comfort Prediction**: Development of neural network models using TensorFlow to predict passenger comfort based on real and simulated driving data.  
- **Visualization Tools**: Interactive applications for real-time comfort analysis and dynamic visualizations.  
- **Simulation Environment**: Use of CARLA simulator and Logitech G29 hardware to test comfort in controlled scenarios.

## Ethical Considerations

To ensure the privacy and confidentiality of individuals involved in this research, sensitive data related to test subjects (names and identifying details) has been removed. This complies with ethical research practices and ensures that no personal information is disclosed.

## Applications

- Autonomous vehicle systems to enhance passenger experience.
- Tailored solutions for ride-sharing platforms to improve comfort.
- Integration with insurance models to assess driving quality.

## Future Scope

- Expanding datasets with diverse driving conditions for broader applicability.  
- Collaborating with the automotive industry for real-world integration.  
- Refining AI models for real-time implementation in autonomous vehicles.

## How to Contribute

Contributions are welcome! If you would like to enhance the project or adapt it for new applications, feel free to fork the repository and submit a pull request.

---

### License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

---

**Note:** The full methodology and findings can be found in the thesis documents provided in this repository.
