# UmaPepPredi
An interactive web application for predicting the umami intensity of short peptides using machine learning. This project innovatively integrates global physicochemical descriptors and local sequence features of peptides, and reveals the dominant influence of the local chemical environment on umami intensity.
# Requirement
1. pandas
2. RDkit
3. sklearn
4. streamlit
5. shap
6. matplotlib.pyplot
7. py3Dmol
8. AutoDock Vina
# Usage
## Running the Application
1. Clone this repository
2. Ensure you have the required data file umami_features.csv in the project directory.
3. Run the model:`python model.py`
4. Run the Streamlit application:
`streamlit run streamlit.py`
5. Open your web browser and navigate to the local URL displayed (typically http://localhost:8501)
## Using the Predictor
1. Input Peptide Sequence: Enter a short peptide sequence using single-letter amino acid codes (e.g., "EE" for Glu-Glu, "KGR" for Lys-Gly-Arg)
2. Set Vina Binding Energy: Adjust the molecular docking energy value (in kcal/mol)
3. Get Prediction: Click the "Predict" button to receive the umami intensity score on a 5.0 scale
4. View Explanation: Check the "Show SHAP Explanation" box to see which features most influenced the prediction
5. 3D Visualization: View the generated 3D molecular structure of your peptide
## Model Features
The predictor uses the following features for umami intensity prediction:
1. logP: Lipophilicity (partition coefficient)
2. TPSA: Topological Polar Surface Area
3. charge: Molecular charge
4. molecular_weight: Peptide molecular weight
5. vina_energy: Molecular docking binding energy
6. Sequence-based features (CTERM, NTERM, N_TERM):
- CTERM indicates whether the C-terminal amino acid is acidic.  
- NTERM indicates whether the N-terminal amino acid is hydrophobic.  
- N_TERM indicates whether the N-terminal amino acid is charged.
