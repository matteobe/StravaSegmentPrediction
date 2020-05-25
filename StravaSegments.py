#!/usr/bin/env python
# coding: utf-8

# # Strava Segments Time Prediction

# This Jupyter Notebook imports a segments from Strava and calculates the time required for finishing the segment according to the user's input. Furthermore the program also calculates the Training Stress Score® (TSS), Normalized Power® (NP) and Intensity Factor® (IF) for the envisioned ride.
# 
# The required input consists of:
# - Rider data
#  - Weight
#  - Position (flat/ascent/descent)
#  - Power (flat/ascent/descent)
#  - Functional Threshold Power (FTP)
#  - Sweat rate (L/(h TSS))
# - Bike data
#  - Weight
#  - Rolling resistance
#  - Drivetrain loss
# - Further equipment
#  - Clothes / helmet and shoes weight
#  - Nutrition and hydration weight
# 
# Normalized Power® (NP), Intensity Factor® (IF), and Training Stress Score® (TSS) are registered trademarks of Peaksware, LLC.

# In[1]:


# Start by importing the required libraries

# API requests libraries
import json
import requests


# In[ ]:


# Download information on the Strava segment in question

