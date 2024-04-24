# Project description

### Motivation
Taxes are the most important (if not, actually, the only) source of reliable income for a state. The type of taxes and their amount are constantly part of political discussions, no matter which parties form the government. Since I am a politically interested person, I found the dataset on taxes in germany distributed by type and time very interesting. 

### Dataset description
The dataset is called [**Statistic on the national tax income**](https://www-genesis.destatis.de/genesis/online#astructure) (code 71211-0005). It includes the years 1999-2024 and contains monthly data. The data is listed numerically in thousands of euros, the table is very dense (most rows have values for all available years), and the data is also very recent (up to the latest month of 2024). This should allow for easy and meaningful analysis.

From the 54 available rows of different tax types I chose several ones which I thought to be interesting:
- Firstly, I chose the overall tax income as well as the two most important ones I could think of: Income tax and sales tax
- Secondly, since I think wealth inequality is an important topic, I chose the wealth tax, the solidarity surtax, and the inheritance tax
- Thirdly, I chose different consumer taxes (alcohol, tabacco, etc.), because I wanted to see if I could find seasonal variations in the data and also look at their development
- Lastly, I chose a fex taxes which also sounded interesting to me: air traffic, energy, electrical energy, and liquor license taxes

I deliberately chose the dataset containing the original uncorrected data. The same data is also available on the destatis website with corrections for seasonal and calendarial variations (More information [here](https://www.destatis.de/DE/Themen/Wirtschaft/Grosshandel-Einzelhandel/Glossar/kalender-saisonbereinigte-werte.html) and [here](https://www.destatis.de/DE/Methoden/Saisonbereinigung/_inhalt.html)); but since I wanted to look at exactly these variations I chose the uncorrected data. One could, however, also compare findings from the uncorrected data with the corrected data and see to what extent they hold true.

### Research questions
- How has the overall tax income developed over the past 20 years? 
- Can we see seasonal variations in the data, specifically in the consumer goods taxes?
- What role did the air traffic tax play in the overall tax income since it's introduction in 2011?
- How do the income tax and the three assets taxes (wealth, solidarity, inheritance) compare to each other? Has this ratio changed over the past 20 years?
- How to the energy and electrical energy ("Stromsteuer") tax compare to each other?

### Methods
1: For the first question, a simple line plot showing the total tax income per year should be sufficient. This allows to both visualize the overall trend, as well as distinguishable spikes or drops in the time series.

2: The second question could be worked out in a more sophisticated way: In case the consumer goods taxes do have comparable values for each month from year to year, one could build the mean for each month. The result would be a line plot (mean value with variance around) going from Januaray to December for each of the different taxes. 
If the time series have seasonal variations, but also an interannual trend, one could still plot a line from January to December, but this time for only one tax and using the absolute values from every year for a new line. Different taxes would then need different plots.

3: The third question could be answered by computing the percentage that the air traffic tax makes of the overall tax income, which could be plotted as a simple line. One could also plot the absolute values as stacked barplots or investigate seasonal variations similar to the second question.

4: This question could be worked out similar to the third question. One could either combine the three asset taxes or use a stacked barplot, where the asset taxes have similar colors in contrast to the income tax. 

5: Since I don't exactly know how these taxes differ, I would simply plot their lines above each other first to see how they developed over time. If they show similar patterns, one could combine the two taxes and compare them to the overall tax income to find trends. 

All of these methods could probably be implemented with pandas for the data handling (and plotting) and matplotlib or seaborn for more advanced/interesting plotting