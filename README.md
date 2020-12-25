# IndexedDB



### Evaluation

#### Extendible Hashing

| Method     | Table Name | Data Size | Table Attributes           | Time of Index's Construction | Time of Program's Execution    |
| ---------- | ---------- | --------- | -------------------------- | ---------------------------- | ------------------------------ |
| Extendible | gen_data   | 10,000    | id \| str1 \| str2 \| str3 | 21.4972 s                    | 1.1921*10^{-5} s               |
| Normal     | gen_data   | 10,000    | id \| str1 \| str2 \| str3 | 0                            | 0.0063 s                       |



### Reference

- [Extendible Hasing for COSC 311](https://emunix.emich.edu/~shaynes/Papers/ExtendibleHashing/extendibleHashing.html)
