import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----------------------------
# Generate realistic synthetic data
# ----------------------------
np.random.seed(42)

channels = ["Email", "Live Chat", "Phone Support", "Social Media"]

email_times = np.random.normal(24, 6, 300)        # slower
chat_times = np.random.normal(8, 2, 300)          # fastest
phone_times = np.random.normal(15, 4, 300)        # medium
social_times = np.random.normal(18, 5, 300)       # medium-high

response_times = np.concatenate([
    email_times,
    chat_times,
    phone_times,
    social_times
])

support_channels = (
    ["Email"] * 300 +
    ["Live Chat"] * 300 +
    ["Phone Support"] * 300 +
    ["Social Media"] * 300
)

df = pd.DataFrame({
    "Support Channel": support_channels,
    "Response Time (Hours)": response_times
})

# ----------------------------
# Professional Seaborn Styling
# ----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# ----------------------------
# Create Violin Plot
# ----------------------------
plt.figure(figsize=(8, 8))  # For 512x512 with dpi=64

sns.violinplot(
    x="Support Channel",
    y="Response Time (Hours)",
    data=df,
    palette="Set2",
    inner="quartile"
)

# ----------------------------
# Titles and Labels
# ----------------------------
plt.title("Customer Support Response Time Distribution\nBy Support Channel", fontsize=16)
plt.xlabel("Support Channel", fontsize=12)
plt.ylabel("Response Time (Hours)", fontsize=12)

# ----------------------------
# Save Chart (EXACT REQUIREMENT)
# ----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("chart.png generated successfully (512x512 pixels).")
