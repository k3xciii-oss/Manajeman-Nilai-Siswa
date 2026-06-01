import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


data = pd.read_csv("data_siswa.csv")

# dataset
X = data[['kehadiran', 'rata_nilai']]
y = data['lulus']

# split data train & test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
def prediksi(kehadiran, rata_nilai):
    siswa = [[kehadiran, rata_nilai]]
    hasil = model.predict(siswa)
    if hasil[0] == 1:
        return 'Diprediksi LULUS'
    else:
        return 'Diprediksi TIDAK LULUS'

