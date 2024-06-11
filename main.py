import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt 
import nibabel as nib

#Conversion d'image nifti en numpy array en 3d
input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w = nib.load(r"/envau/work/meca/users/2024_Kamal/real_data/lastest_nesvor/sub-0001_ses-0001_acq-haste_rec-nesvor_desc-aligned_T2w.nii.gz")
input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w = input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w.get_fdata()

# On swap l'image
input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w_rot = np.transpose(input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w, (0,1,2))[::-1, ::1, ::-1]

#dimension de l'image
dim_sub_0001 = np.shape(input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w_rot)
print("lesexport dimensions de notre image :", dim_sub_0001)
#On selectionne plusieurs tranche de cette objet 3d pour en affiche le swapping
# tranche z = 74
tranche_z = input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w[:, :, 74]
tranche_z_rot = input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w_rot[:, :, 74]
#tranche y = 74
tranche_y = input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w[:, 74, :]
tranche_y_rot = input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w_rot[:, 74, :]
#tranche x = 74
tranche_x = input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w[74,:,:]
tranche_x_rot = input_sub_0001_ses_0001_acq_haste_rec_nesvor_desc_aligned_T2w_rot[74,:,:]

#Affichage
plt.imshow(tranche_z)
plt.title("tranche z image origin")
plt.show()
plt.imshow(tranche_z_rot)
plt.title("tranche z rot image origin")
plt.show()
plt.imshow(tranche_y)
plt.title("tranche y image origin")
plt.show()
plt.imshow(tranche_y_rot)


plt.title("tranche y rot image origin")
plt.show()
plt.imshow(tranche_x)

plt.title("tranche x  image origin")
plt.show()
plt.imshow(tranche_x_rot)

plt.title("tranche x rot image origin")
plt.show()
