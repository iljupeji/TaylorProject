This code is for learning purpouses, and because use token, the data should be replace with the user token.

The logic behind the code for scrapping is the next one:
1. Open the virtual computer.
2. Stablish the connection with kworb.
3. There are two cases:
    a) If there's already a table with the streamings, look inside the table the "song" in order to add another column with the new streamings.
    b) If there's not a table, create the table with the songs and streamings.
4. Print the table in a csv file.
5. Automatic commit to the repository.