import pandas as pd
import glob
import tqdm
import numpy as np

PREF ='CRIME'

def getDict(globstr):
	SRC_DIC = {}
	TGT_DIC = {}
	TGT_DIC_gammas = {}
	mean_gamma = {}
	med_gamma = {}
	for filename in tqdm.tqdm(glob.glob(globstr)):
		df = pd.read_csv(filename)
		df = df[df['gamma'] < 0.90]
		df = df[df['gamma'] > 0.01]
		#mean = df['gamma'].mean()
		#med = df['gamma'].median()


		src = list(set(df['src']))
		if len(list(set(df['tgt']))) < 1:
			continue
		tgt = list(set(df['tgt']))[0]
		#mean_gamma[tgt] = mean
		#med_gamma[tgt] = med

		SRC_DIC[tgt] = src
		file_gammas = []
		for idx,row in df.iterrows():
			s = row['src']
			gamma = row['gamma']
			if s not in TGT_DIC:
				TGT_DIC[s] = []
			if s not in TGT_DIC_gammas:
				TGT_DIC_gammas[s] = []
			TGT_DIC[s].append(gamma)
			TGT_DIC_gammas[s].append(gamma)
			file_gammas.append(gamma)

		mean_gamma[tgt] = np.mean(file_gammas)
		med_gamma[tgt] = np.median(file_gammas)

	rows = []
	for key in SRC_DIC:
		#print TGT_DIC_gammas[key]
		rows.append([key, mean_gamma[key],med_gamma[key], np.mean(TGT_DIC_gammas[key]),np.median(TGT_DIC_gammas[key]),len(SRC_DIC[key]), len(TGT_DIC[key])])
	df = pd.DataFrame(rows, columns=['variable','srcmean_gamma','srcmed_gamma','tgtmean_gamma','tgtmed_gamma','numSrc','numTgt'])
	df.to_csv(PREF + 'gamma_plots.csv',index=None)


getDict('models/*.csv')
