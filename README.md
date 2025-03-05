FOR MIE-14 group work Prescribing dashboard The dashboard aims to offer healthcare professionals a comprehensive view of prescription patterns, medication cost trends, and patient treatments. 
It provides insights by analyzing total prescription items, average medication costs, top prescribed items,ect. 
This information assists doctors in making informed decisions considering cost-effectiveness and patient needs. 
Additionally, specialized tools such as infection treatment drug analysis and a Creatinine clearance calculator are included to optimize medical decisions and resource allocation.

Our team Our team is Group 14, composed of Xinyu Fan, Wenxin Zhang, Muying Zhao, Xiaoyan Ma and Huoding Zhang. 
In three sprints, we rotated roles as Product Owner, Scrum Master and Development Team. Using a one-branch-per-person Git strategy, we construct the dashboard together.

Features: 
1.The total items of the prescribed drugs. 
2.The average ACT cost. 
3.The description of top prescribed item and its percentage of all prescriptions. 
4.The number of unique items in the dataset. 
5.Creatinine clearance calculator to assess the patient kidney health. 
6.About popup: detail the purpose of the dashboard and details our team. 
7.Infection treatment drug as % of all infection treatments: shows the percentage of'Antibacterials','Antifungal','Antiviral', 'Antiprotozoal', 'Anthelminics' five drug groups out of all infection treatments. 
8.Search box: users can search for a drug by name or BNF code. 
9. The bar chart displays the total number of prescribed antibiotics for each GP practice in a selected PCT. 
10. The Generate report menu: click it and it will generate a downloadable summary of the information represented in the dashboard.

How to add code (process): 
1.Database/models.py : transform database’s data to object 
2.Database/controller.py : write the functions calculate the results that need (use the data in database to calculate the results that we need) 
3.View/controllers.py : generate the data for the four home page tiles(by using the functions that we write in Database/controller.py) 
4.Templates/dashboard/index.html : show data(we generate the data in View/controllers.py) on dashboard 
5.Tests/test_database.py : Test whether the results that we calculated are correct
