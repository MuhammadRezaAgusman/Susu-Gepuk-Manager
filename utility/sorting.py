def selection_sort_transaksi(data):

    transaksi_urut = data.copy()

    for i in range(len(transaksi_urut) - 1):

        idx_max = i

        for j in range(i + 1, len(transaksi_urut)):

            if transaksi_urut[j]["total harga"] > transaksi_urut[idx_max]["total harga"]:
                idx_max = j

        transaksi_urut[i], transaksi_urut[idx_max] = (
            transaksi_urut[idx_max],
            transaksi_urut[i]
        )

    return transaksi_urut