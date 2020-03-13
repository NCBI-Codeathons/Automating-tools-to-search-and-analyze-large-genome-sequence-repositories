import sys
import pandas as pd
from dateutil import parser
import datetime
import numpy as np
import json

def srameta2nsmeta(table_file,ref_file,out_file):
	nsmeta=pd.DataFrame(columns=['strain','virus','gisaid_epi_isl','genbank_accession','date','region','country','division','division_exposure','location','segment','length','host','age','sex','originating_lab','submitting_lab','authors','url','title'])
	srameta=pd.read_csv(table_file)
	nsmeta['strain']=srameta['m_acc']
	nsmeta['virus']='ncov'
	dates=[str(parser.parse(date,default=datetime.datetime(1000,1,1))) for date in srameta['m_collection_date_sam']]
	dates=[date.split(' ')[0] for date in dates]
	nsmeta['date']=pd.Series(dates)
	nsmeta['division']='Unknown'
	nsmeta['division_exposure']='Unknown'
	nsmeta['location']='Unknown'
	nsmeta['region']=srameta['m_geo_loc_name_country_continent_calc']
	nsmeta['country']=srameta['m_geo_loc_name_country_calc']
	nsmeta=nsmeta.fillna('?')
	refmeta=pd.read_csv(ref_file,sep='\t')
	nsmeta=pd.concat([nsmeta,refmeta],axis=0,sort=False)
	nsmeta=nsmeta.drop('Unnamed: 20', axis=1)
	nsmeta.to_csv(out_file,sep='	',index=False)
	return nsmeta



def makeconfig(name_config,nsmeta):
	accessions={'samples':list(nsmeta['strain'])}
	print(accessions)
	with open(name_config,'w') as jsonfile:
		json.dump(accessions,jsonfile)

if __name__=="__main__":

	table_file=sys.argv[1]
	ref_file=sys.argv[2]
	out_file=sys.argv[3]
	name_config=sys.argv[3]
	nsmeta=srameta2nsmeta(table_file,ref_file,out_file)
	makeconfig(name_config,nsmeta)
