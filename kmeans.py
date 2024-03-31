import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class KMeans:
    def __init__(self, N, iterations=500):
        self.N = N
        self.iterations = iterations

    def fit(self, X):
        self.centers = X[np.random.choice(X.shape[0], self.N, replace=False)]
        
        for _ in range(self.iterations):
            labels = self._assign_labels(X)
            
            new_centers = self._update_centers(X, labels)
            
            if np.all(self.centers == new_centers):
                break
                
            self.centers = new_centers

    def _assign_labels(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centers, axis=2)
        
        return np.argmin(distances, axis=1)
    
    def _update_centers(self, X, labels):
        new_centers = np.array([X[labels == i].mean(axis=0) for i in range(self.N)])
        return new_centers

df = pd.read_csv("Salary_data.csv",delimiter=",",encoding='utf-8')

kmeans = KMeans(N=4)

X = df[['YearsExperience','Salary']].values
kmeans.fit(X)

labels = kmeans._assign_labels(X)

df['Cluster'] = labels

print("Cluster Assignments:", labels)
print("Final centers:", kmeans.centers)

df1 = df[df.Cluster==0]
df2 = df[df.Cluster==1]
df3 = df[df.Cluster==2]
df4 = df[df.Cluster==3]
plt.scatter(df1.YearsExperience,df1['Salary'],color='green',marker='*',label = 'Salary')
plt.scatter(df2.YearsExperience,df2['Salary'],color='red',marker='*',label = 'Salary')
plt.scatter(df3.YearsExperience,df3['Salary'],color='black',marker='*',label = 'Salary')
plt.scatter(df4.YearsExperience,df4['Salary'],color='blue',marker='*',label = 'Salary')

plt.scatter(kmeans.centers[:,0],kmeans.centers[:,1],color = 'purple',marker = '*',label = 'centeroid')

plt.xlabel('Year of experience')
plt.ylabel('Salary')
plt.legend()
plt.show()