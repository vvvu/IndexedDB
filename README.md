# IndexedDB



### Evaluation

#### Linear Hash
| Method     | Table Name | Data Size | Table Attributes           | Time of Index's Construction | Time of Program's Execution    |
| ---------- | ---------- | --------- | -------------------------- | ---------------------------- | ------------------------------ |
| Linear     | gen_data   | 10,000    | id \| str1 \| str2 \| str3 | 0.103611 s                   | 0.000008 s                     |
| Normal     | gen_data   | 10,000    | id \| str1 \| str2 \| str3 | 0                            | 0.004412 s                     |

#### Extendible Hash

| Method     | Table Name | Data Size | Table Attributes           | Time of Index's Construction | Time of Program's Execution    |
| ---------- | ---------- | --------- | -------------------------- | ---------------------------- | ------------------------------ |
| Extendible | gen_data   | 10,000    | id \| str1 \| str2 \| str3 | 0.040020 s                   | 0.000006 s                     |
| Normal     | gen_data   | 10,000    | id \| str1 \| str2 \| str3 | 0                            | 0.006323 s                     |

`Bucket_max_size` will affect the efficiency of extendible hash method,
        due to it will directly affect the frequency of split.
        According to some related paper, we choose to assign 50 to bucket_size
        and finally get good performance.

### Reference

- [Extendible Hasing for COSC 311](https://emunix.emich.edu/~shaynes/Papers/ExtendibleHashing/extendibleHashing.html)
