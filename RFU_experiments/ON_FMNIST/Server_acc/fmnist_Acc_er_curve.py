

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


x=[1, 2, 3, 4, 5]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['2%', '4%', '6%', '8%', '10%' ]
unl_fr = [87.93, 87.91, 88.4, 88.4, 88.4 ]
unl_br = [81.11,    81.54, 81.02, 81.67, 80.69 ]
unl_vibu = [83.5, 84.19, 82.96, 83.58, 81.41 ]



# unl_br = [78,    81.54, 83.76, 83.33, 80.55 ]
# unl_vibu = [82.5, 83.75, 85.01, 83.9, 81.32 ]
#unl_self_r = [97.58, 97.44, 97.44, 97.3, 97.42 ]
unl_hess_r = [74.7,75.43, 76.13, 73.27, 72.12 ]




plt.figure()
l_w=4.5
m_s=12
#plt.figure(figsize=(8, 5.3))
#plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=4, markersize=10)
plt.plot(x, unl_vibu, color='g',  marker='d',  label='RFU',linewidth=l_w,  markersize=m_s)

plt.plot(x, unl_br, color='orange',  marker='x',  label='VBU',linewidth=l_w,  markersize=m_s)
#plt.plot(x, unl_self_r, color='g',  marker='*',  label='RFU-SS',linewidth=4, markersize=10)
plt.plot(x, unl_hess_r, color='r',  marker='p',  label='HBU',linewidth=l_w, markersize=m_s)
#plt.plot(x, unl_self_r, color='g',  marker='*',  label='RFU-SS',linewidth=4, markersize=10)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Accuracy (%)' ,fontsize=20)
my_y_ticks = np.arange(72 ,88,2)
plt.yticks(my_y_ticks,fontsize=20)
plt.xlabel('$\it{EDR}$' ,fontsize=20)

plt.xticks(x, labels, fontsize=20)
# plt.title('CIFAR10 IID')
plt.legend(loc='best',fontsize=20)
plt.tight_layout()
#plt.title("MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('fmnist_acc_er_curve.png', dpi=200)
plt.show()