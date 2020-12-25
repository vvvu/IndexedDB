# IndexedDB



### Evaluation

#### Extendible Hashing

| Method     | Table Name | Data Size | Table Attributes           | Time of Index's Construction | Time of Program's Execution    |
| ---------- | ---------- | --------- | -------------------------- | ---------------------------- | ------------------------------ |
| Extendible | gen_data   | 10,000    | id \| str1 \| str2 \| str3 | $21.4972 \text{ s}$          | $1.1921\times10^{-5}\text{ s}$ |
| Normal     | gen_data   | 10,000    | id \| str1 \| str2 \| str3 | 0                            | $0.0063 \text{ s}$             |



### Reference

- [Extendible Hasing for COSC 311](https://emunix.emich.edu/~shaynes/Papers/ExtendibleHashing/extendibleHashing.html)