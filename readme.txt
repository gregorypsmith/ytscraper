--- YOUTUBE WEB SCRAPER: HOW TO USE ---

1) Go to YouTube.

2) Type in the desired search query.

3) Click Filter > Video (under Type)

4) Click Enter

5) Copy and paste the search link

6) In terminal, navigate to the directory where scrape.py is located

7) Ensure that you have python3, pandas, and selenium installed (if not use pip install)

7) run the following command:

# python3 scrape.py <minsubcount> <maxsubcount> <readfile> <writefile> <link>
# where:
# minsubcount = minimum number of subscribers a channel needs to be added to the list
# maxsubcount = maximum number of subscribers a channel needs to be added to the list
# readfile = the file to be read from. must end in .csv. Useful so that creators who show up for multiple queries
#            are not added multiple times
# writefile = the file to write to. must end in .csv. Can be the same as readfile.
# link = the link you just copied and pasted

8) A new Chrome window will appear. You may need to give selenium permission to control your browser

9) When the winow appears, scroll down to load more search results (the program starts running after 10s)

10) The (unique) results of your query will appear in creator_list.csv