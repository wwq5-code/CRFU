

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


x=[1, 2, 3, 4, 5]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['2%', '4%', '6%', '8%', '10%' ]
# unl_fr = [97.62, 97.6, 97.6, 97.52, 97.45 ]
unl_br = [52.62, 53.3, 50.4, 49.825, 49.6 ]
unl_vibu = [57.17, 55.92, 52.67, 52.062, 53.27]

# unl_br = [93.17, 92.7, 93.18, 93.14, 95.68 ]
# unl_vibu = [93.85, 93.23, 94.7, 93.91, 95.95  ]
#unl_self_r = [97.58, 97.44, 97.44, 97.3, 97.42 ]
unl_hess_r = [52.87,  53.81, 50.53, 50.27, 50.88  ]




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

# plt.plot(x, y_sa03, color='r',  marker='2',  label='AAAI21 A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_sa05, color='darkblue',  marker='4',  label='AAAI21 A_acc, pr=0.5',linewidth=3, markersize=8)
# plt.plot(x, y_ma03, color='darkviolet',  marker='3',  label='FedMC A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_ma05, color='cyan',  marker='p',  label='FedMC A_acc, pr=0.5',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Accuracy (%)' ,fontsize=20)
my_y_ticks = np.arange(40, 61, 5)
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
plt.savefig('stl10_acc_er_curve.pdf', format='pdf', dpi=200)
plt.show()