Customer Analytics: CLV vs. Acquisition Cost Analysis
23f1001286@ds.study.iitm.ac.in
Project Overview
This repository contains a professional-grade data visualization created for Ziemann Kris and Wyman, a data-driven customer experience company. The analysis examines the relationship between Customer Lifetime Value (CLV) and Customer Acquisition Cost (CAC) to optimize marketing spend and campaign effectiveness.
Business Context
This visualization was developed for a major retail client's quarterly business review to:

Analyze marketing campaign effectiveness across different channels
Identify optimal customer acquisition strategies
Evaluate ROI for various marketing segments
Support data-driven decision-making for executive leadership
Optimize marketing budget allocation

Visualization Details

Tool: Python with Seaborn statistical visualization library
Chart Type: Scatterplot with multiple dimensions
Data Dimensions: CAC, CLV, Campaign Type, ROI
Image Specifications: 512x512 pixels PNG format
Styling: Professional whitegrid style with viridis color palette

Technical Implementation
Libraries Used

seaborn: Statistical data visualization
matplotlib: Plotting framework
pandas: Data manipulation and analysis
numpy: Numerical computations

Data Structure
The analysis includes 80 marketing campaigns across 5 channels:

Social Media
Email Marketing
Content Marketing
Paid Search
Influencer Marketing

Key Metrics

Customer Acquisition Cost (CAC): Cost to acquire a single customer ($50-$500)
Customer Lifetime Value (CLV): Total revenue from customer relationship ($100-$2,500)
ROI: Return on Investment percentage
Break-even Line: Reference line where CLV equals CAC

Visualization Features

Size encoding: Bubble size represents ROI
Color encoding: Different colors for campaign types
Break-even line: Red dashed line showing profitability threshold
Professional styling: Publication-ready appearance
Statistical rigor: Seaborn-based analysis

Business Insights
The scatterplot reveals:

Campaign effectiveness across different marketing channels
Identification of high-ROI and low-ROI campaigns
Campaigns above break-even line are profitable
Relationship between acquisition cost and lifetime value
Optimal marketing spend allocation opportunities

Files

README.md - Project documentation
chart.py - Python script for generating visualization
chart.png - Generated scatterplot (512x512 pixels)

Usage
To regenerate the visualization:
bashpython chart.py
This will generate chart.png with the customer analytics visualization.
Requirements
seaborn>=0.12.0
matplotlib>=3.5.0
pandas>=1.3.0
numpy>=1.21.0
Application
This visualization is suitable for:

Executive presentations and board reports
Quarterly business reviews
Strategic marketing planning
Budget allocation decisions
Marketing campaign optimization
