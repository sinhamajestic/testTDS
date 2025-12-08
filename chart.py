import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for marketing campaigns
n_campaigns = 80

# Create campaign segments with different characteristics
segments = ['Social Media', 'Email Marketing', 'Content Marketing', 'Paid Search', 'Influencer']
segment_list = np.random.choice(segments, n_campaigns)

# Generate Customer Acquisition Cost (CAC) - range $50 to $500
cac = np.random.uniform(50, 500, n_campaigns)

# Generate Customer Lifetime Value (CLV) with positive correlation to CAC
# CLV should generally be higher than CAC for profitable campaigns
clv_base = cac * np.random.uniform(1.5, 4.5, n_campaigns)
clv_noise = np.random.normal(0, 200, n_campaigns)
clv = clv_base + clv_noise

# Ensure CLV is positive and realistic
clv = np.clip(clv, 100, 2500)

# Create DataFrame
df = pd.DataFrame({
    'Customer_Acquisition_Cost': cac,
    'Customer_Lifetime_Value': clv,
    'Campaign_Type': segment_list,
    'ROI': (clv - cac) / cac * 100  # ROI percentage
})

# Set professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create figure with exact dimensions for 512x512 output
plt.figure(figsize=(8, 8))

# Create scatterplot with professional styling
scatter = sns.scatterplot(
    data=df,
    x='Customer_Acquisition_Cost',
    y='Customer_Lifetime_Value',
    hue='Campaign_Type',
    size='ROI',
    sizes=(50, 400),
    alpha=0.7,
    palette='viridis',
    edgecolor='white',
    linewidth=0.5
)

# Add break-even line (where CLV = CAC)
max_val = max(df['Customer_Acquisition_Cost'].max(), df['Customer_Lifetime_Value'].max())
plt.plot([0, max_val], [0, max_val], 'r--', linewidth=2, alpha=0.5, label='Break-even Line')

# Customize the plot
plt.title('Customer Lifetime Value vs. Acquisition Cost\nMarketing Campaign Effectiveness Analysis', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Customer Acquisition Cost ($)', fontsize=12, fontweight='bold')
plt.ylabel('Customer Lifetime Value ($)', fontsize=12, fontweight='bold')

# Adjust legend
plt.legend(title='Campaign Type', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Tight layout to prevent label cutoff
plt.tight_layout()

# Save with exact specifications
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
print("Chart saved successfully as chart.png (512x512 pixels)")

# Display summary statistics
print("\nSummary Statistics:")
print(f"Average CAC: ${df['Customer_Acquisition_Cost'].mean():.2f}")
print(f"Average CLV: ${df['Customer_Lifetime_Value'].mean():.2f}")
print(f"Average ROI: {df['ROI'].mean():.2f}%")
print(f"Campaigns above break-even: {(df['Customer_Lifetime_Value'] > df['Customer_Acquisition_Cost']).sum()}/{len(df)}")
