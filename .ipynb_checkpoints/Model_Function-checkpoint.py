{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "64.92"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import pickle\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "\n",
    "def price_estimator(features):\n",
    "    with open('Model.sav', 'rb') as f:\n",
    "        model = pickle.load(f)\n",
    "    return model.predict(features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  449,   328,  5196,  4755,   158,   800,  1009,  1658,  5000,\n",
       "          43,    71,    50,   195,  5890, 24382,   281,   281,   281,\n",
       "           0,   100,     7,    58,     0,     0,     0,   269,   269,\n",
       "         269,  1035,    97,     0,   229,     0,     0,     0,   267,\n",
       "         267,   267,   971,    63,     1,   309,     0,     0,     0,\n",
       "         273,   273,   273,  1039,    75,     1,    21,     0,     0,\n",
       "           0,   270,   270,   270,  1001,    77,     1,    62,     0,\n",
       "           0,     0,  2015,     1,     1,     0])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features = np.array([449,328,5196,4755,158,800,1009,1658,5000,43,71,50,195,5890,24382,281,281,281,0,100,7,58,0,0,0,269,269,269,1035,97,0,229,0,0,0,267,267,267,971,63,1,309,0,0,0,273,273,273,1039,75,1,21,0,0,0,270,270,270,1001,77,1,62,0,0,0,2015,1,1,0])\n",
    "features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([42.81])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "price_estimator(features.reshape(1, -1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
