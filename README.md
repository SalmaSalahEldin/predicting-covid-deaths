# Project 2

## Introduction
This project predicts and compares the possibility of deaths, and critical states of covid-positive patients in Singapore for the upcoming day based on vaccination status using Markov Chain.
The model is used to answer questions such as: 
- In the next month, what is the expected number of deaths and critical state patients among the fully vaccinated?
- In the next month, what is the expected number of deaths and critical state patients among the non-vaccinated?

## Obtaining Data
The dataset has been obtained via the [Ministry of Health website](https://data.gov.sg/dataset/covid-19-case-numbers?resource_id=783f0c4c-caf7-4818-8683-760f3d7f0757). The dataset is called "7-Day moving average of deaths & active cases in ICU, per 100k population, by vax status." 

## Method
The details of each function are documented via comments in in [main.py](main.py). 
Here is a brief overview of the implementation.
I downloaded the CSV file and read it into a dataframe using the library Pandas.
Under the transitionMatrix method, I construct a full transition matrix consisting of three states.
The three states are non-critical, critical (ICU), and death.

Non-critical | Critical (ICU) | Death
-- | -- | --
Non-critical | x11 | x12 | x13
Critical (ICU) | x21 | x22 | x23
Death | x31 | x32 | x33

Since the data points are given for 7 days, I take an average of each of the states for each vax status for the seven day points.
I use the average points to create a transition matrix.

Using the transition matrix, I use the Markov Chain to predict for the user-designated range (in days).

## Outcome

## Assumptions and Limitations
Along the way, I realized that there is no data to represent the state change from critical to death.
I looked at 