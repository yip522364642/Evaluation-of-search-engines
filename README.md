
Performance evaluation of Baidu, Google and Bing


1 Data preparation
	Compose these 3 queries: 
query1='网络信息检索的性能评估'
query2='苹果新品发布会'
query3='2018乒乓球男子世界杯'
	Run these 3 queries on Baidu, Bing and Google search engines, and collect the top 20 documents returned by each SE. Totally, each query corresponds to 60 documents.
	Judge the relevance between query and documents. If relevant, mark 1 before the website of document. Otherwise, mark 0.
 
 
 
	Union related documents which marks 1 from three SEs as full relevant document set of the query.

2 Evaluation Procedure
For each query in 3 SEs, if the returned document is relevant to it, calculate the P/R value at this time and record the result.
P=  (|Relevant Document|)/(|Returned Document|)
R=(|Relevant Document|)/(|Full Relevant Document|)
In addition, calculate the P-value when the SE returns 20 documents so as to calculate MAP of each SE.
MAP=  (P(Baidu)+P(Bing)+P(Google))/3

3 Result Analysis
Draw a P/R graph for each query, and consider x axis as Recall Rate, y axis as Precision Rate.
 
P/R value(query1='网络信息检索的性能评估')
 
P/R value(query2='苹果新品发布会')
 
P/R value(query3='2018乒乓球男子世界杯')

MAP value: {'Baidu': 0.7000000000000001, 'Bing': 0.65, 'Google': 0.7166666666666667}
The higher the MAP value is, the better average performance SE has. As is shown above, we can conclude the performance of these 3 SEs from high to low: Google, Baidu, and Bing. Meanwhile, the MAP value of Google and Baidu is closed, but Bing’s is obviously lower. Hence, the average performance of Google and Baidu is similar and Bing’s is worse.

