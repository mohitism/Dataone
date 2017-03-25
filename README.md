# Dataone

I have used python to accomplish this.

I have taken the dictionary of <storeid,dictionary of <product,price >>.
Now for each query i am iterating each store and checking whether that store contains all the products mentioned in the given query.
If yes the ans is calculated and compared to minimum else this store is ignored. Similarly i have iterated all the stores and at last
we wil have the store id and the minimum price of the product which we want.


Take queries as input as long as query in not empty

Queries are in the form

1 teddy_bear baby_powder
2 pampers_diapers baby_soap

etc.
