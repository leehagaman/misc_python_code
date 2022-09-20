In this inclusive nu_e low-energy excess search, seven channels are simultaneously employed in the chi2 calculation and minimization.


A. DEFINITION OF SEVEN CHANNELS
The 7 channels and corresponding number of bins (including an overflow bin for each channel) are:
-------------------------
nueCC  FC      -- 26 bins
nueCC  PC      -- 26 bins 
numuCC FC      -- 26 bins
numuCC PC      -- 26 bins
numuCC pi0 FC  -- 11 bins
numuCC pi0 PC  -- 11 bins
NC pi0 FC+PC   -- 11 bins
-------------------------
7 channels     -- 137 bins in total

nueCC/numuCC : electron/muon neutrino charged-current interaction events
FC/PC : reconstructed TPC activity fully contained/partially contained in the fiducial volume
CC/NC pi0 : charged-current or neutral-current neutrino interactions with at least one final-state pi0



B. CONTENTS OF HISTOGRAMS FOR SEVEN CHANNELS 
The predicted and measured number of events in each bin for the 7 channels are summarized in "7channelCV_MC_data.txt".

Definition of each column:
Channel        -- see A. Definitions of 7 channels

Energy (GeV)   -- reconstructed neutrino energy for nueCC and numuCC channels
               -- reconstructed pi0 kinetic energy for pi0 channels

#Bin           -- bin index for each channel; the last bin is the overflow bin

eLEEx=1        -- number of excess nue events corresponding to median MiniBooNE LEE, i.e. eLEE strengh x equal to 1.

Signal         -- predicted number of intrinsic (from beam) signal events with interaction vertices inside the fiducial volume (3 cm inward the TPC active volume)

Background     -- predicted number of background events

Data           -- measured number of events from 6.369e20 POT MicroBooNE data



C. ELEMENTS OF SYSTEMATIC UNCERTAINTY COVARIANCE MATRIX
The covariance matrix is a joint covariance matrix for 7 channels, i.e. 137 bins x 137 bins.
The bin-to-bin correlations across different channels are included.
Note that different eLEE strengths correspond to different number of nue events and the covariance matrix should change.

Files named "7channelCovariance_eLEE[xx].txt" save the elements for each covariance matrix. 
eLEE[xx] means the eLEE strengh is 0.1 times [xx], e.g., eLEE10 means the eLEE strength is 1.0.
In total 21 different covariance matrices for eLEE strenghs ranging from 0.0 to 2.0.
ATTENTION:
Only systematic uncertainty, statistical uncertainty not included.
For statistical uncertainty covariance matrix (only diagonal elements), Neyman, Pearson, or combined Neyman and Pearson (CNP) formulism can be used. In this eLEE analysis, CNP format is used and details can be found in the paper.


Bin index (last bin is overflow bin for each channel/block):
  1- 26th bins/rows/columns: nueCC FC channel
 27- 52nd bins/rows/columns: nueCC PC channel
 53- 78th bins/rows/columns: numuCC FC channel
 79-104th bins/rows/columns: numuCC PC channel
105-115th bins/rows/columns: CCpi0 FC channel
116-126th bins/rows/columns: CCpi0 PC channel
127-137th bins/rows/columns: NCpi0 channel


