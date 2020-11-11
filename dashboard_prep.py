'''
dashboard preparation code
'''
import ingest_scielo
import pickle
import networkx as nx

df = ingest_scielo.ingest_wos_scielo_folder()
authors, papers, institutions = ingest_scielo.get_scielo_dicts(df)

data_dict = {'authors_dict':authors,
             'papers_dict':papers,
             'institutions_dict':institutions}

filehandler = open('data_pickle.pkl','wb')
pickle.dump(data_dict, filehandler)
