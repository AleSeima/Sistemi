vet = [1, 7, 0, 9, 8]
dim = len(vet) 

for k in range(dim-1):                              # for (int k = 0; k < dim - 1; k++) {
    for j in range (dim-k-1):                       # for (int j = 0, j < dim - k - 1; j++) {
        if vet[j] > vet[j+1]:                       # if (vet[j] > vet[j+1]) {
            vet[j], vet[j+1] = vet[j+1], vet[j]     # funzione scambio

for l in range (dim):                               # for (int l = 0; l < dim; l++) {
    print ("%d" %vet[l])