# Big Data Analytics in Brazilian E-Commerce

- [ ] anticipated by Fri 11.12.2020
- [x] the preliminary zip code analysis needs calrification. Population data for example is not considered. Just the folume of sales seems to limited of an analysis
- [ ] 2 references is a bit few
- [ ] Conclusion TBD

[![Check Report](https://github.com/cybertraining-dsc/fa20-523-330/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-330/actions)
[![Status](https://github.com/cybertraining-dsc/fa20-523-330/workflows/Status/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-330/actions)
Status: in progress approved, Type: Project

Oluwatobi Bolarin, bolarint@iu.edu, [fa20-523-330](https://github.com/cybertraining-dsc/fa20-523-330/), [Edit](https://github.com/cybertraining-dsc/fa20-523-330/blob/main/project/project.md)

{{% pageinfo %}}

## Abstract

As the world begins to utilize online service and stores at greater capacity it becomes a greater priority to increase the efficiency of the various processes that are required for online stores to work effectively. By analyzing the data the comes from online purchases, a better understanding can be formed about what is needed and where as well as the quantity. This data should also allow for us to better predict what orders will be needed at future times so shortages can be avoided. 

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** economics, Brazil, money, shipping, Amazon, density

## 1. Introduction

Brazil has the largest E-commerce market in Latin America. "It has been estimated that the country accounts for over one third of the region's ecommerce market"[^2]. However, the growth of the potential e-commerce giant has problems that could potentially stunt its long-term growth. The concentration of this effort is to determine the areas the money is spent; however, this topic should expand to other countries and nations to determine locations to stores specific products. After amazon, this can be applied to many online stores or stores that have so form of digital commerce. Due to the nature of spending, this method could also be used to determine what regions of a country are in need of what items when the residents are in poverty. The amount of money that is spent can also be a strong indicator about what trends are possible and what type of goods people are willing to spend their income on. Part of the reason why this is important is due is combating shortages. The COVID pandemic showed that working global supply chains to their maximum at all times isn’t just a bad idea, it is detrimental to the citizens of their respective countries and by extension the world. Supply chains that are constantly working to their maximum capacity lives no room for emergency supplies that could be utilized in live saving applications. Examples would be masks, hospital beds, protective equipment, etc. 



## 2. Background Research and Previous Work

The study of economics is understanding the best way how to deal with scarcity. Earning a bachelor’s degree in economics didn’t feel satisfying enough due to my love for technology. Determine how resources are allocated is one of the most important decision that can be made in our modern world regardless of our region, race, occupations, or economical class.

Working in restaurants for 7 years working through undergrad the opportunity to learn numerous social and management skills. However, there would always be never ending problems present thing themselves through the day. One of the most painful ones would consistently be the fact that we would run out of things. Surplus were hardly considered acceptable and when there was a shortage the workers would pay the price. This would be understandable in places that just opened for less than a year, however in restaurants that had been in business for a while it was inexcusable. People can reason that, it was a busy day so we didn’t know that it would sell out, that a product went bad that wasn’t counted before, or someone made an ordering error. However, none of those excuses are valid in a place that has been running for a while because they should have an estimate about how much they should be growing and how much extra product they should by to ensure the fact that they don’t run out.

This is a similar issue that supply chains around the world had, except, with one problem you would have to deal with numerous angry customers and the other it was a matter of lives. This matter should increase the emphasis that we should have more relax supply chains in our world then over-worked ones. It seems that it is in worlds best interest that we start formatting our data in a more readable way for ever one to see a understand so we can do a better job of managing where we place our resources. Constantly determining what is being done well and what needs to be working on and improved. This analysis will attempt to better illustrate a better picture to determine more practical ways to increase e-commerce growth in Brazil and possible by extension this method can be superimposed on other regions of the world. 


## 3. Choice of Data-sets

After exploring a vast amount of data available, it was best to choose the following two datasets in order to analyze Amazon sales data in brazil to get an unbiased look at what sells on average.

1. [Amazon Sales Data](https://www.kaggle.com/olistbr/brazilian-ecommerce?select=olist_products_dataset.csv)[^1]

The four datasets that will speficialy be using in this file will be the "olist_customers_dataset.csv", "olist_order_items_dataset.csv", "olist_orders_dataset.csv", and "olist_products_dataset.csv". Both of the datasets are needed for this project because to obtain the location data from customers the zip code of the customer is needed for the olist_customers_dataset.csv dataset and the name of the order and specifically the category that it is in is held in the olist_order_items_dataset.csv dataset.
For this project work is done with a dataset of 100,000 that has various amazon orders ranging from basic items to more expensive and complex things. The only limiter is what was being sold on amazon at that point in time. The data set size is only 120.3 MB and markdown will be used to show the findings and the method got to them.

![Dataset Image Map](https://github.com/cybertraining-dsc/fa20-523-330/raw/main/project/images/datasetImage.png)

**Figure 1:** Database Map[^1]


The data that is used can be derived from the database map using in figure 1. The data in each data set that is necessary for this project would be the olist_customers_dataset.csv for what location the customer got their goods delivered to. This can be done with both the city that they live in and the zip code. Both should be used to see if there is going to be a notable difference between what people in entire cities will order verses specific zip codes. Then the order can be found in olist_orders_dataset.csv by matching the customer ID in the dataset olist_customers_dataset.csv. After the specific order is found we can find the specific item that was bought with the dataset olist_order_items_dataset.csv. The chain completed by using the product ID from the olist_order_items_dataset.csv and matching it with the product ID in the olist_products_dataset.csv. 

The reason why it needs to be done this way is because the information that is necessary to answer the question is too vast if people are to deal with specific items so it would be more important and helpful if we found the category of items that is necessary instead. In the end, this project deals with four different datasets in the same database that helps us connect the location of where the order is needed and being sent to the type of object that is bought.


## 4. Methodology

To correctly articulate the scope of what the dataset is measuring and the region that it is as well as when the data was collected for the project. It is also needed to come up with a viable solution for any (if there is) missing data that exists in the data set. Looking into ways that that the different data sheets interact with one another to find any patterns or factors that could exist that aren&#39;t otherwise easily seen is needed as well.

To determine the product categories that were sold in each region it is mandator that the relevant data frames were merged together through panda. When that is done it is optional to remove the data that isn’t necessary. The reason it is a necessity to merge the data sets together is because the way that it is currently organized is not helpful to the analysis that is trying to be done. The olist_order_customer_dataset contains only information about the customer ordering the objects. The Customer Dataset has no information on the item that they ordered or what. The only relative data that it has for this analysis is the Zip Code of the consumer, the City of the consumer and the State of the consumer. With all of this information we can make any size analysis base on an area as small as people in the same Zip Code to be people as large as a region by putting together multiple cities together. This concept can be utilized with any area data, so it is helpful here as well. However, the customer_id is needed to link the olist_order_customer_dataset with the olist_orders_dataset.

Although the olist_orders_dataset doesn’t have any information that directly makes it important for this analysis it does have the order_id that is linked to customer_id. Thus, the Order that the Customer made can be linked back to the customer and from the customer the location that it was ordered to. Then with the order_id, we can link the olist_order_items_dataset. Interesting things can be determined from this information.

For example, we can determine the average freight_value for any area in our data size regardless of how big. It can also be used compare that to other areas or regions to determine how much each large shipment of items should be ensured by. The same thing can also be done with the price and that can help determine economic status, although without knowing the specific type of item this type of analysis may not be accurate and, by extension, not beneficial. However, if any really meaningful analysis that will come out of this the olist_products_data set is a one of the most important sets of data that we need for this analysis. To that end, the product_id from olist_order_items_dataset needs to be linked with the product_id in the olist_products_dataset. With that the area that the products go to are linked with what the products are.

By linking the products_id to the olist_products_dataset an analysis can be done with about specific product information and the region that it is going to. The most important for this analysis, however, would be the product_category_name. This is important because the product category that is ordered can now be linked with the region that it is going to. Down to an area as small as a zip code. Ultimately, this could potential help determine how much what should be store and where to best help the customers and increase 2-day completion rates without over burdening the work force any more then necessary. From this large data frame, it can now be determining what type of products are ordered this most in what regions. If this information is utilized correctly and efficiently it can greatly reduce the stress of a supply chain. By increase the supply chain’s efficiency without increasing the load we can create slack that will be able to minimize the stress a supply chain suffers when demand is higher than usual for any reason.


## 5. Analysis

![ZIP from Python](https://github.com/cybertraining-dsc/fa20-523-330/raw/main/project/images/figure1.png)

**Figure 2:** First set of preliminary data showing zicode density

For the figure above, figure 2, this is a histogram of the various zip codes in Brazil. The problem with this chart is the fact that it doesn’t really tell you much. It doesn’t properly illustrate the density each area nor do a good job of showing exactly how many orders were made in each area. All this graph could show is the number of customers that reside in each area, but it doesn’t do that well either. What would have worked better for this would have been to first of all understand the fact that there is a lot of data that should have been broken up from the beginning. The main problem with this graph, as well as many others in the series, is the fact that it is trying to show a lot with far too little. The problem would be “solved” in a sense if, instead of showing all of the zip codes, only finding the zip codes in a part of Brazil. That would enable people to be able to see multiple different useful graphs. One graph could be made to show the number of customers per region and then a few others could be regional showing the Zip codes, states, and/or cities for each region. This would produce graphs that could inform the reader more about how many customers are living in each area. 

![Heatmap Data](https://github.com/cybertraining-dsc/fa20-523-330/raw/main/project/images/figure3.png)

**Figure 3:** Shows Heat map of all the data

For the figure above, figure 3, this is a heatmap showing all of the data. This type of graph really doesn’t make sense with the parameters that it was set with. It would have been more helpful to show, like in figure 2, the relationship between the areas and the amount of people that were in the areas. It would also be good to use it for the visualization of areas and the number of products for each area as well as how much is made revenue in each area. The problem with the current format is the fact that it is trying to incorporate strings as well as various numbers that just make all the data harder to understand.

![Sales Per City](https://github.com/cybertraining-dsc/fa20-523-330/raw/main/project/images/figure2.png)

**Figure 4:** Shows Sales per State

![Products](https://github.com/cybertraining-dsc/fa20-523-330/raw/main/project/images/figure4.png)

**Figure 5:** Histogram for different products in Brazil

![SP State Products](https://github.com/cybertraining-dsc/fa20-523-330/raw/main/project/images/figure5.png)

**Figure 6:** Histogram for products sold In SP State.




## 6. Conclusion



## 7. Acknowledgements

The author would like to thank Dr. Gregor Von Laszewski, Dr. Geoffrey Fox, and the associate instructors in the *FA20-BL-ENGR-E534-11530: Big Data Applications* course (offered in the Fall 2020 semester at Indiana University, Bloomington) for their continued assistance and suggestions with regard to exploring this idea and also for their aid with preparing the various drafts of this article.

## 8. References

[^1]: Olist. "Brazilian E-Commerce Public Dataset by Olist." Kaggle, 29 Nov. 2018, <www.kaggle.com/olistbr/brazilian-ecommerce>.

[^2]: Navarro, José Gabriel. "Topic: E-Commerce in Brazil." Statista, <www.statista.com/topics/4697/e-commerce-in-brazil/>. 
