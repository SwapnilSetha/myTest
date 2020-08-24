import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn import datasets


np.random.seed(0)
feature_set, labels = datasets.make_moons(100, noise=0.10)

"""plt.figure(figsize=(10,7))
plt.scatter(feature_set[:,0], feature_set[:,1], c=labels, cmap=plt.cm.winter)"""

feature_set.shape
labels = labels.reshape(100, 1)
labels.shape
lr = 0.07


def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_der(x):
    return sigmoid(x) * (1-sigmoid(x))


def forward_propogation(feature_set, wh1, wh2, wo):
    zh1 = np.dot(feature_set, wh1)
    ah1 = sigmoid(zh1)

    zh2 = np.dot(ah1, wh2)
    ah2 = sigmoid(zh2)

    zo = np.dot(ah2, wo)
    ao = sigmoid(zo)

    return {"ao": ao, "zo": zo, "ah2": ah2, "zh2": zh2, "ah1": ah1, "zh1": zh1}


def backward_propogation(c, labels, wh1, wh2, wo):
    dcost_dao = c["ao"] - labels
    dao_dzo = sigmoid_der(c["zo"])
    dzo_dwo = c["ah2"]
    dcost_wo = np.dot(dzo_dwo.T, dcost_dao * dao_dzo)

    # phase2

    dcost_dzo = dcost_dao * dao_dzo
    dzo_dah2 = wo

    dcost_dah2 = np.dot(dcost_dzo, dzo_dah2.T)
    dah2_dzh2 = sigmoid_der(c["zh2"])
    dzh2_dwh2 = c["ah1"]
    dcost_wh2 = np.dot(dzh2_dwh2.T, dah2_dzh2 * dcost_dah2)

    # phase3

    dcost_dzh2 = dcost_dah2 * dah2_dzh2
    dzh2_dah1 = wh2

    dcost_dah1 = np.dot(dcost_dzh2, dzh2_dah1.T)
    dah1_dzh1 = sigmoid_der(c["zh1"])
    dzh1_dwh1 = feature_set
    dcost_wh1 = np.dot(dzh1_dwh1.T, dah1_dzh1 * dcost_dah1)

    # Update Weights ================

    wh1 -= lr * dcost_wh1
    wh2 -= lr * dcost_wh2
    wo -= lr * dcost_wo

    return {"wh1": wh1, "wh2": wh2, "wo": wo}


def iterations():

    wh1 = np.random.rand(len(feature_set[0]), 4)
    wh2 = np.random.rand(4, 4)
    wo = np.random.rand(4, 1)

    losses = []

    for epoch in range(20000):
        # Feed Forward

        c = forward_propogation(feature_set, wh1, wh2, wo)

        b = backward_propogation(c, labels, wh1, wh2, wo)

        wh1, wh2, wo = b["wh1"], b["wh2"], b["wo"]

        # backward propogation Phase1
        error_out = ((1 / 2) * (np.power((c["ao"] - labels), 2)))
        m = labels.shape

        if epoch % 100 == 0:

            y_hat = np.reshape(c['ao'], 100)
            y_true = np.reshape(labels, 100)
            print('Loss after iteration', epoch, ':', error_out.sum())
            print('Accuracy after iteration', epoch, ':', accuracy_score(
                y_pred=y_hat.round(), y_true=y_true)*100, '%')
            losses.append(accuracy_score(
                y_pred=y_hat.round(), y_true=y_true)*100)
            plt.plot(losses)
