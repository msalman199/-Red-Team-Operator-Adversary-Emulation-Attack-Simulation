#!/usr/bin/env python3
"""
Threat Analysis and Statistics Generator
Students will complete this to provide detailed analysis and metrics
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime

class ThreatAnalyzer:
    def __init__(self):
        self.output_dir = "../reports"
        self.assets_dir = "../assets"
        
    def generate_threat_statistics(self):
        """
        Generate comprehensive threat statistics and visualizations.
        
        TODO: Complete this function to:
        1. Create a DataFrame with threat data (type, frequency, severity, detection rate, cost)
        2. Calculate risk scores for each threat
        3. Create 4 visualizations:
           - Bar chart of top threats by risk score
           - Pie chart of threat frequency distribution
           - Scatter plot of detection rate vs severity
           - Bar chart of mitigation costs
        4. Save statistics to JSON file
        5. Return sorted DataFrame
        """
        
        # TODO: Create threat_data dictionary with appropriate columns
        threat_data = {
            'Threat_Type': [],
            'Frequency': [],
            'Severity': [],
            'Detection_Rate': [],
            'Mitigation_Cost': []
        }
        
        # TODO: Create DataFrame from threat_data
        df = pd.DataFrame(threat_data)
        
        # TODO: Calculate risk score
        # Formula: Frequency * Severity * (100 - Detection_Rate) / 100
        
        # TODO: Create 2x2 subplot figure
        
        # TODO: Create visualization 1 - Top threats bar chart
        
        # TODO: Create visualization 2 - Frequency pie chart
        
        # TODO: Create visualization 3 - Detection vs Severity scatter
        
        # TODO: Create visualization 4 - Mitigation cost bar chart
        
        # TODO: Save figure to assets directory
        
        # TODO: Create and save statistics summary to JSON
        
        return df

def main():
    analyzer = ThreatAnalyzer()
    analyzer.generate_threat_statistics()

if __name__ == "__main__":
    main()
