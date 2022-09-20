import yaml
import numpy as np

# Function for calculating the CNP chi square errors, to be added to each diagonal bin of the covariance matrices, where
# M = observation
# mu = prediction 
def cov_cnp(M,mu):
  cov=0
  if mu > 0:
    if M != 0:
      cov = (3. / (2. / mu + 1. / M))
    else:
      cov = mu/2.
    return cov

yamlDir = "HEPData_yamls" # Modify this to wherever your .yaml files are saved

yaml_dict = {}

# load constrained distributions
with open(yamlDir+"/HEPData-114859-v1-NuE_data_and_background_(+_LEE)_constrained_prediction.yaml", "r") as stream:
  try:
    yaml_dict["constr_dist"] = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

# load unconstrained distributions
with open(yamlDir+"/HEPData-114859-v1-NuE_data_and_background_(+_LEE)_unconstrained_prediction.yaml", "r") as stream:
  try:
    yaml_dict["unconstr_dist"] = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

# load constrained background-only covariance matrix
with open(yamlDir+"/HEPData-114859-v1-NuE_background_constrained_fractional_covariance_matrix.yaml", "r") as stream:
  try:
    yaml_dict["constr_cov_bkg"] = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

# load constrained background+LEE covariance matrix
with open(yamlDir+"/HEPData-114859-v1-NuE_background+LEE_constrained_fractional_covariance_matrix.yaml", "r") as stream:
  try:
    yaml_dict["constr_cov_lee"] = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

# load unconstrained background-only covariance matrix
with open(yamlDir+"/HEPData-114859-v1-NuE_background_unconstrained_fractional_covariance_matrix.yaml", "r") as stream:
  try:
    yaml_dict["unconstr_cov_bkg"] = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

# load unconstrained background+LEE covariance matrix
with open(yamlDir+"/HEPData-114859-v1-NuE_background+LEE_unconstrained_fractional_covariance_matrix.yaml", "r") as stream:
  try:
    yaml_dict["unconstr_cov_lee"] = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)


# turn the loaded yaml infromation into numpy arrays

# lists to store information
dat_arr = []
mc_arr = []
lee_arr = []
bkg_arr = []
dat_err_low = []
dat_err_high = []
bins_low = []
bins_high = []
mc_arr_nom = []
lee_arr_nom = []

# list-ize constrained distributions and binning/data
for i in range(len(yaml_dict["constr_dist"]['dependent_variables'][0]['values'])):
  dat_arr.append(yaml_dict["constr_dist"]['dependent_variables'][0]['values'][i]['value'])
  mc_arr.append(yaml_dict["constr_dist"]['dependent_variables'][1]['values'][i]['value'])
  lee_arr.append(yaml_dict["constr_dist"]['dependent_variables'][2]['values'][i]['value'])
  bkg_arr.append(yaml_dict["constr_dist"]['dependent_variables'][3]['values'][i]['value'])
  dat_err_low.append(-1*yaml_dict["constr_dist"]['dependent_variables'][0]['values'][i]['errors'][0]['asymerror']['minus'])
  dat_err_high.append(yaml_dict["constr_dist"]['dependent_variables'][0]['values'][i]['errors'][0]['asymerror']['plus'])
for i in range(len(yaml_dict["constr_dist"]['independent_variables'][0]['values'])):
  bins_low.append(yaml_dict["constr_dist"]['independent_variables'][0]['values'][i]['low'])
  bins_high.append(yaml_dict["constr_dist"]['independent_variables'][0]['values'][i]['high'])
bins = bins_low + [bins_high[-1]]
bins_centers = 0.5*(np.array(bins_low)+np.array(bins_high))

# list-ize unconstrained predictions
for i in range(len(yaml_dict["unconstr_dist"]['dependent_variables'][0]['values'])):
  mc_arr_nom.append(yaml_dict["unconstr_dist"]['dependent_variables'][1]['values'][i]['value'])
  lee_arr_nom.append(yaml_dict["unconstr_dist"]['dependent_variables'][2]['values'][i]['value'])

# list-ize constrained background-only covariance matrix
covm = []
for i in range(len(bins_centers)**2):
    covm.append(yaml_dict["constr_cov_bkg"]['dependent_variables'][0]['values'][i]['value'])
# reshape and scale to the full covariance matrix
covm = np.array(covm).reshape((len(bins_centers),len(bins_centers)))
covm*=np.outer(np.array(mc_arr),np.array(mc_arr))
# add CNP error to diagonal covariance
for i in range(len(bins_centers)): covm[i,i] += cov_cnp(dat_arr[i],mc_arr[i])

# list-ize constrained background+lee covariance matrix
lee_covm = []
for i in range(len(bins_centers)**2):
    lee_covm.append(yaml_dict["constr_cov_lee"]['dependent_variables'][0]['values'][i]['value'])
# reshape and scale to the full covariance matrix
lee_covm = np.array(lee_covm).reshape((len(bins_centers),len(bins_centers)))
lee_covm*=np.outer(np.array(lee_arr),np.array(lee_arr))
# add CNP error to diagonal covariance
for i in range(len(bins_centers)): lee_covm[i,i] += cov_cnp(dat_arr[i],lee_arr[i])

# list-ize unconstrained background-only covariance matrix
covm_nom = []
for i in range(len(bins_centers)**2):
    covm_nom.append(yaml_dict["unconstr_cov_bkg"]['dependent_variables'][0]['values'][i]['value'])
# reshape and scale to the full covariance matrix
covm_nom = np.array(covm_nom).reshape((len(bins_centers),len(bins_centers)))
covm_nom*=np.outer(np.array(mc_arr_nom),np.array(mc_arr_nom))
# add CNP error to diagonal covariance
for i in range(len(bins_centers)): covm_nom[i,i] += cov_cnp(dat_arr[i],mc_arr_nom[i])

# list-ize unconstrained background+lee covariance matrix
lee_covm_nom = []
for i in range(len(bins_centers)**2):
    lee_covm_nom.append(yaml_dict["unconstr_cov_lee"]['dependent_variables'][0]['values'][i]['value'])
# reshape and scale to the full covariance matrix
lee_covm_nom = np.array(lee_covm_nom).reshape((len(bins_centers),len(bins_centers)))
lee_covm_nom*=np.outer(np.array(lee_arr_nom),np.array(lee_arr_nom))
# add CNP error to diagonal covariance
for i in range(len(bins_centers)): lee_covm_nom[i,i] += cov_cnp(dat_arr[i],lee_arr_nom[i])


print('Unconstrained Chi Squares (H0, without LEE) (H1, with LEE)')
# Chi square calculation 200-500 MeV
mask1D = np.where(bins_centers<550,True,False)
mask2D = np.outer(mask1D,mask1D)
Del_H0 = (np.array(mc_arr_nom) - np.array(dat_arr))[mask1D]
Del_H1 = (np.array(lee_arr_nom) - np.array(dat_arr))[mask1D]
chi2_H0 = np.matmul(np.matmul(Del_H0,np.linalg.inv(covm_nom[mask2D].reshape(len(Del_H0),len(Del_H0)))),Del_H0)
chi2_H1 = np.matmul(np.matmul(Del_H1,np.linalg.inv(lee_covm_nom[mask2D].reshape(len(Del_H1),len(Del_H1)))),Del_H1)
print('200-500 MeV:',chi2_H0,chi2_H1)

# Chi square calculation 200-1200 MeV
Del_H0 = np.array(mc_arr_nom) - np.array(dat_arr)
Del_H1 = np.array(lee_arr_nom) - np.array(dat_arr)
chi2_H0 = np.matmul(np.matmul(Del_H0,np.linalg.inv(covm_nom)),Del_H0)
chi2_H1 = np.matmul(np.matmul(Del_H1,np.linalg.inv(lee_covm_nom)),Del_H1)
print('200-1200 MeV:',chi2_H0,chi2_H1)

print('Constrained Chi Squares (H0, without LEE) (H1, with LEE)')
# Chi square calculation 200-500 MeV
mask1D = np.where(bins_centers<550,True,False)
mask2D = np.outer(mask1D,mask1D)
Del_H0 = (np.array(mc_arr) - np.array(dat_arr))[mask1D]
Del_H1 = (np.array(lee_arr) - np.array(dat_arr))[mask1D]
chi2_H0 = np.matmul(np.matmul(Del_H0,np.linalg.inv(covm[mask2D].reshape(len(Del_H0),len(Del_H0)))),Del_H0)
chi2_H1 = np.matmul(np.matmul(Del_H1,np.linalg.inv(lee_covm[mask2D].reshape(len(Del_H1),len(Del_H1)))),Del_H1)
print('200-500 MeV:',chi2_H0,chi2_H1)

# Chi square calculation 200-1200 MeV
Del_H0 = np.array(mc_arr) - np.array(dat_arr)
Del_H1 = np.array(lee_arr) - np.array(dat_arr)
chi2_H0 = np.matmul(np.matmul(Del_H0,np.linalg.inv(covm)),Del_H0)
chi2_H1 = np.matmul(np.matmul(Del_H1,np.linalg.inv(lee_covm)),Del_H1)
print('200-1200 MeV:',chi2_H0,chi2_H1)
