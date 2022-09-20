import yaml
from hepdata_tools import text as convert
from hepdata_tools import types as heptype

# Submission header
submission = heptype.Submission(
    additional_resources=[],
    comment=r"""Data release for the first results from MicroBooNE's deep learning-based search for an excess of charged-current quasi-elastic electron neutrinos, corresponding to informaiton from arXiv:2110.14080""",
)

# Energy keywords
energy_keywords = [
    heptype.Keyword(name="reactions", values=["NUE CCQE"]),
    heptype.Keyword(name="observables", values=["DN/DE"]),
    heptype.Keyword(name="phrases", values=["Neutrino LArTPC Interactions"]),
]

data_files = []

##### 200 MeV - 1200 MeV reco energy

# Constrained Prediciton

# Binning
nue_binning_file = heptype.AdditionalResource(
    location="nue_1e1p_bins.txt",
    description="1D array of bin boundaries in reconstructed neutrino energy. Given in MeV.",
    license=None,
)

# NuE Data
nue_data_file = convert.data_and_bins(
    data_file="nue_1e1p_data.txt",
    data_name=r"1e1p Sample Observation",
    bin_file="nue_1e1p_bins.txt",
    bin_name=r"$E_\nu$",
)

orig_nue_data_file = heptype.AdditionalResource(
    location="nue_1e1p_data.txt",
    description=r"1D array of observed $\nu_e$ CCQE 1e1p candidate events per reconstructed neutrino energy bin.",
    license=None,
)

# NuE background prediction
nue_bkg_file = convert.expect_and_bins(
    data_file="nue_1e1p_pred.txt",
    data_name=r"1e1p Sample Prediction (Total Background Only)",
    bin_file="nue_1e1p_bins.txt",
    bin_name=r"$E_\nu$",
)

orig_nue_bkg_file = heptype.AdditionalResource(
    location="nue_1e1p_pred.txt",
    description="1D array of predicted total background events per reconstructed neutrino energy bin.",
    license=None,
)

# NuE lee prediction
nue_lee_file = convert.expect_and_bins(
    data_file="nue_1e1p_pred_lee.txt",
    data_name=r"1e1p Sample Prediction (Total Background + LEE)",
    bin_file="nue_1e1p_bins.txt",
    bin_name=r"$E_\nu$",
)

orig_nue_lee_file = heptype.AdditionalResource(
    location="nue_1e1p_pred_lee.txt",
    description="1D array of predicted total background + LEE events per reconstructed neutrino energy bin.",
    license=None,
)

# NuMu Background Fit
numu_bkg_file = convert.expect_and_bins(
    data_file="nue_1e1p_bkg.txt",
    data_name=r"1e1p Sample $\nu_\mu$ Background Prediction (from Empirical Fit)",
    bin_file="nue_1e1p_bins.txt",
    bin_name=r"$E_\nu$",
)

orig_numu_bkg_file = heptype.AdditionalResource(
    location="nue_1e1p_bkg.txt",
    description="1D array of predicted muon neutrino background events (from emprical Landau+linear fit) per reconstructed neutrino energy bin.",
    license=None,
)

data_files.append(heptype.InlineResource(
    name="NuE data and background (+ LEE) prediction",
    description="Observed NuE data and background (+ LEE) prediction, including the muon neutrino background prediction from the empirical fit, for arXiv:2110.14080. The prediction incorporates the constraint from the 1mu1p sample",
    keywords=energy_keywords,
    independent_variables=nue_data_file.independent_variables,
    dependent_variables=(nue_data_file.dependent_variables + nue_bkg_file.dependent_variables + nue_lee_file.dependent_variables + numu_bkg_file.dependent_variables),
    data_license=None,
    additional_resources=[orig_nue_data_file, orig_nue_bkg_file, orig_nue_lee_file, orig_numu_bkg_file, nue_binning_file],
))

# Background fractional covariance matrix (systematic uncertainty only)
nue_bkg_frac_cov_file = convert.cov_and_bins(
    data_file="nue_1e1p_cov.txt",
    data_name=r"$\sigma_\text{bkg}^2/\mu_\text{bkg}$",
    bin_file="nue_1e1p_bins.txt",
    bin_name=r"$E_\nu$",
)

orig_nue_bkg_frac_cov_file = heptype.AdditionalResource(
    location="nue_1e1p_cov.txt",
    description="2D array of (systematic uncertainty only) predicted background fractional covariance matrix per reconstructed neutrino energy bins after the 1mu1p constraint.",
    license=None,
)

data_files.append(heptype.InlineResource(
    name="NuE background constrained fractional covariance matrix",
    description="NuE background fractional covariance matrix after the 1mu1p constraint from arXiv:2110.14080",
    keywords=energy_keywords,
    independent_variables=nue_bkg_frac_cov_file.independent_variables,
    dependent_variables=nue_bkg_frac_cov_file.dependent_variables,
    data_license=None,
    additional_resources=[orig_nue_bkg_frac_cov_file, nue_binning_file],
))

# LEE fractional covariance matrix (systematic uncertainty only)
nue_lee_frac_cov_file = convert.cov_and_bins(
    data_file="nue_1e1p_cov_lee.txt",
    data_name=r"$\sigma_\text{lee}^2/\mu_\text{lee}$",
    bin_file="nue_1e1p_bins.txt",
    bin_name=r"$E_\nu$",
)

orig_nue_lee_frac_cov_file = heptype.AdditionalResource(
    location="nue_1e1p_cov_lee.txt",
    description="2D array of (systematic uncertainty only) predicted LEE fractional covariance matrix per reconstructed neutrino energy bins after the 1mu1p constraint.",
    license=None,
)

data_files.append(heptype.InlineResource(
    name="NuE background+LEE constrained fractional covariance matrix",
    description="NuE background+LEE fractional covariance matrix after the 1mu1p constraint from arXiv:2110.14080",
    keywords=energy_keywords,
    independent_variables=nue_lee_frac_cov_file.independent_variables,
    dependent_variables=nue_lee_frac_cov_file.dependent_variables,
    data_license=None,
    additional_resources=[orig_nue_lee_frac_cov_file, nue_binning_file],
))

# Background fractional covariance matrix pre constraint (systematic uncertainty only)
nue_bkg_frac_cov_nom_file = convert.cov_and_bins(
    data_file="nue_1e1p_cov_nom.txt",
    data_name=r"$\sigma_\text{bkg}^2/\mu_\text{bkg}$",
    bin_file="nue_1e1p_bins.txt",
    bin_name=r"$E_\nu$",
)

orig_nue_bkg_frac_cov_nom_file = heptype.AdditionalResource(
    location="nue_1e1p_cov_nom.txt",
    description="2D array of (systematic uncertainty only) predicted background fractional covariance matrix per reconstructed neutrino energy bins before the 1mu1p constraint.",
    license=None,
)

data_files.append(heptype.InlineResource(
    name="NuE background nominal fractional covariance matrix",
    description="NuE background fractional covariance matrix before the 1mu1p constraint from arXiv:2110.14080",
    keywords=energy_keywords,
    independent_variables=nue_bkg_frac_cov_nom_file.independent_variables,
    dependent_variables=nue_bkg_frac_cov_nom_file.dependent_variables,
    data_license=None,
    additional_resources=[orig_nue_bkg_frac_cov_nom_file, nue_binning_file],
))

# LEE fractional covariance matrix pre constraint (systematic uncertainty only)
nue_lee_frac_cov_nom_file = convert.cov_and_bins(
    data_file="nue_1e1p_cov_nom_lee.txt",
    data_name=r"$\sigma_\text{lee}^2/\mu_\text{lee}$",
    bin_file="nue_1e1p_bins.txt",
    bin_name=r"$E_\nu$",
)

orig_nue_lee_frac_cov_nom_file = heptype.AdditionalResource(
    location="nue_1e1p_cov_nom_lee.txt",
    description="2D array of (systematic uncertainty only) predicted LEE fractional covariance matrix per reconstructed neutrino energy bins before the 1mu1p constraint.",
    license=None,
)

data_files.append(heptype.InlineResource(
    name="NuE background+LEE nominal fractional covariance matrix",
    description="NuE background+LEE fractional covariance matrix before the 1mu1p constraint from arXiv:2110.14080",
    keywords=energy_keywords,
    independent_variables=nue_lee_frac_cov_nom_file.independent_variables,
    dependent_variables=nue_lee_frac_cov_nom_file.dependent_variables,
    data_license=None,
    additional_resources=[orig_nue_lee_frac_cov_nom_file, nue_binning_file],
))

# NuE monte-carlo
nue_simulation_file = convert.ntuple(
    fname="nue_eventlist.txt",
    column_names=[
        r"$E_\nu$",
        r"$E_\nu^{\rm True}$",
        r"weight",
    ],
    column_units=[
        "MeV",
        "MeV",
        "Counts in 6.67e20 POT",
    ],
    is_independent=[
        False,
        True,
        False,
    ],
)

orig_nue_simulation_file = heptype.AdditionalResource(
    location="nue_eventlist.txt",
    description="ntuple file of 7609 predicted electron neutirno events, containing information on reconstructed neutrino energy, true neutrino energy and event weight (scaled to 6.67e20 POT) for each event.",
    license=None,
)

data_files.append(heptype.InlineResource(
    name="NuE simulation",
    description="""NuE simulation from arXiv:2110.14080""",
    keywords=energy_keywords,
    independent_variables=nue_simulation_file.independent_variables,
    dependent_variables=nue_simulation_file.dependent_variables,
    data_license=None,
    additional_resources=[orig_nue_simulation_file],
))



outdir = "./release/"

submission_file = [submission]

for i, data in enumerate(data_files):
    fname = "data_%d.yaml" % i
    d = data._asdict()
    d.update({"data_file": fname})
    del d["dependent_variables"]
    del d["independent_variables"]
    ex = heptype.LinkedResource(**d)
    submission_file.append(ex)
    data_file = heptype.DataFile(independent_variables=data.independent_variables, dependent_variables=data.dependent_variables)
    with open(outdir + fname, "w") as f:
        yaml.safe_dump(data_file.to_py(), stream=f)


submission_file = [x.to_py() for x in submission_file]

with open(outdir + "submission.yaml", "w") as f:
    yaml.safe_dump_all(submission_file, stream=f)

