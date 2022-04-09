seq_name = "chrom1"

for i in range(1,101):
    if i <= 20:
        print(f"chrom1 {i} 15")
    elif i <= 40:
        print(f"chrom2 {i} 43")
    else:
        print(f"chrom3 {i} 60")
